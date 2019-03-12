; Auto-generated. Do not edit!


(cl:in-package pck2-srv)


;//! \htmlinclude movesrv-request.msg.html

(cl:defclass <movesrv-request> (roslisp-msg-protocol:ros-message)
  ((shape
    :reader shape
    :initarg :shape
    :type cl:string
    :initform "")
   (time
    :reader time
    :initarg :time
    :type cl:integer
    :initform 0))
)

(cl:defclass movesrv-request (<movesrv-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <movesrv-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'movesrv-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pck2-srv:<movesrv-request> is deprecated: use pck2-srv:movesrv-request instead.")))

(cl:ensure-generic-function 'shape-val :lambda-list '(m))
(cl:defmethod shape-val ((m <movesrv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pck2-srv:shape-val is deprecated.  Use pck2-srv:shape instead.")
  (shape m))

(cl:ensure-generic-function 'time-val :lambda-list '(m))
(cl:defmethod time-val ((m <movesrv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pck2-srv:time-val is deprecated.  Use pck2-srv:time instead.")
  (time m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <movesrv-request>) ostream)
  "Serializes a message object of type '<movesrv-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'shape))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'shape))
  (cl:let* ((signed (cl:slot-value msg 'time)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <movesrv-request>) istream)
  "Deserializes a message object of type '<movesrv-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'shape) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'shape) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'time) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<movesrv-request>)))
  "Returns string type for a service object of type '<movesrv-request>"
  "pck2/movesrvRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'movesrv-request)))
  "Returns string type for a service object of type 'movesrv-request"
  "pck2/movesrvRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<movesrv-request>)))
  "Returns md5sum for a message object of type '<movesrv-request>"
  "a076d4040c3b13d43930b340985ffc25")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'movesrv-request)))
  "Returns md5sum for a message object of type 'movesrv-request"
  "a076d4040c3b13d43930b340985ffc25")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<movesrv-request>)))
  "Returns full string definition for message of type '<movesrv-request>"
  (cl:format cl:nil "string shape~%int32 time~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'movesrv-request)))
  "Returns full string definition for message of type 'movesrv-request"
  (cl:format cl:nil "string shape~%int32 time~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <movesrv-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'shape))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <movesrv-request>))
  "Converts a ROS message object to a list"
  (cl:list 'movesrv-request
    (cl:cons ':shape (shape msg))
    (cl:cons ':time (time msg))
))
;//! \htmlinclude movesrv-response.msg.html

(cl:defclass <movesrv-response> (roslisp-msg-protocol:ros-message)
  ((return
    :reader return
    :initarg :return
    :type cl:string
    :initform ""))
)

(cl:defclass movesrv-response (<movesrv-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <movesrv-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'movesrv-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pck2-srv:<movesrv-response> is deprecated: use pck2-srv:movesrv-response instead.")))

(cl:ensure-generic-function 'return-val :lambda-list '(m))
(cl:defmethod return-val ((m <movesrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pck2-srv:return-val is deprecated.  Use pck2-srv:return instead.")
  (return m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <movesrv-response>) ostream)
  "Serializes a message object of type '<movesrv-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'return))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'return))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <movesrv-response>) istream)
  "Deserializes a message object of type '<movesrv-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'return) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'return) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<movesrv-response>)))
  "Returns string type for a service object of type '<movesrv-response>"
  "pck2/movesrvResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'movesrv-response)))
  "Returns string type for a service object of type 'movesrv-response"
  "pck2/movesrvResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<movesrv-response>)))
  "Returns md5sum for a message object of type '<movesrv-response>"
  "a076d4040c3b13d43930b340985ffc25")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'movesrv-response)))
  "Returns md5sum for a message object of type 'movesrv-response"
  "a076d4040c3b13d43930b340985ffc25")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<movesrv-response>)))
  "Returns full string definition for message of type '<movesrv-response>"
  (cl:format cl:nil "string return~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'movesrv-response)))
  "Returns full string definition for message of type 'movesrv-response"
  (cl:format cl:nil "string return~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <movesrv-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'return))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <movesrv-response>))
  "Converts a ROS message object to a list"
  (cl:list 'movesrv-response
    (cl:cons ':return (return msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'movesrv)))
  'movesrv-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'movesrv)))
  'movesrv-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'movesrv)))
  "Returns string type for a service object of type '<movesrv>"
  "pck2/movesrv")