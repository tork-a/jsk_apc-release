#!/usr/bin/env python

import datetime
import os
import os.path as osp
import warnings

import click
import cv2
import dateutil.parser
import fcn
import matplotlib.cm
import numpy as np
import skimage.io

import jsk_recognition_utils
import rospkg
import yaml


PKG_DIR = rospkg.RosPack().get_path('jsk_arc2017_common')


def colorize_depth(depth, min_value=None, max_value=None):
    """Colorize depth image with JET colormap."""
    min_value = np.nanmin(depth) if min_value is None else min_value
    max_value = np.nanmax(depth) if max_value is None else max_value
    if np.isinf(min_value) or np.isinf(max_value):
        warnings.warn('Min or max value for depth colorization is inf.')

    colorized = depth.copy()
    nan_mask = np.isnan(colorized)
    colorized[nan_mask] = 0
    colorized = 1. * (colorized - min_value) / (max_value - min_value)
    colorized = matplotlib.cm.jet(colorized)[:, :, :3]
    colorized = (colorized * 255).astype(np.uint8)
    colorized[nan_mask] = (0, 0, 0)
    return colorized


@click.command()
@click.option('-s', '--start')
def main(start):
    dataset_dir = osp.join(PKG_DIR, 'data/datasets/JSKV1')
    if not osp.exists(dataset_dir):
        print('Please install JSKV1 dataset to: %s' % dataset_dir)
        quit(1)

    label_files = []
    for stamp_dir in os.listdir(dataset_dir):
        stamp_dir = osp.join(dataset_dir, stamp_dir)
        label_file = osp.join(stamp_dir, 'label.npz')
        if osp.exists(label_file):
            label_files.append(label_file)
        else:
            label_files.append(None)
    print('==> Size of dataset: All: %d, Annotated: %d.' %
          (len(label_files), len(list(filter(None, label_files)))))

    with open(osp.join(PKG_DIR, 'config/label_names.yaml')) as f:
        object_names = yaml.load(f)['label_names']
    object_names.append('__unlabeled__')

    print('==> Press keys: [q] to quit, [n] to go next, [p] to go previous')
    stamp_dirs = list(sorted(os.listdir(dataset_dir)))
    i = 0
    while True:
        stamp = datetime.datetime.fromtimestamp(int(stamp_dirs[i]) / 1e9)
        if start and stamp < dateutil.parser.parse(start):
            i += 1
            continue
        start = None

        stamp_dir = osp.join(dataset_dir, stamp_dirs[i])
        print('%s: %s' % (stamp.isoformat(), stamp_dir))

        img_file = osp.join(stamp_dir, 'image.jpg')
        img = skimage.io.imread(img_file)

        depth_file = osp.join(stamp_dir, 'depth.npz')
        depth = np.load(depth_file)['arr_0']
        depth_viz = colorize_depth(depth, min_value=0.4, max_value=1.0)

        label_file = osp.join(stamp_dir, 'label.npz')
        if osp.exists(label_file):
            label = np.load(label_file)['arr_0']
            mask_unlabeled = label == -1
            label[mask_unlabeled] = object_names.index('__unlabeled__')
            img_labeled = img.copy()
            img_labeled[mask_unlabeled] = \
                np.random.randint(0, 255, (mask_unlabeled.sum(), 3))
            label_viz = fcn.utils.draw_label(
                label, img_labeled, len(object_names),
                dict(enumerate(object_names)))
        else:
            label_viz = np.zeros_like(img)

        viz = jsk_recognition_utils.get_tile_image([img, label_viz, depth_viz])

        cv2.imshow('view_jsk_v1', viz[:, :, ::-1])
        key = cv2.waitKey(0)
        if key == ord('q'):
            break
        elif key == ord('n'):
            i += 1
        elif key == ord('p'):
            i -= 1
        else:
            continue


if __name__ == '__main__':
    main()
