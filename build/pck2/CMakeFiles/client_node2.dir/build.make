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

# Include any dependencies generated for this target.
include pck2/CMakeFiles/client_node2.dir/depend.make

# Include the progress variables for this target.
include pck2/CMakeFiles/client_node2.dir/progress.make

# Include the compile flags for this target's objects.
include pck2/CMakeFiles/client_node2.dir/flags.make

pck2/CMakeFiles/client_node2.dir/src/client_node.cpp.o: pck2/CMakeFiles/client_node2.dir/flags.make
pck2/CMakeFiles/client_node2.dir/src/client_node.cpp.o: /home/kikot/ROS/src/pck2/src/client_node.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kikot/ROS/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object pck2/CMakeFiles/client_node2.dir/src/client_node.cpp.o"
	cd /home/kikot/ROS/build/pck2 && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/client_node2.dir/src/client_node.cpp.o -c /home/kikot/ROS/src/pck2/src/client_node.cpp

pck2/CMakeFiles/client_node2.dir/src/client_node.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/client_node2.dir/src/client_node.cpp.i"
	cd /home/kikot/ROS/build/pck2 && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kikot/ROS/src/pck2/src/client_node.cpp > CMakeFiles/client_node2.dir/src/client_node.cpp.i

pck2/CMakeFiles/client_node2.dir/src/client_node.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/client_node2.dir/src/client_node.cpp.s"
	cd /home/kikot/ROS/build/pck2 && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kikot/ROS/src/pck2/src/client_node.cpp -o CMakeFiles/client_node2.dir/src/client_node.cpp.s

pck2/CMakeFiles/client_node2.dir/src/client_node.cpp.o.requires:

.PHONY : pck2/CMakeFiles/client_node2.dir/src/client_node.cpp.o.requires

pck2/CMakeFiles/client_node2.dir/src/client_node.cpp.o.provides: pck2/CMakeFiles/client_node2.dir/src/client_node.cpp.o.requires
	$(MAKE) -f pck2/CMakeFiles/client_node2.dir/build.make pck2/CMakeFiles/client_node2.dir/src/client_node.cpp.o.provides.build
.PHONY : pck2/CMakeFiles/client_node2.dir/src/client_node.cpp.o.provides

pck2/CMakeFiles/client_node2.dir/src/client_node.cpp.o.provides.build: pck2/CMakeFiles/client_node2.dir/src/client_node.cpp.o


# Object files for target client_node2
client_node2_OBJECTS = \
"CMakeFiles/client_node2.dir/src/client_node.cpp.o"

# External object files for target client_node2
client_node2_EXTERNAL_OBJECTS =

/home/kikot/ROS/devel/lib/pck2/client_node2: pck2/CMakeFiles/client_node2.dir/src/client_node.cpp.o
/home/kikot/ROS/devel/lib/pck2/client_node2: pck2/CMakeFiles/client_node2.dir/build.make
/home/kikot/ROS/devel/lib/pck2/client_node2: /opt/ros/kinetic/lib/libroscpp.so
/home/kikot/ROS/devel/lib/pck2/client_node2: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
/home/kikot/ROS/devel/lib/pck2/client_node2: /usr/lib/x86_64-linux-gnu/libboost_signals.so
/home/kikot/ROS/devel/lib/pck2/client_node2: /opt/ros/kinetic/lib/librosconsole.so
/home/kikot/ROS/devel/lib/pck2/client_node2: /opt/ros/kinetic/lib/librosconsole_log4cxx.so
/home/kikot/ROS/devel/lib/pck2/client_node2: /opt/ros/kinetic/lib/librosconsole_backend_interface.so
/home/kikot/ROS/devel/lib/pck2/client_node2: /usr/lib/x86_64-linux-gnu/liblog4cxx.so
/home/kikot/ROS/devel/lib/pck2/client_node2: /usr/lib/x86_64-linux-gnu/libboost_regex.so
/home/kikot/ROS/devel/lib/pck2/client_node2: /opt/ros/kinetic/lib/libxmlrpcpp.so
/home/kikot/ROS/devel/lib/pck2/client_node2: /opt/ros/kinetic/lib/libroscpp_serialization.so
/home/kikot/ROS/devel/lib/pck2/client_node2: /opt/ros/kinetic/lib/librostime.so
/home/kikot/ROS/devel/lib/pck2/client_node2: /opt/ros/kinetic/lib/libcpp_common.so
/home/kikot/ROS/devel/lib/pck2/client_node2: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/kikot/ROS/devel/lib/pck2/client_node2: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/kikot/ROS/devel/lib/pck2/client_node2: /usr/lib/x86_64-linux-gnu/libboost_chrono.so
/home/kikot/ROS/devel/lib/pck2/client_node2: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/kikot/ROS/devel/lib/pck2/client_node2: /usr/lib/x86_64-linux-gnu/libboost_atomic.so
/home/kikot/ROS/devel/lib/pck2/client_node2: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/kikot/ROS/devel/lib/pck2/client_node2: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so
/home/kikot/ROS/devel/lib/pck2/client_node2: pck2/CMakeFiles/client_node2.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/kikot/ROS/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/kikot/ROS/devel/lib/pck2/client_node2"
	cd /home/kikot/ROS/build/pck2 && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/client_node2.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
pck2/CMakeFiles/client_node2.dir/build: /home/kikot/ROS/devel/lib/pck2/client_node2

.PHONY : pck2/CMakeFiles/client_node2.dir/build

pck2/CMakeFiles/client_node2.dir/requires: pck2/CMakeFiles/client_node2.dir/src/client_node.cpp.o.requires

.PHONY : pck2/CMakeFiles/client_node2.dir/requires

pck2/CMakeFiles/client_node2.dir/clean:
	cd /home/kikot/ROS/build/pck2 && $(CMAKE_COMMAND) -P CMakeFiles/client_node2.dir/cmake_clean.cmake
.PHONY : pck2/CMakeFiles/client_node2.dir/clean

pck2/CMakeFiles/client_node2.dir/depend:
	cd /home/kikot/ROS/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/kikot/ROS/src /home/kikot/ROS/src/pck2 /home/kikot/ROS/build /home/kikot/ROS/build/pck2 /home/kikot/ROS/build/pck2/CMakeFiles/client_node2.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : pck2/CMakeFiles/client_node2.dir/depend
