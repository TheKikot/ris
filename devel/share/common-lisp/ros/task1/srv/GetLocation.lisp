; Auto-generated. Do not edit!


(cl:in-package task1-srv)


;//! \htmlinclude GetLocation-request.msg.html

(cl:defclass <GetLocation-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass GetLocation-request (<GetLocation-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GetLocation-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GetLocation-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name task1-srv:<GetLocation-request> is deprecated: use task1-srv:GetLocation-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GetLocation-request>) ostream)
  "Serializes a message object of type '<GetLocation-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GetLocation-request>) istream)
  "Deserializes a message object of type '<GetLocation-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GetLocation-request>)))
  "Returns string type for a service object of type '<GetLocation-request>"
  "task1/GetLocationRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetLocation-request)))
  "Returns string type for a service object of type 'GetLocation-request"
  "task1/GetLocationRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GetLocation-request>)))
  "Returns md5sum for a message object of type '<GetLocation-request>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GetLocation-request)))
  "Returns md5sum for a message object of type 'GetLocation-request"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GetLocation-request>)))
  "Returns full string definition for message of type '<GetLocation-request>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GetLocation-request)))
  "Returns full string definition for message of type 'GetLocation-request"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GetLocation-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GetLocation-request>))
  "Converts a ROS message object to a list"
  (cl:list 'GetLocation-request
))
;//! \htmlinclude GetLocation-response.msg.html

(cl:defclass <GetLocation-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass GetLocation-response (<GetLocation-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GetLocation-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GetLocation-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name task1-srv:<GetLocation-response> is deprecated: use task1-srv:GetLocation-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GetLocation-response>) ostream)
  "Serializes a message object of type '<GetLocation-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GetLocation-response>) istream)
  "Deserializes a message object of type '<GetLocation-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GetLocation-response>)))
  "Returns string type for a service object of type '<GetLocation-response>"
  "task1/GetLocationResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetLocation-response)))
  "Returns string type for a service object of type 'GetLocation-response"
  "task1/GetLocationResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GetLocation-response>)))
  "Returns md5sum for a message object of type '<GetLocation-response>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GetLocation-response)))
  "Returns md5sum for a message object of type 'GetLocation-response"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GetLocation-response>)))
  "Returns full string definition for message of type '<GetLocation-response>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GetLocation-response)))
  "Returns full string definition for message of type 'GetLocation-response"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GetLocation-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GetLocation-response>))
  "Converts a ROS message object to a list"
  (cl:list 'GetLocation-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'GetLocation)))
  'GetLocation-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'GetLocation)))
  'GetLocation-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetLocation)))
  "Returns string type for a service object of type '<GetLocation>"
  "task1/GetLocation")