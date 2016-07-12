Name:           ros-indigo-stereo-image-proc
Version:        1.12.18
Release:        0%{?dist}
Summary:        ROS stereo_image_proc package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/stereo_image_proc
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-image-geometry
Requires:       ros-indigo-image-proc
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-message-filters
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-stereo-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-image-geometry
BuildRequires:  ros-indigo-image-proc
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-message-filters
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-stereo-msgs

%description
Stereo and single image rectification and disparity processing.

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
* Tue Jul 12 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.18-0
- Autogenerated by Bloom

* Mon Jul 11 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.17-0
- Autogenerated by Bloom

* Sat Mar 19 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.16-0
- Autogenerated by Bloom

* Sun Jan 17 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.15-0
- Autogenerated by Bloom

* Wed Jul 22 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.14-0
- Autogenerated by Bloom

* Mon Apr 06 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.13-0
- Autogenerated by Bloom

* Wed Dec 31 2014 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.12-0
- Autogenerated by Bloom

