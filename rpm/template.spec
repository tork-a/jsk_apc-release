Name:           ros-indigo-jsk-apc
Version:        4.1.3
Release:        0%{?dist}
Summary:        ROS jsk_apc package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/jsk_apc
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-jsk-2015-05-baxter-apc
Requires:       ros-indigo-jsk-2016-01-baxter-apc
Requires:       ros-indigo-jsk-apc2015-common
Requires:       ros-indigo-jsk-apc2016-common
Requires:       ros-indigo-jsk-arc2017-baxter
Requires:       ros-indigo-jsk-arc2017-common
BuildRequires:  ros-indigo-catkin

%description
Metapackage for Amazon Picking Challenge

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

* Tue Mar 08 2016 baxter <baxter@jsk.imi.i.u-tokyo.ac.jp> - 0.2.0-1
- Autogenerated by Bloom

* Tue Mar 08 2016 baxter <baxter@jsk.imi.i.u-tokyo.ac.jp> - 0.2.0-0
- Autogenerated by Bloom

