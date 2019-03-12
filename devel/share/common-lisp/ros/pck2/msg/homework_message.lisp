; Auto-generated. Do not edit!


(cl:in-package pck2-msg)


;//! \htmlinclude homework_message.msg.html

(cl:defclass <homework_message> (roslisp-msg-protocol:ros-message)
  ((content
    :reader content
    :initarg :content
    :type cl:string
    :initform "")
   (number
    :reader number
    :initarg :number
    :type cl:integer
    :initform 0))
)

(cl:defclass homework_message (<homework_message>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <homework_message>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'homework_message)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pck2-msg:<homework_message> is deprecated: use pck2-msg:homework_message instead.")))

(cl:ensure-generic-function 'content-val :lambda-list '(m))
(cl:defmethod content-val ((m <homework_message>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pck2-msg:content-val is deprecated.  Use pck2-msg:content instead.")
  (content m))

(cl:ensure-generic-function 'number-val :lambda-list '(m))
(cl:defmethod number-val ((m <homework_message>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pck2-msg:number-val is deprecated.  Use pck2-msg:number instead.")
  (number m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <homework_message>) ostream)
  "Serializes a message object of type '<homework_message>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'content))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'content))
  (cl:let* ((signed (cl:slot-value msg 'number)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <homework_message>) istream)
  "Deserializes a message object of type '<homework_message>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'content) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'content) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'number) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<homework_message>)))
  "Returns string type for a message object of type '<homework_message>"
  "pck2/homework_message")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'homework_message)))
  "Returns string type for a message object of type 'homework_message"
  "pck2/homework_message")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<homework_message>)))
  "Returns md5sum for a message object of type '<homework_message>"
  "0dd088ad22ee351bec89d6fb19ccdc0d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'homework_message)))
  "Returns md5sum for a message object of type 'homework_message"
  "0dd088ad22ee351bec89d6fb19ccdc0d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<homework_message>)))
  "Returns full string definition for message of type '<homework_message>"
  (cl:format cl:nil "string content~%int32 number~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'homework_message)))
  "Returns full string definition for message of type 'homework_message"
  (cl:format cl:nil "string content~%int32 number~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <homework_message>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'content))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <homework_message>))
  "Converts a ROS message object to a list"
  (cl:list 'homework_message
    (cl:cons ':content (content msg))
    (cl:cons ':number (number msg))
))
