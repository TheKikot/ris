# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "pck2: 1 messages, 2 services")

set(MSG_I_FLAGS "-Ipck2:/home/kikot/ROS/src/pck2/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(pck2_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/kikot/ROS/src/pck2/srv/sum.srv" NAME_WE)
add_custom_target(_pck2_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "pck2" "/home/kikot/ROS/src/pck2/srv/sum.srv" ""
)

get_filename_component(_filename "/home/kikot/ROS/src/pck2/msg/homework_message.msg" NAME_WE)
add_custom_target(_pck2_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "pck2" "/home/kikot/ROS/src/pck2/msg/homework_message.msg" ""
)

get_filename_component(_filename "/home/kikot/ROS/src/pck2/srv/movesrv.srv" NAME_WE)
add_custom_target(_pck2_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "pck2" "/home/kikot/ROS/src/pck2/srv/movesrv.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(pck2
  "/home/kikot/ROS/src/pck2/msg/homework_message.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pck2
)

### Generating Services
_generate_srv_cpp(pck2
  "/home/kikot/ROS/src/pck2/srv/sum.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pck2
)
_generate_srv_cpp(pck2
  "/home/kikot/ROS/src/pck2/srv/movesrv.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pck2
)

### Generating Module File
_generate_module_cpp(pck2
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pck2
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(pck2_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(pck2_generate_messages pck2_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/kikot/ROS/src/pck2/srv/sum.srv" NAME_WE)
add_dependencies(pck2_generate_messages_cpp _pck2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kikot/ROS/src/pck2/msg/homework_message.msg" NAME_WE)
add_dependencies(pck2_generate_messages_cpp _pck2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kikot/ROS/src/pck2/srv/movesrv.srv" NAME_WE)
add_dependencies(pck2_generate_messages_cpp _pck2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pck2_gencpp)
add_dependencies(pck2_gencpp pck2_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pck2_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(pck2
  "/home/kikot/ROS/src/pck2/msg/homework_message.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pck2
)

### Generating Services
_generate_srv_eus(pck2
  "/home/kikot/ROS/src/pck2/srv/sum.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pck2
)
_generate_srv_eus(pck2
  "/home/kikot/ROS/src/pck2/srv/movesrv.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pck2
)

### Generating Module File
_generate_module_eus(pck2
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pck2
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(pck2_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(pck2_generate_messages pck2_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/kikot/ROS/src/pck2/srv/sum.srv" NAME_WE)
add_dependencies(pck2_generate_messages_eus _pck2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kikot/ROS/src/pck2/msg/homework_message.msg" NAME_WE)
add_dependencies(pck2_generate_messages_eus _pck2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kikot/ROS/src/pck2/srv/movesrv.srv" NAME_WE)
add_dependencies(pck2_generate_messages_eus _pck2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pck2_geneus)
add_dependencies(pck2_geneus pck2_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pck2_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(pck2
  "/home/kikot/ROS/src/pck2/msg/homework_message.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pck2
)

### Generating Services
_generate_srv_lisp(pck2
  "/home/kikot/ROS/src/pck2/srv/sum.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pck2
)
_generate_srv_lisp(pck2
  "/home/kikot/ROS/src/pck2/srv/movesrv.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pck2
)

### Generating Module File
_generate_module_lisp(pck2
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pck2
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(pck2_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(pck2_generate_messages pck2_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/kikot/ROS/src/pck2/srv/sum.srv" NAME_WE)
add_dependencies(pck2_generate_messages_lisp _pck2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kikot/ROS/src/pck2/msg/homework_message.msg" NAME_WE)
add_dependencies(pck2_generate_messages_lisp _pck2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kikot/ROS/src/pck2/srv/movesrv.srv" NAME_WE)
add_dependencies(pck2_generate_messages_lisp _pck2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pck2_genlisp)
add_dependencies(pck2_genlisp pck2_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pck2_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(pck2
  "/home/kikot/ROS/src/pck2/msg/homework_message.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pck2
)

### Generating Services
_generate_srv_nodejs(pck2
  "/home/kikot/ROS/src/pck2/srv/sum.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pck2
)
_generate_srv_nodejs(pck2
  "/home/kikot/ROS/src/pck2/srv/movesrv.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pck2
)

### Generating Module File
_generate_module_nodejs(pck2
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pck2
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(pck2_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(pck2_generate_messages pck2_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/kikot/ROS/src/pck2/srv/sum.srv" NAME_WE)
add_dependencies(pck2_generate_messages_nodejs _pck2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kikot/ROS/src/pck2/msg/homework_message.msg" NAME_WE)
add_dependencies(pck2_generate_messages_nodejs _pck2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kikot/ROS/src/pck2/srv/movesrv.srv" NAME_WE)
add_dependencies(pck2_generate_messages_nodejs _pck2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pck2_gennodejs)
add_dependencies(pck2_gennodejs pck2_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pck2_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(pck2
  "/home/kikot/ROS/src/pck2/msg/homework_message.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pck2
)

### Generating Services
_generate_srv_py(pck2
  "/home/kikot/ROS/src/pck2/srv/sum.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pck2
)
_generate_srv_py(pck2
  "/home/kikot/ROS/src/pck2/srv/movesrv.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pck2
)

### Generating Module File
_generate_module_py(pck2
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pck2
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(pck2_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(pck2_generate_messages pck2_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/kikot/ROS/src/pck2/srv/sum.srv" NAME_WE)
add_dependencies(pck2_generate_messages_py _pck2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kikot/ROS/src/pck2/msg/homework_message.msg" NAME_WE)
add_dependencies(pck2_generate_messages_py _pck2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kikot/ROS/src/pck2/srv/movesrv.srv" NAME_WE)
add_dependencies(pck2_generate_messages_py _pck2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pck2_genpy)
add_dependencies(pck2_genpy pck2_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pck2_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pck2)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pck2
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(pck2_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pck2)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pck2
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(pck2_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pck2)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pck2
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(pck2_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pck2)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pck2
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(pck2_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pck2)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pck2\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pck2
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(pck2_generate_messages_py std_msgs_generate_messages_py)
endif()
