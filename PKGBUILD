# Script generated with Bloom
pkgdesc="ROS - <p> Contains a node that rotates an image stream in a way that minimizes the angle between a vector in some arbitrary frame and a vector in the camera frame. The frame of the outgoing image is published by the node. </p> <p> This node is intended to allow camera images to be visualized in an orientation that is more intuitive than the hardware-constrained orientation of the physical camera. This is particularly helpful, for example, to show images from the PR2's forearm cameras with a consistent up direction, despite the fact that the forearms need to rotate in arbitrary ways during manipulation. </p> <p> It is not recommended to use the output from this node for further computation, as it interpolates the source image, introduces black borders, and does not output a camera_info. </p>"
url='http://ros.org/wiki/image_rotate'

pkgname='ros-kinetic-image-rotate'
pkgver='1.12.22_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-cmake-modules'
'ros-kinetic-cv-bridge'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-geometry-msgs'
'ros-kinetic-image-transport'
'ros-kinetic-nodelet'
'ros-kinetic-roscpp'
'ros-kinetic-rostest'
'ros-kinetic-tf2'
'ros-kinetic-tf2-geometry-msgs'
'ros-kinetic-tf2-ros'
)

depends=('ros-kinetic-cv-bridge'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-image-transport'
'ros-kinetic-nodelet'
'ros-kinetic-roscpp'
'ros-kinetic-tf2'
'ros-kinetic-tf2-geometry-msgs'
'ros-kinetic-tf2-ros'
)

conflicts=()
replaces=()

_dir=image_rotate
source=()
md5sums=()

prepare() {
    cp -R $startdir/image_rotate $srcdir/image_rotate
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

