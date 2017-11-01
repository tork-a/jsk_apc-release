Name:           ros-indigo-jsk-apc2016-common
Version:        4.2.0
Release:        0%{?dist}
Summary:        ROS jsk_apc2016_common package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/jsk_apc2016_common
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-jsk-data
Requires:       ros-indigo-jsk-gui-msgs
Requires:       ros-indigo-jsk-recognition-msgs
Requires:       ros-indigo-message-filters
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-pcl-ros
Requires:       ros-indigo-qt-gui-py-common
Requires:       ros-indigo-resource-retriever
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rqt-gui
Requires:       ros-indigo-rqt-gui-py
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-tf2
Requires:       ros-indigo-tf2-eigen
Requires:       ros-indigo-tf2-ros
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-jsk-data
BuildRequires:  ros-indigo-jsk-gui-msgs
BuildRequires:  ros-indigo-jsk-recognition-msgs
BuildRequires:  ros-indigo-jsk-tools
BuildRequires:  ros-indigo-message-filters
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-pcl-ros
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roslint
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-tf2
BuildRequires:  ros-indigo-tf2-eigen
BuildRequires:  ros-indigo-tf2-ros

%description
The jsk_apc2016_common package

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

* Tue Mar 08 2016 wkentaro <wkentaro@todo.todo> - 0.2.0-1
- Autogenerated by Bloom

* Tue Mar 08 2016 wkentaro <wkentaro@todo.todo> - 0.2.0-0
- Autogenerated by Bloom

