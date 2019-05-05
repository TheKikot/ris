; Auto-generated. Do not edit!


(cl:in-package exercise6-srv)


;//! \htmlinclude GetLocation-request.msg.html

(cl:defclass <GetLocation-request> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0))
)

(cl:defclass GetLocation-request (<GetLocation-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GetLocation-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GetLocation-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name exercise6-srv:<GetLocation-request> is deprecated: use exercise6-srv:GetLocation-request instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <GetLocation-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader exercise6-srv:x-val is deprecated.  Use exercise6-srv:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <GetLocation-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader exercise6-srv:y-val is deprecated.  Use exercise6-srv:y instead.")
  (y m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GetLocation-request>) ostream)
  "Serializes a message object of type '<GetLocation-request>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GetLocation-request>) istream)
  "Deserializes a message object of type '<GetLocation-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GetLocation-request>)))
  "Returns string type for a service object of type '<GetLocation-request>"
  "exercise6/GetLocationRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetLocation-request)))
  "Returns string type for a service object of type 'GetLocation-request"
  "exercise6/GetLocationRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GetLocation-request>)))
  "Returns md5sum for a message object of type '<GetLocation-request>"
  "ff8d7d66dd3e4b731ef14a45d38888b6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GetLocation-request)))
  "Returns md5sum for a message object of type 'GetLocation-request"
  "ff8d7d66dd3e4b731ef14a45d38888b6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GetLocation-request>)))
  "Returns full string definition for message of type '<GetLocation-request>"
  (cl:format cl:nil "float32 x~%float32 y~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GetLocation-request)))
  "Returns full string definition for message of type 'GetLocation-request"
  (cl:format cl:nil "float32 x~%float32 y~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GetLocation-request>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GetLocation-request>))
  "Converts a ROS message object to a list"
  (cl:list 'GetLocation-request
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
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
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name exercise6-srv:<GetLocation-response> is deprecated: use exercise6-srv:GetLocation-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GetLocation-response>) ostream)
  "Serializes a message object of type '<GetLocation-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GetLocation-response>) istream)
  "Deserializes a message object of type '<GetLocation-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GetLocation-response>)))
  "Returns string type for a service object of type '<GetLocation-response>"
  "exercise6/GetLocationResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetLocation-response)))
  "Returns string type for a service object of type 'GetLocation-response"
  "exercise6/GetLocationResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GetLocation-response>)))
  "Returns md5sum for a message object of type '<GetLocation-response>"
  "ff8d7d66dd3e4b731ef14a45d38888b6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GetLocation-response)))
  "Returns md5sum for a message object of type 'GetLocation-response"
  "ff8d7d66dd3e4b731ef14a45d38888b6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GetLocation-response>)))
  "Returns full string definition for message of type '<GetLocation-response>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GetLocation-response)))
  "Returns full string definition for message of type 'GetLocation-response"
  (cl:format cl:nil "~%~%"))
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
  "exercise6/GetLocation")