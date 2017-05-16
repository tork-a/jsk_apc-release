Name:           ros-indigo-jsk-2015-05-baxter-apc
Version:        3.0.1
Release:        0%{?dist}
Summary:        ROS jsk_2015_05_baxter_apc package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/jsk_2015_05_baxter_apc
Source0:        %{name}-%{version}.tar.gz

Requires:       numpy
Requires:       opencv-python
Requires:       python-progressbar
Requires:       python-scikit-image
Requires:       python-scikit-learn
Requires:       python-termcolor
Requires:       ros-indigo-baxter-gazebo
Requires:       ros-indigo-baxter-sim-hardware
Requires:       ros-indigo-baxtereus
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-imagesift
Requires:       ros-indigo-jsk-apc2015-common
Requires:       ros-indigo-jsk-pcl-ros
Requires:       ros-indigo-jsk-recognition-msgs
Requires:       ros-indigo-jsk-rqt-plugins
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-posedetection-msgs
Requires:       ros-indigo-roseus
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rosserial-arduino
Requires:       ros-indigo-rosserial-client
Requires:       ros-indigo-sound-play
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-turtlebot-description
BuildRequires:  gazebo-devel
BuildRequires:  ros-indigo-baxter-description
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-collada-urdf
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-euscollada
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-jsk-tools
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-roseus
BuildRequires:  ros-indigo-rosserial-arduino
BuildRequires:  ros-indigo-rosserial-client
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-xacro

%description
ROS package for Amazon Picking Challenge in May 2015

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed May 17 2017 Kentaro Wada <www.kentaro.wada@gmail.com> - 3.0.1-0
- Autogenerated by Bloom

* Mon May 08 2017 Kentaro Wada <www.kentaro.wada@gmail.com> - 3.0.0-0
- Autogenerated by Bloom

* Sat Oct 22 2016 Kentaro Wada <www.kentaro.wada@gmail.com> - 2.0.0-0
- Autogenerated by Bloom

* Sat Jul 16 2016 Kentaro Wada <www.kentaro.wada@gmail.com> - 1.5.1-0
- Autogenerated by Bloom

* Fri Jul 08 2016 Kentaro Wada <www.kentaro.wada@gmail.com> - 1.0.0-0
- Autogenerated by Bloom

* Fri Jun 24 2016 Kentaro Wada <www.kentaro.wada@gmail.com> - 0.8.1-0
- Autogenerated by Bloom

* Wed Jun 01 2016 Kentaro Wada <www.kentaro.wada@gmail.com> - 0.8.0-2
- Autogenerated by Bloom

* Fri Apr 15 2016 Kentaro Wada <www.kentaro.wada@gmail.com> - 0.2.4-0
- Autogenerated by Bloom

* Mon Apr 11 2016 Kentaro Wada <www.kentaro.wada@gmail.com> - 0.2.3-0
- Autogenerated by Bloom

* Tue Mar 08 2016 Kentaro Wada <www.kentaro.wada@gmail.com> - 0.2.2-0
- Autogenerated by Bloom

* Tue Mar 08 2016 Kentaro Wada <wkentaro@gmail.com> - 0.2.1-0
- Autogenerated by Bloom

* Tue Mar 08 2016 baxter <baxter@jsk.imi.i.u-tokyo.ac.jp> - 0.2.0-1
- Autogenerated by Bloom

* Tue Mar 08 2016 baxter <baxter@jsk.imi.i.u-tokyo.ac.jp> - 0.2.0-0
- Autogenerated by Bloom

