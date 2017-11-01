Name:           ros-indigo-jsk-arc2017-common
Version:        4.2.0
Release:        0%{?dist}
Summary:        ROS jsk_arc2017_common package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/jsk_arc2017_common
Source0:        %{name}-%{version}.tar.gz

Requires:       pyserial
Requires:       ros-indigo-jsk-apc2016-common
Requires:       ros-indigo-jsk-data
Requires:       ros-indigo-jsk-pcl-ros
Requires:       ros-indigo-jsk-pcl-ros-utils
Requires:       ros-indigo-jsk-perception
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-rospy
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-jsk-data
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-roseus
BuildRequires:  ros-indigo-roslint
BuildRequires:  ros-indigo-rostest

%description
Common package for Amazon Robotics Challenge 2017 at JSK Lab.

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
* Wed Nov 01 2017 Kentaro Wada <www.kentaro.wada@gmail.com> - 4.2.0-0
- Autogenerated by Bloom

* Sat Oct 28 2017 Kentaro Wada <www.kentaro.wada@gmail.com> - 4.1.9-0
- Autogenerated by Bloom

* Thu Oct 26 2017 Kentaro Wada <www.kentaro.wada@gmail.com> - 4.1.8-0
- Autogenerated by Bloom

* Tue Oct 24 2017 Kentaro Wada <www.kentaro.wada@gmail.com> - 4.1.6-0
- Autogenerated by Bloom

* Mon Oct 23 2017 Kentaro Wada <www.kentaro.wada@gmail.com> - 4.1.5-0
- Autogenerated by Bloom

* Sun Oct 15 2017 Kentaro Wada <www.kentaro.wada@gmail.com> - 4.1.4-0
- Autogenerated by Bloom

* Thu Oct 12 2017 Kentaro Wada <www.kentaro.wada@gmail.com> - 4.1.3-0
- Autogenerated by Bloom

* Tue Jul 25 2017 Kentaro Wada <www.kentaro.wada@gmail.com> - 4.0.0-0
- Autogenerated by Bloom

* Thu May 25 2017 Kentaro Wada <www.kentaro.wada@gmail.com> - 3.0.3-0
- Autogenerated by Bloom

* Thu May 18 2017 Kentaro Wada <www.kentaro.wada@gmail.com> - 3.0.2-0
- Autogenerated by Bloom

* Wed May 17 2017 Kentaro Wada <www.kentaro.wada@gmail.com> - 3.0.1-0
- Autogenerated by Bloom

* Mon May 08 2017 Kentaro Wada <www.kentaro.wada@gmail.com> - 3.0.0-0
- Autogenerated by Bloom

