# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/kikot/ROS/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/kikot/ROS/build

# Utility rule file for exercise6_generate_messages_py.

# Include the progress variables for this target.
include exercise6/CMakeFiles/exercise6_generate_messages_py.dir/progress.make

exercise6/CMakeFiles/exercise6_generate_messages_py: /home/kikot/ROS/devel/lib/python2.7/dist-packages/exercise6/msg/_RingLocation.py
exercise6/CMakeFiles/exercise6_generate_messages_py: /home/kikot/ROS/devel/lib/python2.7/dist-packages/exercise6/msg/__init__.py
exercise6/CMakeFiles/exercise6_generate_messages_py: /home/kikot/ROS/devel/lib/python2.7/dist-packages/exercise6/srv/__init__.py


/home/kikot/ROS/devel/lib/python2.7/dist-packages/exercise6/msg/_RingLocation.py: /opt/ros/kinetic/lib/genpy/genmsg_py.py
/home/kikot/ROS/devel/lib/python2.7/dist-packages/exercise6/msg/_RingLocation.py: /home/kikot/ROS/src/exercise6/msg/RingLocation.msg
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/kikot/ROS/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating Python from MSG exercise6/RingLocation"
	cd /home/kikot/ROS/build/exercise6 && ../catkin_generated/env_cached.sh /usr/bin/python /opt/ros/kinetic/share/genpy/cmake/../../../lib/genpy/genmsg_py.py /home/kikot/ROS/src/exercise6/msg/RingLocation.msg -Iexercise6:/home/kikot/ROS/src/exercise6/msg -Imove_base_msgs:/opt/ros/kinetic/share/move_base_msgs/cmake/../msg -Iactionlib_msgs:/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg -Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg -Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg -p exercise6 -o /home/kikot/ROS/devel/lib/python2.7/dist-packages/exercise6/msg

/home/kikot/ROS/devel/lib/python2.7/dist-packages/exercise6/msg/__init__.py: /opt/ros/kinetic/lib/genpy/genmsg_py.py
/home/kikot/ROS/devel/lib/python2.7/dist-packages/exercise6/msg/__init__.py: /home/kikot/ROS/devel/lib/python2.7/dist-packages/exercise6/msg/_RingLocation.py
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/kikot/ROS/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Generating Python msg __init__.py for exercise6"
	cd /home/kikot/ROS/build/exercise6 && ../catkin_generated/env_cached.sh /usr/bin/python /opt/ros/kinetic/share/genpy/cmake/../../../lib/genpy/genmsg_py.py -o /home/kikot/ROS/devel/lib/python2.7/dist-packages/exercise6/msg --initpy

/home/kikot/ROS/devel/lib/python2.7/dist-packages/exercise6/srv/__init__.py: /opt/ros/kinetic/lib/genpy/genmsg_py.py
/home/kikot/ROS/devel/lib/python2.7/dist-packages/exercise6/srv/__init__.py: /home/kikot/ROS/devel/lib/python2.7/dist-packages/exercise6/msg/_RingLocation.py
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/kikot/ROS/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Generating Python srv __init__.py for exercise6"
	cd /home/kikot/ROS/build/exercise6 && ../catkin_generated/env_cached.sh /usr/bin/python /opt/ros/kinetic/share/genpy/cmake/../../../lib/genpy/genmsg_py.py -o /home/kikot/ROS/devel/lib/python2.7/dist-packages/exercise6/srv --initpy

exercise6_generate_messages_py: exercise6/CMakeFiles/exercise6_generate_messages_py
exercise6_generate_messages_py: /home/kikot/ROS/devel/lib/python2.7/dist-packages/exercise6/msg/_RingLocation.py
exercise6_generate_messages_py: /home/kikot/ROS/devel/lib/python2.7/dist-packages/exercise6/msg/__init__.py
exercise6_generate_messages_py: /home/kikot/ROS/devel/lib/python2.7/dist-packages/exercise6/srv/__init__.py
exercise6_generate_messages_py: exercise6/CMakeFiles/exercise6_generate_messages_py.dir/build.make

.PHONY : exercise6_generate_messages_py

# Rule to build all files generated by this target.
exercise6/CMakeFiles/exercise6_generate_messages_py.dir/build: exercise6_generate_messages_py

.PHONY : exercise6/CMakeFiles/exercise6_generate_messages_py.dir/build

exercise6/CMakeFiles/exercise6_generate_messages_py.dir/clean:
	cd /home/kikot/ROS/build/exercise6 && $(CMAKE_COMMAND) -P CMakeFiles/exercise6_generate_messages_py.dir/cmake_clean.cmake
.PHONY : exercise6/CMakeFiles/exercise6_generate_messages_py.dir/clean

exercise6/CMakeFiles/exercise6_generate_messages_py.dir/depend:
	cd /home/kikot/ROS/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/kikot/ROS/src /home/kikot/ROS/src/exercise6 /home/kikot/ROS/build /home/kikot/ROS/build/exercise6 /home/kikot/ROS/build/exercise6/CMakeFiles/exercise6_generate_messages_py.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : exercise6/CMakeFiles/exercise6_generate_messages_py.dir/depend

