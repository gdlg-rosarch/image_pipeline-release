Name:           ros-kinetic-image-view
Version:        1.12.16
Release:        0%{?dist}
Summary:        ROS image_view package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/image_view
Source0:        %{name}-%{version}.tar.gz

Requires:       gtk2-devel
Requires:       opencv-python
Requires:       ros-kinetic-camera-calibration-parsers
Requires:       ros-kinetic-cv-bridge
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-image-transport
Requires:       ros-kinetic-message-filters
Requires:       ros-kinetic-nodelet
Requires:       ros-kinetic-rosconsole
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-std-srvs
BuildRequires:  gtk2-devel
BuildRequires:  ros-kinetic-camera-calibration-parsers
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cv-bridge >= 1.11.10
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-image-transport
BuildRequires:  ros-kinetic-message-filters
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-nodelet
BuildRequires:  ros-kinetic-rosconsole
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-srvs
BuildRequires:  ros-kinetic-stereo-msgs

%description
A simple viewer for ROS image topics. Includes a specialized viewer for stereo +
disparity images.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Apr 07 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.16-0
- Autogenerated by Bloom

