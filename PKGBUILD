# Script generated with Bloom
pkgdesc="ROS - camera_calibration allows easy calibration of monocular or stereo cameras using a checkerboard calibration target."
url='http://www.ros.org/wiki/camera_calibration'

pkgname='ros-lunar-camera-calibration'
pkgver='1.12.21_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin>=0.5.68'
'ros-lunar-rostest'
)

depends=('ros-lunar-cv-bridge'
'ros-lunar-image-geometry'
'ros-lunar-message-filters'
'ros-lunar-rospy'
'ros-lunar-sensor-msgs'
'ros-lunar-std-srvs'
)

conflicts=()
replaces=()

_dir=camera_calibration
source=()
md5sums=()

prepare() {
    cp -R $startdir/camera_calibration $srcdir/camera_calibration
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

