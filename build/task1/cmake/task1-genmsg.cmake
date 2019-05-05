# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "task1: 0 messages, 1 services")

set(MSG_I_FLAGS "-Imove_base_msgs:/opt/ros/kinetic/share/move_base_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(task1_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/kikot/ROS/src/task1/srv/GetLocation.srv" NAME_WE)
add_custom_target(_task1_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "task1" "/home/kikot/ROS/src/task1/srv/GetLocation.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(task1
  "/home/kikot/ROS/src/task1/srv/GetLocation.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/task1
)

### Generating Module File
_generate_module_cpp(task1
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/task1
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(task1_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(task1_generate_messages task1_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/kikot/ROS/src/task1/srv/GetLocation.srv" NAME_WE)
add_dependencies(task1_generate_messages_cpp _task1_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(task1_gencpp)
add_dependencies(task1_gencpp task1_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS task1_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(task1
  "/home/kikot/ROS/src/task1/srv/GetLocation.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/task1
)

### Generating Module File
_generate_module_eus(task1
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/task1
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(task1_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(task1_generate_messages task1_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/kikot/ROS/src/task1/srv/GetLocation.srv" NAME_WE)
add_dependencies(task1_generate_messages_eus _task1_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(task1_geneus)
add_dependencies(task1_geneus task1_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS task1_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(task1
  "/home/kikot/ROS/src/task1/srv/GetLocation.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/task1
)

### Generating Module File
_generate_module_lisp(task1
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/task1
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(task1_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(task1_generate_messages task1_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/kikot/ROS/src/task1/srv/GetLocation.srv" NAME_WE)
add_dependencies(task1_generate_messages_lisp _task1_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(task1_genlisp)
add_dependencies(task1_genlisp task1_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS task1_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(task1
  "/home/kikot/ROS/src/task1/srv/GetLocation.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/task1
)

### Generating Module File
_generate_module_nodejs(task1
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/task1
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(task1_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(task1_generate_messages task1_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/kikot/ROS/src/task1/srv/GetLocation.srv" NAME_WE)
add_dependencies(task1_generate_messages_nodejs _task1_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(task1_gennodejs)
add_dependencies(task1_gennodejs task1_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS task1_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(task1
  "/home/kikot/ROS/src/task1/srv/GetLocation.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/task1
)

### Generating Module File
_generate_module_py(task1
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/task1
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(task1_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(task1_generate_messages task1_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/kikot/ROS/src/task1/srv/GetLocation.srv" NAME_WE)
add_dependencies(task1_generate_messages_py _task1_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(task1_genpy)
add_dependencies(task1_genpy task1_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS task1_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/task1)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/task1
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET move_base_msgs_generate_messages_cpp)
  add_dependencies(task1_generate_messages_cpp move_base_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/task1)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/task1
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET move_base_msgs_generate_messages_eus)
  add_dependencies(task1_generate_messages_eus move_base_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/task1)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/task1
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET move_base_msgs_generate_messages_lisp)
  add_dependencies(task1_generate_messages_lisp move_base_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/task1)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/task1
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET move_base_msgs_generate_messages_nodejs)
  add_dependencies(task1_generate_messages_nodejs move_base_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/task1)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/task1\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/task1
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET move_base_msgs_generate_messages_py)
  add_dependencies(task1_generate_messages_py move_base_msgs_generate_messages_py)
endif()
