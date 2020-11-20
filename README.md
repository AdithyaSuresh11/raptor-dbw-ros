# `NEW EAGLE ROS DRIVER FOR SCHAEFFLER PARAVAN AND AUTONOMOUSTUFF DEMONSTRATION`

This driver was forked and modified by Adithya Suresh (Perception System engineer) of Clemson University's Deep Orange 12 - Autonomous Systems team from the New Eagle ROS1 driver developed by the [New Eagle group](https://github.com/NewEagleRaptor/raptor-dbw-ros). This folder contains a collection of ROS packages, which allow DBW kit developers to quickly implement a generic ROS node for interacting with New Eagle Raptor controller. The Joystick node in the package associates Xbox One joystick controller's commands and associates with steering, brake and supervisor input commands for the startup and shutdown sequence of Spacedrive system. 

The New Eagle node subscribes to the Waypoint Controller developed by Manikanda Balaji Venkatesan (Team Lead and Waypoint control engineer) and Abhishek Bhagwat (Waypoint Control engineer) and sends the steering value from the MATLAB-Simulink model (Waypoint controller) in CAN bus to the New Eagle raptor controller which in turn is passed to the spacedrive system for actuation. The Joystick node is used for input commands for startup and shutdown, safe stop by braking and steering for transportation when the Waypoint controller is not used.

The current development branch is `AdithyaSuresh_SP_dev` and targets ROS `kinetic` and `melodic`.

## Dependency

The New Eagle ROS driver works with [Kvaser interface](https://github.com/astuff/kvaser_interface) developed by the [AutonomouStuff](https://autonomoustuff.com/). Certain packages are needed to be installed to ensure the CAN transmission and reception is working in the computer system. To build and install the necessary packages:

* Download [Kvaser linux drivers and SDK](https://www.kvaser.com/download/)
* `cd /usr/src`
* `sudo mv ~/Downloads/linuxcan.tar.gz .`
* `sudo tar xvf linuxcan.tar.gz`
* `cd linuxcan`
* `sudo make`
* `sudo make install`
* `sudo apt install ros-[distro_version]-can-msgs` (distro - kinetic or melodic)
* `sudo apt-add-repository ppa:astuff/kvaser-linux`
* `sudo apt-get update`
* `sudo apt-get install kvaser-canlib-dev kvaser-drivers-dkms`

Disclaimer: Kvaser Driver is needed for the New Eagle driver to work. 

Doing the above task will blacklist the SocketCan driver which is built-in the user's computer. If the user does not want to have Kvaser driver and wants to remove the blacklist problem, then use:

* `cd /usr/src/linuxcan`
* `sudo make`
* `sudo make uninstall`

Once the drivers are installed, the user can verify the Kvaser channel which is connected to their computer/laptop by:

* `cd /usr/doc/canlib/examples`
* `./listChannels`

## Installing and building

The user can build them from source using a catkin workspace and following these steps:
* Create and initialize a new catkin workspace if you don't already have one. Instructions below assume the workspace was created in catkin_ws.
* `cd catkin_ws/src`
* `git clone https://github.com/cuicardeeporange/raptor-dbw-ros.git` (AdithyaSP_dev_branch)
* `cd ..`
* `catkin_make`

## Usage

* `roscore`
* `roslaunch raptor_dbw_can dbw_sp.launch`

For running the Joystick node: (Assuming the user has Xbox One controller)
* `roslaunch raptor_dbw_joystick_demo joystick_demo_sp.launch`

## Contributors
* Manikanda Balaji Venkatesan (Waypoint controller)
* Abhishek Bhagwat (Waypoint controller)
