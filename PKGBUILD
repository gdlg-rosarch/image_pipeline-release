# Script generated with Bloom
pkgdesc="ROS - image_pipeline fills the gap between getting raw images from a camera driver and higher-level vision processing."
url='http://www.ros.org/wiki/image_pipeline'

pkgname='ros-kinetic-image-pipeline'
pkgver='1.12.22_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-camera-calibration'
'ros-kinetic-depth-image-proc'
'ros-kinetic-image-proc'
'ros-kinetic-image-publisher'
'ros-kinetic-image-rotate'
'ros-kinetic-image-view'
'ros-kinetic-stereo-image-proc'
)

conflicts=()
replaces=()

_dir=image_pipeline
source=()
md5sums=()

prepare() {
    cp -R $startdir/image_pipeline $srcdir/image_pipeline
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
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

