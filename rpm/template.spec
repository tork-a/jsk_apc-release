Name:           ros-indigo-jsk-apc2015-common
Version:        0.2.4
Release:        0%{?dist}
Summary:        ROS jsk_apc2015_common package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-gazebo-ros
Requires:       ros-indigo-jsk-demo-common
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roslint

%description
Common stacks for Amazon Picking Challenge 2015

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

