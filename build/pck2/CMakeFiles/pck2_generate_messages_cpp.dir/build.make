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

# Utility rule file for pck2_generate_messages_cpp.

# Include the progress variables for this target.
include pck2/CMakeFiles/pck2_generate_messages_cpp.dir/progress.make

pck2/CMakeFiles/pck2_generate_messages_cpp: /home/kikot/ROS/devel/include/pck2/homework_message.h
pck2/CMakeFiles/pck2_generate_messages_cpp: /home/kikot/ROS/devel/include/pck2/sum.h
pck2/CMakeFiles/pck2_generate_messages_cpp: /home/kikot/ROS/devel/include/pck2/movesrv.h


/home/kikot/ROS/devel/include/pck2/homework_message.h: /opt/ros/kinetic/lib/gencpp/gen_cpp.py
/home/kikot/ROS/devel/include/pck2/homework_message.h: /home/kikot/ROS/src/pck2/msg/homework_message.msg
/home/kikot/ROS/devel/include/pck2/homework_message.h: /opt/ros/kinetic/share/gencpp/msg.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/kikot/ROS/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating C++ code from pck2/homework_message.msg"
	cd /home/kikot/ROS/src/pck2 && /home/kikot/ROS/build/catkin_generated/env_cached.sh /usr/bin/python /opt/ros/kinetic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/kikot/ROS/src/pck2/msg/homework_message.msg -Ipck2:/home/kikot/ROS/src/pck2/msg -Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg -p pck2 -o /home/kikot/ROS/devel/include/pck2 -e /opt/ros/kinetic/share/gencpp/cmake/..

/home/kikot/ROS/devel/include/pck2/sum.h: /opt/ros/kinetic/lib/gencpp/gen_cpp.py
/home/kikot/ROS/devel/include/pck2/sum.h: /home/kikot/ROS/src/pck2/srv/sum.srv
/home/kikot/ROS/devel/include/pck2/sum.h: /opt/ros/kinetic/share/gencpp/msg.h.template
/home/kikot/ROS/devel/include/pck2/sum.h: /opt/ros/kinetic/share/gencpp/srv.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/kikot/ROS/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Generating C++ code from pck2/sum.srv"
	cd /home/kikot/ROS/src/pck2 && /home/kikot/ROS/build/catkin_generated/env_cached.sh /usr/bin/python /opt/ros/kinetic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/kikot/ROS/src/pck2/srv/sum.srv -Ipck2:/home/kikot/ROS/src/pck2/msg -Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg -p pck2 -o /home/kikot/ROS/devel/include/pck2 -e /opt/ros/kinetic/share/gencpp/cmake/..

/home/kikot/ROS/devel/include/pck2/movesrv.h: /opt/ros/kinetic/lib/gencpp/gen_cpp.py
/home/kikot/ROS/devel/include/pck2/movesrv.h: /home/kikot/ROS/src/pck2/srv/movesrv.srv
/home/kikot/ROS/devel/include/pck2/movesrv.h: /opt/ros/kinetic/share/gencpp/msg.h.template
/home/kikot/ROS/devel/include/pck2/movesrv.h: /opt/ros/kinetic/share/gencpp/srv.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/kikot/ROS/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Generating C++ code from pck2/movesrv.srv"
	cd /home/kikot/ROS/src/pck2 && /home/kikot/ROS/build/catkin_generated/env_cached.sh /usr/bin/python /opt/ros/kinetic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/kikot/ROS/src/pck2/srv/movesrv.srv -Ipck2:/home/kikot/ROS/src/pck2/msg -Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg -p pck2 -o /home/kikot/ROS/devel/include/pck2 -e /opt/ros/kinetic/share/gencpp/cmake/..

pck2_generate_messages_cpp: pck2/CMakeFiles/pck2_generate_messages_cpp
pck2_generate_messages_cpp: /home/kikot/ROS/devel/include/pck2/homework_message.h
pck2_generate_messages_cpp: /home/kikot/ROS/devel/include/pck2/sum.h
pck2_generate_messages_cpp: /home/kikot/ROS/devel/include/pck2/movesrv.h
pck2_generate_messages_cpp: pck2/CMakeFiles/pck2_generate_messages_cpp.dir/build.make

.PHONY : pck2_generate_messages_cpp

# Rule to build all files generated by this target.
pck2/CMakeFiles/pck2_generate_messages_cpp.dir/build: pck2_generate_messages_cpp

.PHONY : pck2/CMakeFiles/pck2_generate_messages_cpp.dir/build

pck2/CMakeFiles/pck2_generate_messages_cpp.dir/clean:
	cd /home/kikot/ROS/build/pck2 && $(CMAKE_COMMAND) -P CMakeFiles/pck2_generate_messages_cpp.dir/cmake_clean.cmake
.PHONY : pck2/CMakeFiles/pck2_generate_messages_cpp.dir/clean

pck2/CMakeFiles/pck2_generate_messages_cpp.dir/depend:
	cd /home/kikot/ROS/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/kikot/ROS/src /home/kikot/ROS/src/pck2 /home/kikot/ROS/build /home/kikot/ROS/build/pck2 /home/kikot/ROS/build/pck2/CMakeFiles/pck2_generate_messages_cpp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : pck2/CMakeFiles/pck2_generate_messages_cpp.dir/depend
