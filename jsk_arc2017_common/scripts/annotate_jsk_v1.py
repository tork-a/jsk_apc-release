#!/usr/bin/env python

import datetime
import json
import os
import os.path as osp
import shlex

import cv2
import labelme
import numpy as np
import PIL.Image
import skimage.io
import subprocess32 as subprocess

import rospkg


PKG_DIR = rospkg.RosPack().get_path('jsk_arc2017_common')


def json_to_label(json_file):
    data = json.load(open(json_file))

    img = labelme.utils.img_b64_to_array(data['imageData'])
    shapes = []
    shelf_shape = None
    for shape in data['shapes']:
        if shape['label'] == '41':
            if shelf_shape is not None:
                raise RuntimeError
            shelf_shape = shape
        else:
            shapes.append(shape)

    if shelf_shape is None:
        raise RuntimeError

    lbl = np.zeros(img.shape[:2], dtype=np.int32)
    lbl.fill(-1)

    lbl_shelf, _ = labelme.utils.labelme_shapes_to_label(
        img.shape, [shelf_shape])
    mask_shelf = lbl_shelf == 1
    lbl[mask_shelf] = 41

    lbl_obj, lbl_values_str = labelme.utils.labelme_shapes_to_label(
        img.shape, shapes)
    for i, lbl_val in enumerate(lbl_values_str):
        if lbl_val == 'background':
            continue
        mask_obj = lbl_obj == i
        lbl[mask_obj] = int(lbl_val)

    return lbl


def main():
    dataset_dir = osp.join(PKG_DIR, 'data/datasets/JSKV1')
    if not osp.exists(dataset_dir):
        print('Please install JSKV1 dataset to: %s' % dataset_dir)
        quit(1)

    objlist_file = osp.join(PKG_DIR, 'data/others/object_list_5x8.jpg')
    objlist = cv2.imread(objlist_file)
    scale = 1000. / max(objlist.shape[:2])
    objlist = cv2.resize(objlist, dsize=None, fx=scale, fy=scale)

    cmap = labelme.utils.labelcolormap(41)

    for stamp_dir in sorted(os.listdir(dataset_dir)):
        stamp = datetime.datetime.fromtimestamp(int(stamp_dir) / 1e9)
        stamp_dir = osp.join(dataset_dir, stamp_dir)
        if not osp.isdir(stamp_dir):
            continue
        json_file = osp.join(stamp_dir, 'label.json')
        img_file = osp.join(stamp_dir, 'image.jpg')
        lbl_file = osp.join(stamp_dir, 'label.npz')
        lbl_viz_file = osp.join(stamp_dir, 'label_viz.jpg')

        lock_file = osp.join(stamp_dir, 'annotation.lock')
        if osp.exists(lock_file):
            continue

        if not osp.exists(json_file):
            open(lock_file, 'w')

            print('%s: %s' % (stamp.isoformat(), stamp_dir))
            cmd = 'labelme %s -O %s' % (img_file, json_file)
            output = subprocess.Popen(shlex.split(cmd))

            returncode = None
            while returncode is None:
                try:
                    output.communicate(timeout=1)
                    returncode = output.returncode
                except subprocess.TimeoutExpired:
                    pass
                except KeyboardInterrupt:
                    break
                cv2.imshow('object list', objlist)
                cv2.waitKey(50)

            os.remove(lock_file)

            if returncode != 0:
                output.kill()
                break

        if not (osp.exists(lbl_file) and osp.exists(lbl_viz_file)):
            img = skimage.io.imread(img_file)
            lbl = json_to_label(json_file)
            lbl_viz = skimage.color.label2rgb(
                lbl, img, bg_label=0, colors=cmap[1:])
            np.savez_compressed(lbl_file, lbl)
            skimage.io.imsave(lbl_viz_file, lbl_viz)


if __name__ == '__main__':
    main()
