; Auto-generated. Do not edit!


(cl:in-package pck2-srv)


;//! \htmlinclude sum-request.msg.html

(cl:defclass <sum-request> (roslisp-msg-protocol:ros-message)
  ((content
    :reader content
    :initarg :content
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass sum-request (<sum-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <sum-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'sum-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pck2-srv:<sum-request> is deprecated: use pck2-srv:sum-request instead.")))

(cl:ensure-generic-function 'content-val :lambda-list '(m))
(cl:defmethod content-val ((m <sum-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pck2-srv:content-val is deprecated.  Use pck2-srv:content instead.")
  (content m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <sum-request>) ostream)
  "Serializes a message object of type '<sum-request>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'content))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'content))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <sum-request>) istream)
  "Deserializes a message object of type '<sum-request>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'content) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'content)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<sum-request>)))
  "Returns string type for a service object of type '<sum-request>"
  "pck2/sumRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'sum-request)))
  "Returns string type for a service object of type 'sum-request"
  "pck2/sumRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<sum-request>)))
  "Returns md5sum for a message object of type '<sum-request>"
  "eff151ed5a6df648d5c30ca5d71ccbda")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'sum-request)))
  "Returns md5sum for a message object of type 'sum-request"
  "eff151ed5a6df648d5c30ca5d71ccbda")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<sum-request>)))
  "Returns full string definition for message of type '<sum-request>"
  (cl:format cl:nil "int32[] content~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'sum-request)))
  "Returns full string definition for message of type 'sum-request"
  (cl:format cl:nil "int32[] content~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <sum-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'content) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <sum-request>))
  "Converts a ROS message object to a list"
  (cl:list 'sum-request
    (cl:cons ':content (content msg))
))
;//! \htmlinclude sum-response.msg.html

(cl:defclass <sum-response> (roslisp-msg-protocol:ros-message)
  ((comment
    :reader comment
    :initarg :comment
    :type cl:integer
    :initform 0))
)

(cl:defclass sum-response (<sum-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <sum-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'sum-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pck2-srv:<sum-response> is deprecated: use pck2-srv:sum-response instead.")))

(cl:ensure-generic-function 'comment-val :lambda-list '(m))
(cl:defmethod comment-val ((m <sum-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pck2-srv:comment-val is deprecated.  Use pck2-srv:comment instead.")
  (comment m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <sum-response>) ostream)
  "Serializes a message object of type '<sum-response>"
  (cl:let* ((signed (cl:slot-value msg 'comment)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <sum-response>) istream)
  "Deserializes a message object of type '<sum-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'comment) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<sum-response>)))
  "Returns string type for a service object of type '<sum-response>"
  "pck2/sumResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'sum-response)))
  "Returns string type for a service object of type 'sum-response"
  "pck2/sumResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<sum-response>)))
  "Returns md5sum for a message object of type '<sum-response>"
  "eff151ed5a6df648d5c30ca5d71ccbda")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'sum-response)))
  "Returns md5sum for a message object of type 'sum-response"
  "eff151ed5a6df648d5c30ca5d71ccbda")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<sum-response>)))
  "Returns full string definition for message of type '<sum-response>"
  (cl:format cl:nil "int32 comment~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'sum-response)))
  "Returns full string definition for message of type 'sum-response"
  (cl:format cl:nil "int32 comment~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <sum-response>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <sum-response>))
  "Converts a ROS message object to a list"
  (cl:list 'sum-response
    (cl:cons ':comment (comment msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'sum)))
  'sum-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'sum)))
  'sum-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'sum)))
  "Returns string type for a service object of type '<sum>"
  "pck2/sum")