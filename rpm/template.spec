Name:           ros-indigo-jsk-2016-01-baxter-apc
Version:        4.1.8
Release:        0%{?dist}
Summary:        ROS jsk_2016_01_baxter_apc package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/jsk_2016_01_baxter_apc
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-baxter-core-msgs
Requires:       ros-indigo-baxter-gazebo
Requires:       ros-indigo-baxter-sim-controllers
Requires:       ros-indigo-baxter-sim-io
Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-controller-manager
Requires:       ros-indigo-dynamixel-controllers
Requires:       ros-indigo-dynamixel-msgs
Requires:       ros-indigo-gazebo-ros
Requires:       ros-indigo-hardware-interface
Requires:       ros-indigo-jsk-2015-05-baxter-apc
Requires:       ros-indigo-jsk-apc2016-common
Requires:       ros-indigo-jsk-baxter-startup
Requires:       ros-indigo-jsk-data
Requires:       ros-indigo-jsk-interactive-marker
Requires:       ros-indigo-jsk-recognition-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-roseus-mongo
Requires:       ros-indigo-rosserial-python
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-transmission-interface
BuildRequires:  openssl-devel
BuildRequires:  ros-indigo-baxter-core-msgs
BuildRequires:  ros-indigo-baxter-description
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-collada-urdf
BuildRequires:  ros-indigo-control-msgs
BuildRequires:  ros-indigo-controller-manager
BuildRequires:  ros-indigo-dynamixel-msgs
BuildRequires:  ros-indigo-euscollada
BuildRequires:  ros-indigo-hardware-interface
BuildRequires:  ros-indigo-jsk-2015-05-baxter-apc
BuildRequires:  ros-indigo-jsk-data
BuildRequires:  ros-indigo-jsk-tools
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roseus
BuildRequires:  ros-indigo-roslint
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-transmission-interface
BuildRequires:  ros-indigo-xacro
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  rubygems

%description
Common stacks for Amazon Picking Challenge 2016

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
* Thu Oct 26 2017 Hasegawa Shun <pazeshun3684@gmail.com> - 4.1.8-0
- Autogenerated by Bloom

* Tue Oct 24 2017 Hasegawa Shun <pazeshun3684@gmail.com> - 4.1.6-0
- Autogenerated by Bloom

* Mon Oct 23 2017 Hasegawa Shun <pazeshun3684@gmail.com> - 4.1.5-0
- Autogenerated by Bloom

* Sun Oct 15 2017 Hasegawa Shun <pazeshun3684@gmail.com> - 4.1.4-0
- Autogenerated by Bloom

* Thu Oct 12 2017 Hasegawa Shun <pazeshun3684@gmail.com> - 4.1.3-0
- Autogenerated by Bloom

* Tue Jul 25 2017 Hasegawa Shun <pazeshun3684@gmail.com> - 4.0.0-0
- Autogenerated by Bloom

* Thu May 25 2017 Hasegawa Shun <pazeshun3684@gmail.com> - 3.0.3-0
- Autogenerated by Bloom

* Thu May 18 2017 Hasegawa Shun <pazeshun3684@gmail.com> - 3.0.2-0
- Autogenerated by Bloom

* Wed May 17 2017 Hasegawa Shun <pazeshun3684@gmail.com> - 3.0.1-0
- Autogenerated by Bloom

* Mon May 08 2017 Hasegawa Shun <pazeshun3684@gmail.com> - 3.0.0-0
- Autogenerated by Bloom

* Sat Oct 22 2016 Hasegawa Shun <pazeshun3684@gmail.com> - 2.0.0-0
- Autogenerated by Bloom

* Sat Jul 16 2016 Hasegawa Shun <pazeshun3684@gmail.com> - 1.5.1-0
- Autogenerated by Bloom

* Fri Jul 08 2016 Hasegawa Shun <pazeshun3684@gmail.com> - 1.0.0-0
- Autogenerated by Bloom

* Fri Jun 24 2016 Hasegawa Shun <pazeshun3684@gmail.com> - 0.8.1-0
- Autogenerated by Bloom

* Wed Jun 01 2016 pazeshun <pazeshun3684@gmail.com> - 0.8.0-2
- Autogenerated by Bloom

* Fri Apr 15 2016 pazeshun <pazeshun3684@gmail.com> - 0.2.4-0
- Autogenerated by Bloom

* Mon Apr 11 2016 pazeshun <pazeshun3684@gmail.com> - 0.2.3-0
- Autogenerated by Bloom

* Tue Mar 08 2016 pazeshun <pazeshun3684@gmail.com> - 0.2.2-0
- Autogenerated by Bloom

* Tue Mar 08 2016 pazeshun <pazeshun3684@gmail.com> - 0.2.1-0
- Autogenerated by Bloom

* Tue Mar 08 2016 pazeshun <pazeshun3684@gmail.com> - 0.2.0-1
- Autogenerated by Bloom

* Tue Mar 08 2016 pazeshun <pazeshun3684@gmail.com> - 0.2.0-0
- Autogenerated by Bloom

