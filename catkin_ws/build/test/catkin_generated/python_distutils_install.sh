#!/bin/sh -x

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

cd "/Users/Saren/Documents/Uni/306/SpeedKiwi/catkin_ws/src/test"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
/usr/bin/env \
    PYTHONPATH="/Users/Saren/Documents/Uni/306/SpeedKiwi/catkin_ws/install/lib/python2.7/site-packages:/Users/Saren/Documents/Uni/306/SpeedKiwi/catkin_ws/build/lib/python2.7/site-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/Users/Saren/Documents/Uni/306/SpeedKiwi/catkin_ws/build" \
    "/usr/bin/python" \
    "/Users/Saren/Documents/Uni/306/SpeedKiwi/catkin_ws/src/test/setup.py" \
    build --build-base "/Users/Saren/Documents/Uni/306/SpeedKiwi/catkin_ws/build/test" \
    install \
    $DESTDIR_ARG \
     --prefix="/Users/Saren/Documents/Uni/306/SpeedKiwi/catkin_ws/install" --install-scripts="/Users/Saren/Documents/Uni/306/SpeedKiwi/catkin_ws/install/bin"
