^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package jsk_arc2017_baxter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

4.0.0 (2017-07-24)
------------------
* Improve rosoncole output on rviz
* Add right_main and left_main flag to pick/stow.launch
* Re-calibration right_hand hand-eye extrinsic params
* do not stop-grasp in pinch
* avoid collision with head_pan
* Error message about movable region
* Fix ik failure in pinching
* Fix for record and play the rosbag
* Fix finger angle in spherical position
* Re-calibrate finger tendon
* Fix movable region
* Fix rotation of gripper to avoid IK failure
* Move reseting gripper to pick-object-with-movable-region
* Lift gripper to avoid collision
* Use rotate-wrist-ik in pick-object
* Use near-wall in suction
* Use near-wall in pinch
* Add :check-near-wall
* reset gripper rotation after lifting object
* Revert "reset gripper rotation after lifting object"
  This reverts commit 2c6935465c32e1ef110f61074a83d9bf89b6cbb7.
* modify overlook-pose offset
* reset gripper rotation after lifting object
* Improve pinching
* Don't extend prismatic joint in :stop-grasp
* reset weight error for pick task
* use spherical grasp-pose in suction picking
* use prismatic-based approach in :pick-object
* update place-object motion
* update cardboard_marker yaml
* refine moveit scene operation in main
* add cardboard-rack scene methods
* add and delete cardboard-scene separately
* add cardboard rack leg scene methods
* Re-calibrate vacuum pad joint
* Set multiturn after calib
* Add euslisp interface to prismatic calib
* Enable dynamic calib of prismatic joints
* Add action for prismatic joint calib
* add object-in-hand as attached object scene
* update state_server for new state_machines
* check start picking and redesign state_machine
* introduce grasp_style_server in task system
* add :get-grasp-style method
* fix typo in state_server.py
* Use angle-vector-raw
* Better drawing from box after suction grasp of object
* use only centroid for determining obj-pos
* slow down return-object motion
* fix typo in baxter-interface.l moveit-environment
* Fix typo
* Dynamic movable region in :pick-object method
* do not use :revert-if-fail
* use :rotation-axis nil in pinch
* restrict pinch-yaw : -pi/2 ~ pi/2
* change how to sethash proximity
* add :finger-proximity in :wait-interpolation-until in pinch
* use hash-table in proximities-
* remove unused valiable : middle proximity sensor
* change prismatic joint length during pinch
* Save scale value outputs correctly
* change box index in arc-interface.l to pick largest boundingbox
* change keyword :proximity -> :finger-proximity
* add proximity condition in :wait-interpolation-until
* add n-random key in get-larget-target-object
* Fix load direction
* Add missing slot variable
* move gripper config in robots/ dir
* Use baxter_simple.urdf in jsk_arc2017_baxter baxter.xacro
* Fix error of weight_candidates_refiner for expo (20g)
* update get-next-target-bin test
* skip finished-objects in :get-largest-object-index
* fix typo: add missing local variable
* set objects rosparam in :wait-for-user-input
* add :reset-object-tables method
* use hash-table for objects controll
* Adjust hand-eye extrinsic parameters for both hands (`#2325 <https://github.com/start-jsk/jsk_apc/issues/2325>`_)
* modify place object position for stable place
* increase weight error for pick task
* modify move-arm-body->tote-overlook-pose position
* update shelf and tote marker
* add NOQA for long line in state_server
* fix typo: rename to check-trail-fail-count state
* Stabilize flex sensor
* Add rosbag record for pick and stow
* Use box_type instead of boxes to select bin or tote
* enable data collection in tote
* add get_object_weights() in jsk_arc2017_common
* Reasonable time-limit for eus test codes
* add get-next-target-bin test
* reset recognize-fail-count in check-recognize-fail-count
* add check-recognize-fail-count state in pick
* select work order dynamically
* add select-work-order-in-bin method
* add :get-next-target-bin method
* enable cpi decomposer for labels in pick task
* line slots in alphabetical order
* Remove outlier values in flex sensor values
* updated extrinsic parameter between depth_optical_frame and rgb_optical_frame
* updated IR intrinsic parameter
* reset picking-fail-count after verify-object
  this is because `:graspingp` is always `t`, when `grasp-style` is
  `:pinch`
* add check trail fail count
* remove obj from postponed list when finished
* add postponed-objects in slots
* subscribe work-order msg only once
  current system only needs to subscribe work order once in the beginning.
* add finished-objects slots
* line slots in alphabetical order
* Fix larm IK to accept :use-gripper nil
* update stow.rviz
* update pick.rviz
* use raw instead to make lifting object faster
* do not wait move-hand in pick-object
* add put stop-grasp in proper position
* try picking twice and not recognize
* add max_acceleration for right_s0 in joint_limits
* Update doc for create_dataset2d
* Can select both / right / left
* Create dataset V2
* Update README for look_around_bins
* Contributors: Kentaro Wada, Naoya Yamaguchi, Shingo Kitagawa, Shun Hasegawa, Yuto Uchimi

3.3.0 (2017-07-15)
------------------
* Add look_around_bins experiment
* Update hand action state in :hand-interpolatingp
* Clean up :graspingp
* Always set graspingp of pinching as true
* Detect serial blocked and restart
* Re-calibrate left vacuum pad joint
* Move gripper upward in :return-object to prevent collision
* Add initialization of left hand
* Fix for slow tf_to_transform
* Rotate head monitor before collect_data_in_shelf
* Use transformable_markers_client in collect_data_in_shelf
* Disable moveit to see in shelf
* add sleep after publishing moveit scene msg
* Fix :get-arm-controller for larm (`#2271 <https://github.com/start-jsk/jsk_apc/issues/2271>`_)
* Program to test hand-eye coordination (`#2265 <https://github.com/start-jsk/jsk_apc/issues/2265>`_)
  * Test hand eye coordination
  * Add test_hand_eye_coordination example
* add controller-type in cancel-angle-vector (`#2266 <https://github.com/start-jsk/jsk_apc/issues/2266>`_)
* Make @pazeshun happy by hand-eye calibration (`#2264 <https://github.com/start-jsk/jsk_apc/issues/2264>`_)
  * Make @pazeshun happy by hand-eye calibration
  * Remove initial pose setting in stereo_astra_hand.launch
* fix indent in baxter-interface.l
* add arm-head-controller, exclude head from arm-controller
* Fix topic of republish_gripper_sensor_states.py
* Fix typo in :finger-closep
* Fix line length
* vacuum_gripper.srdf.xacro -> gripper_v6.srdf.xacro
* Adjust pick and stow to left gripper-v6
* Adjust moveit config to left gripper-v6
* Adjust baxter interface to left gripper-v6
* Adjust baxter.launch to left gripper-v6
* Add left gripper-v6 to gripper launch
* Add udev rule for left gripper-v6
* Add Arduino firm for left gripper-v6
* Add config for left gripper-v6
* Add left gripper-v6 to robot model
* Add mesh of left gripper-v6
* loosen weight error limit
* Enable to change offset of flex threshold in :wait-interpolation-until
* Improve logging of :wait-interpolation-until
* Fix for euslint
* divide too long lines into several lines
* add check pinch graspability program
* add midpoint when returning from place object
* remove duplicated file
* add unix::sleep in while loop
* change error to ros::ros-error
* wait for :interpolatingp
* use proximity in :start-grasp
* rotate gripper according to BoundingBox pose before pinching
* check if angle-vector length is 0 or 2
* add scale methods in arc-interface
* refine weight_candidates_refiner node
* add scale node in setup launch
* add scale.launch
* add use_topic and input_candidates args
* update place motion
* make cardboard bbox bigger to avoid collision
* disable moveit and add fixme
* escape when both arm waiting other arm
* fix typo in main program
* try twice when grasp-stye is :suction
* change head_pan angle to suppress warning message
* add moveit debug arg in baxter.launch
* add midpoint for place object
* Fix encoding of depth: use 32FC1
* Stop using right side depth sensor to avoid ir conflicts
* Calibrate intrinsic parameters
* Use software registration for depth registration
* Revert `#2235 <https://github.com/start-jsk/jsk_apc/issues/2235>`_ 'Grasp using proximity'
  Because
  - We cannot use left hand with this change.
  - Has typo.
* update pick.rviz
* Add test for :recognize-bboxes
* update add-cardboard-scene method
* fix typo in arc-interface
* update transformable_markers_client node name
* modify to set offset in world coords
* update ik->cardboard-center to use subscribed bbox
* add recognize-cardboard-boxes method
* add cardboard markers
* order depends of jsk_arc2017_baxter alphabetically
* add smach_viewer args in main launch
* add smach_viewer as run_depend
* apply stereo to setup_for_pick/stow.launch (fixed 3e91e84)
* Fix topic name in euslisp
* Replace publish_boxes to transformable_markers_client/output/boxes
* Use transformable_markers_client to adjust scene
* fix typo  :rarm -> arm
* correct open/close parenthesises
* add exit after ros::ros-error
* add unix::sleep in while loop
* change error to ros::ros-error
* correct indent 3
* wait for :interpolatingp
* correct indent 2
* correct indent
* use proximity in :start-grasp
* rotate gripper according to BoundingBox pose before pinching
* check if angle-vector length is 0 or 2
* Add sleep in :wait-interpolation-until loop
* replace bg_label by ignore_labels
* use arc2017 object_segmentation_3d in stow task
* return nil when largest box is not found
* Show FCN results in stow.rviz
* Improve stow.rviz with transparent moveit scene
* Resolve dependency on position_controller/joint_trajectory_controller
* Revert "Apply stereo camera to setup_for_pick/stow.launch"
* do not use fused RGB as FCN input
* apply stereo camera to setup_for_pick/stow.launch
* Contributors: Kentaro Wada, Naoya Yamaguchi, Shingo Kitagawa, Shun Hasegawa, Yuto Uchimi

3.2.0 (2017-07-06)
------------------
* add in_hand_recognition launch
* add astra_external launch
* add set-target-location method
* update candidates for segmentation via topic
* Avoid collision to shelf or tote in pick-object
* Fix offset of place-object in pick for moveit
* Ignore collision between fingers and other gripper parts
* Wait for opposite return-object in pick task
* Don't turn gripper over in ik->cardboard-center
* Fix logging of wait-interpolation-until
* Fold fingers more tightly before suction-object
* Move pinch-yaw to key in try-to-pick-object
* Add meta method :try-to-pick-object and :try-to-suction-object
* Rewrite waiting for :interpolatingp
* Reset picking-fail-count for new target obj
* Ignore unstable flex value and calib flex offset
* Don't use prismatic load for graspingp and calib thresholds
* Calib finger init state of try-to-pick-object
* Re-calibrate finger tendon winder
* Avoid collision between fingers
* Add logging to try-to-pinch-object
* Stop grasp in return-from-pick-object
* Add pinching to pick
* Don't back to fold-pose-back until 2nd failure in pick
* Add :try-to-pinch-object and use it in stow
* Use wait-interpolation-until in try-to-suction-object
* Split try-to-pick-object to try-to-pick-object-v4 and try-to-suction-object
* Enable :pick-object-with-movable-region to get grasp-style
* Add set-grasp-style state in stow
* Don't back to fold-pose-back until 2nd failure in stow
* Enable to set palm endpoint as move-target in IK
* Enable to select no gripper controller
* Add :wait-interpolation-until
* Erase one-shot-subscribe in pressure calib
* Erase one-shot-subscribe and consider pinching in :graspingp
* Enable :start-grasp and :stop-grasp to move hand
* Add get func of gripper sensor states
* Enable to get gripper sensor states
* Create object_segmentation_3d.launch in jsk_arc2017_common
* return nil when largest bbox subscription timeout
* Calibrated extrinsic parameters of right_hand_stereo by @YutoUchimi
* Calibrated extrinsic parameters of right_hand_stereo by @YutoUchimi
* introduce left stereo astra camera
  thanks to @YutoUchimi and @pazeshun
* modify not to use moveit unnecessary part
* modify joint_limits for moveit
* Visualize json_dir on baxter's xdisplay
* introduce stereo Astra Mini S camera into both hands
* modify json save dir
* save json in pick task
* modify :update-json api in arc-interface
  (send self :update-json target-obj :src :tote :dst (cons :bin target-bin))
  (send self :update-json target-obj :src (cons :bin target-bin) :dst (cons :cardboard target-cardboard))
  (send self :update-json target-obj :src (cons :bin target-bin) :dst (cons :bin target-bin))
* calibrate intrinsic parameter of left hand camera
* Contributors: Kentaro Wada, Shingo Kitagawa, Shun Hasegawa, Yuto Uchimi

3.1.0 (2017-06-30)
------------------
* Fix for euslint
* Update data collection motion
* Change save_dir in dynamic
* Update motion
* Use last 3 frames as texture
* Generate texture model of objects by kinfu
* move set segmentation candidates method
* update UpdateJSON and replace SaveJSON by Trigger
* correct indent in stow-interface.l
* use fcn in stow task recognition pipeline
* remove unused parameters in setup_for_stow
* move hand camera nodes to setup launch
* update stow_task environment config
* add json_saver methods and save json in main loop
* add json_saver.py
* use latest fcn model for segmentation
* change state-machine frequency: 1.0 -> 2.0 hz
* add path-constraints for place object
* update pick motion parameters for new env
* update cardboard moveit methods
* update cardboard pos for new env
* update shelf_bin and shelf_marker for new shelf
* fix typo in baxter.launch
* Merge pull request `#2154 <https://github.com/start-jsk/jsk_apc/issues/2154>`_ from wkentaro/test_task_arc_interface
  Add test for motion code in both pick and stow tasks
* add baxter-moveit-environment for gripper-v6
* update right_vacuum_gripper.xacro for gazebo
* add baxter_sim.launch in jsk_arc2017_baxter
* add moveit config for gripper-v6
* Remove no need newline in tote.yaml
* Merge branch 'master' into test_task_arc_interface
* Don't load old robot model
* Revert mvit-env and mvit-rb
* Adjust gravity compensation automatically
* Fix parenthesis and add comment to move-hand
* Adjust rvizconfig to gripper-v6
* Fix arc-interface to support left hand
* Use only left astra mini
* Apply IK additional check to avoid collision to bin wall
* Use wait-interpolation-until-grasp to prevent unnecessary push
* Fix wait-interpolation-until-grasp for first interpolatingp nil
* Fix rarm pressure threshold
* Use right_hand_left_camera in setup_for_stow
* Fold fingers in picking to avoid collision
* Add finger init motion to pick and stow init
* Use right_hand_left_camera in setup_for_pick
* Disable rviz in default of stereo_astra_hand
* Fix linter target
* Adjust euslisp codes to baxter with right gripper-v6
* Add baxter.launch for right gripper-v6
* Add ros_control layer for gripper-v6
* Add dxl controller for gripper-v6
* Add baxter model with right gripper-v6
* Place location config files in jsk_arc2017_baxter
* state_server accept Ctrl-C keyboard interruption
* remove duplicated line
* update stow-arc-interface test
* add publish_tote_boxes and interactive tote marker
* Add test for arc-interface for stow task
* Generalize visualize-bins by renaming it to visualize-boxes
* Publish source location of task in setup_for\_(pick|stow).launch
* Fix typo and test arc_interface for pick task
* Move task config to jsk_arc2017_baxter
* Yet another refactoring of stereo_astra_hand.launch
* add "task" argument to select shelf_marker.yaml
* Refactoring right_hand rgb-d camera stereo
* fix typo
* add files for data collection
* Update tf from right to left by using project matrix
* Update transformation from left_hand to right_hand
* Use moveit to avoid collision to box and shelf
* Collect data in shelf bins
* Fix typo in filename
* Update rvizconfig name
* Update rvizconfig
* Reuse possible code by using include in roslaunch file
* Don't use laser
* Refactor stereo_astra_hand.launch
* Remove spam.launch
* Improve visualization of triple fusion
* support quad fusion
* update calibration yaml files
* Quad fusion using depth from laser scan
* test for laser depth_image_creator
* add tilt laser to stereo system
* Launch right stereo camera in baxter.launch
* calibrated extrinsic parameter
* add depth image merging nodes
* add monoral_camera_info files
* move stereo_camera_info files from jsk_2016_01_baxter_apc to jsk_arc2017_baxter
* move stereo_astra.launch to launch/setup/ directory
* introduce stereo astra_mini_s
* Add create_udev_rules and simplify README
* Merge pull request `#2152 <https://github.com/start-jsk/jsk_apc/issues/2152>`_ from pazeshun/fix-bugs-stow
  Fix small bugs added when adding stow
* Don't change target-obj in verify-object
* Revert offsets for bin overlook pose
* Fix mistakes of arg and return value
* Use fold-pose-back in arc-interface
* Fix translation in ik->bin-center and ik->tote-center
* add moveit-p slot in stow-interface
* add moveit-p slot in pick-interface
* Add Arduino sketch for sparkfun sensor
* Remove unused constants and functions in firm
* Lighten GripperSensorStates msg
* add main program state machine test
* add state_server test for stow task
* fix indent of main launch files
* use symbol-string to replace string-upcase
* translate bin/tote coords in local coordinate
* fix typo in arc-interface
* add stow.launch and stow.rviz
* add stow-main.l
* add stow-interface.l
* update pick methods and add :pick-object-in-tote
* add stow_task methods and slots
* mv ik->cardboard-entrance -> ik->cardboard-center
* replace :ik->bin-entrance by  ik->bin-center
* use bin-cubes- instead of bin-boxes-
* reset order in wait-for-user-input
* rename to :recognize-target-object and update
  :recognize-objects-in-bin -> :recognize-target-object
* update pick-main state machine
* state_server support stow_task and set rosparam
* add shelf_marker for stow_task
* fail-count -> picking-fail-count for pick task
* add setup_for_stow launch
* add &rest args in :fold-pose-back method
* move fold-pose-back method in arc-interface
* Publish proximity sensor values with other gripper sensor states (`#2125 <https://github.com/start-jsk/jsk_apc/issues/2125>`_)
  * add FA-I sensor to gripper-v5
  * add GripperSensorStates republish program
  * Rename and refactor republish_gripper_sensor_states.py
  * rename finger flex topic
  * add eof to .travis.rosinstall
* fix typo in pick-interface.l (`#2133 <https://github.com/start-jsk/jsk_apc/issues/2133>`_)
* add roseus_smach run_depend in package.xml
* add lint test for node_scripts
* add state_server test
* add :get-state method in arc-interface
* add FIXME smach_viewer in main.launch
* add state_server in main.launch
* use smach state-machine in pick-main.l
* add state_server methods in arc-interface
* add state_server.py
  this server collect state of both arms
  and determine which arm can start picking
* add UpdateState GetState and CheckCanStart srv
* add pick-interface
* move :send-av in arc-interface
* use baxter-robot for init robot and add FIXME
* add :spin-off-by-wrist in arc-interface
* arc-interface inherits propertied-object
* use *ri* *baxter* in arc-interface
  I follwed *tfl* usage in robot-interface.l.
* use global var *tfl* set in robot-interface
* rename *arc* -> *ti*
  *ti* is named after task-interface
* use robot of slots in baxter-interface
* split arc-interface and baxter-interface
* Add Arduino firmware for right gripper-v6
* fix bug in pick-main
* update move overlook method to support all bins
* modify :ik->bin-entrance
* do not wait head motion
* modify movable region
* modify overlook-pose
* move point-shelf-position.l
* rename detect-bin-position -> point-shelf-position
* add require lines and show warn message
* redefine detect-bin-position() in another file
* point ideal position of bin
* set movable region for bin narrower in order not to collide with bin
* improve motion in :place_object
* remove inefficient motion in :recognize_objects_in_bin
* calibration for rarm in the beginnig, and after that larm. not simultaneously.
* use key in pick-init
* use angle-vector-raw in pick method
* fix typo in moveit methods
* add pick.rviz in jsk_arc2017_baxter
* set default arg moveit as true
* add moveit arg in pick launch
* add moveit scenes in pick-main
* add moveit methods in arc-interface
* rename detect-bin-position -> point-shelf-position
* add require lines and show warn message
* redefine detect-bin-position() in another file
* point ideal position of bin
* do not wait head motion
* modify movable region
* modify overlook-pose
* use key in pick-init
* use angle-vector-raw in pick method
* fix typo in moveit methods
* add pick.rviz in jsk_arc2017_baxter
* set default arg moveit as true
* add moveit arg in pick launch
* add moveit scenes in pick-main
* add moveit methods in arc-interface
* refine place_object motion (`#2103 <https://github.com/start-jsk/jsk_apc/issues/2103>`_)
  * remove and move rosparam and add TODO in pick-main
  * refine place_object motion
* fix :pick_object (`#2101 <https://github.com/start-jsk/jsk_apc/issues/2101>`_)
* Contributors: Kei Okada, Kentaro Wada, Naoya Yamaguchi, Shingo Kitagawa, Shun Hasegawa, Yuto Uchimi, YutoUchimi

3.0.3 (2017-05-18)
------------------
* Add roseus as build_depend
* update midpose to go back fold-pose-back (`#2093 <https://github.com/start-jsk/jsk_apc/issues/2093>`_)
* Contributors: Kentaro Wada, Shingo Kitagawa

3.0.2 (2017-05-18)
------------------

3.0.1 (2017-05-16)
------------------
* Move astra_hand.launch from setup_for_pick.launch to baxter.launch
* fix typo in CMakeLists
* Fix for moved euslint to jsk_apc2016_common
* Depends at test time on jsk_2016_01_baxter_apc
* add wait condition for wait_for_user_input
* got to wait_for_opposite_arm first
* update waiting condition
* fix typo in arc-interface
* mv euslint to jsk_apc2016_common package
* Contributors: Kentaro Wada, Shingo Kitagawa, YutoUchimi

3.0.0 (2017-05-08)
------------------
* add TODO in util.l
* rename opposite-arm -> get-opposite-arm
* move get-bin-contents to arc-interface
* format apc -> arc for ARC2017
* remove unused package and sort alphabetically
* add find_package jsk_2016_01_baxter_apc in test
* refer related issue in TODO
* move some util func in apc-interface
* add TODO: make apc-inteface and pick-interface class properly
* make tf->pose-coords as a method of apc-interface
* rename arg launch_main -> main
* set myself as a author
* mv pick_work_order_server -> work_order_publisher
* replace publish_shelf_bin_bbox to existing node
* improve euslint to accept path
* remove unnecessary lines in CMakeLists
* update pytorch fcn model file
* place manager in ns
* fix and improve let variables
* use arm2str instead of arm-symbol2str
* improve picking motion
* when object is not recognized, wait opposite arm
* rename get-movable-region -> set-movable-region
* modify pick object motion
* angle-vector use :fast and :scale
* update overlook-pose to avoid aggresive motion
* rename baxter-interface -> apc-interface
* fix typo and improve euslisp codes
* fix typo in pick.launch for jsk_arc2017_baxter
* add pick.launch for arc2017
* add euslint in jsk_arc2017_baxter
* add euslisp codes for arc2017
* add myself as a maintainer
* update CMakelists.txt and package.xml for roseus
* move baxter.launch to setup
* add setup_for_pick.launch for arc2017
* add baxter.launch for arc2017
* move collect_data_in_bin in launch/main
* add run_depend in jsk_arc2017_baxter
* Add link to wiki
* Fix typo in collect_data_in_bin.launch
* Save tf and bin_name also
* Save tf also
* Save data with compression
* Update save dir
* Add data_collection program in bin
* Contributors: Kentaro Wada, Shingo Kitagawa
