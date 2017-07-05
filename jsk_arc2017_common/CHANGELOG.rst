^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package jsk_arc2017_common
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3.1.0 (2017-06-30)
------------------
* Add mesh models for 36 objects
* update UpdateJSON and replace SaveJSON by Trigger
* add json_saver.py
* Refactor yaml file format
* Fix format
* Add thread lock to estimate_object_by_scale
* Change init of object estimation to srv
* Add object estimation by scale
* and_scale_rosserial -> ekew_i_driver
* Add object weight data
* remove non-item label in json generator
* update sample_pick_task json
* update pick_json_generator for new pick env
* update work_order_publisher for new shelf
* Place location config files in jsk_arc2017_baxter
* add publish_tote_boxes and interactive tote marker
* Move task config to jsk_arc2017_baxter
* Rename config collect_data -> collect_data_in_shelf
* add files for data collection
* Remove no need merge_depth_images.py
* add depth image merging nodes
* Deploy FCN32s trained on Dataset=v2, config=003
* add shelf_marker for stow_task
* add stow_json_generator and sample_stow_task json
* fix typo in pick_json_generator
* Add python module: get_object_names (`#2132 <https://github.com/start-jsk/jsk_apc/issues/2132>`_)
  * Add python module: get_object_names
  * Fix for flake8
  * Fix typo
* Make label_names.yml as just a name list
* Add log summarization script
* Improve logging in training script
* add easy picking task json files for mayfes demo
* Contributors: Kentaro Wada, Shingo Kitagawa, Shun Hasegawa, Yuto Uchimi

3.0.3 (2017-05-18)
------------------

3.0.2 (2017-05-18)
------------------
* Fix missing build depend on jsk_data
  - because install_data.py is run in Cmake
* Contributors: Kentaro Wada

3.0.1 (2017-05-16)
------------------
* Fix missing dependency on jsk_data
* fix typo in WorkOrderPublisher
* sort cardboard by box size and give ABC name
* Contributors: Kentaro Wada, Shingo Kitagawa

3.0.0 (2017-05-08)
------------------
* Fix style of nodes in roslaunch files
* Add sample for work_order_publisher
* Fix name of sample_set_location_in_rosparam
* Fix for move of data/objects -> config/objects
* Don't use ROS in training script
* add sample launch for set_location_in_rosparam
* print stdout in set_location_in_rosparam
* fix typo in set_location_in_rosparam
* remove unused package and sort alphabetically
* use label_names.yaml instead of objects.txt
* set myself as a author
* update json generator script
* mv pick_work_order_server -> work_order_publisher
* replace publish_shelf_bin_bbox to existing node
* remove unnecessary lines in CMakeLists
* move json -> data/json
* switch cardboard place
  cardboard a: left upper
  cardboard b: left lower
  cardboard c: right
* add abandon items for work_order_server
* fix typo in package.xml in jsk_arc2017_common
* update shelf_bin position config
* set cardboard id as A,B,C in work_order
* add pick_work_order_server test
* fix typo in arc2017 json item_location_file.json
* add myself as a maintainer
* update CMakelists.txt and package.xml for roseus
* add set_location_in_rosparam node
* format bin_name as capital alphabet
* update pick_work_order_server for new json format
* update json generator and sample in correct format
* add example json and box size config
* add pick_work_order_server for arc2017
* introduce new WorkOrder&WorkOrderArray msg
* add sample_pick.json and json generate script
* add setup_for_pick.launch for arc2017
* add shelf_interactive_marker.yaml
* add publish_shelf_bin_bbox for new shelf
* Add python-serial to run_depends
* Fix typo
* Read weight data from AND scale
  - new file:   and_scale_rosserial.py
* Ignore AR20170331
* Update model file with stacking data augmentation
* Add data augmentation method with stacking
* Update api of torchfcn
* Improve imgaug
* Simplify config
* Update data with AR_20170331 dataset
* Add link to wiki
* Neat config & log handling
* Add ROS sample of FCNObjectSegmentation
* Add sample data of JSKV1 dataset
* Fix path of data
* Change path of JSKV1
* Add option to skip dataset with stamp
* Show datetime in annotation
* Improve view_jsk_v1
  - p for back
  - show timestamp
* Training experiments
* Update config
* Check label.npz existence
* Sort dirs for annotation
* Fix locking
* Show stamp_dir
* Lock for parallel annotation
* Augument image using imgaug
* Fix data field name
* 002_fcn32s_dataset_v1.yaml
* Fix for flake8
* Add requirements.txt
* Training script of FCN32s
* Add dataset class for JSKARC2017From16
* Add script to convert JSKAPC2016 to ARC2017
* Split dataset for train and valid
* Remove underscore for consistent names
* Add dataset.py
* Neat visualization of dataset
  - Show size of All and Annotated
  - Show label names
* Script to view dataset before/after annotated
* Update data using Training_items_20170320_fixed.zip
* Save data with compression
* Save label as npz file with compression
* Smaller size of object list
* Annotation script for JSK_V1 dataset
* Add script to list objects
* Visualize object list
* Parse AR_20170224 dataset
* Contributors: Kentaro Wada, Shingo Kitagawa
