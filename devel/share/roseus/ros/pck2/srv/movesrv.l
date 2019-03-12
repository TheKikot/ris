;; Auto-generated. Do not edit!


(when (boundp 'pck2::movesrv)
  (if (not (find-package "PCK2"))
    (make-package "PCK2"))
  (shadow 'movesrv (find-package "PCK2")))
(unless (find-package "PCK2::MOVESRV")
  (make-package "PCK2::MOVESRV"))
(unless (find-package "PCK2::MOVESRVREQUEST")
  (make-package "PCK2::MOVESRVREQUEST"))
(unless (find-package "PCK2::MOVESRVRESPONSE")
  (make-package "PCK2::MOVESRVRESPONSE"))

(in-package "ROS")





(defclass pck2::movesrvRequest
  :super ros::object
  :slots (_shape _time ))

(defmethod pck2::movesrvRequest
  (:init
   (&key
    ((:shape __shape) "")
    ((:time __time) 0)
    )
   (send-super :init)
   (setq _shape (string __shape))
   (setq _time (round __time))
   self)
  (:shape
   (&optional __shape)
   (if __shape (setq _shape __shape)) _shape)
  (:time
   (&optional __time)
   (if __time (setq _time __time)) _time)
  (:serialization-length
   ()
   (+
    ;; string _shape
    4 (length _shape)
    ;; int32 _time
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _shape
       (write-long (length _shape) s) (princ _shape s)
     ;; int32 _time
       (write-long _time s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _shape
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _shape (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int32 _time
     (setq _time (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass pck2::movesrvResponse
  :super ros::object
  :slots (_return ))

(defmethod pck2::movesrvResponse
  (:init
   (&key
    ((:return __return) "")
    )
   (send-super :init)
   (setq _return (string __return))
   self)
  (:return
   (&optional __return)
   (if __return (setq _return __return)) _return)
  (:serialization-length
   ()
   (+
    ;; string _return
    4 (length _return)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _return
       (write-long (length _return) s) (princ _return s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _return
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _return (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass pck2::movesrv
  :super ros::object
  :slots ())

(setf (get pck2::movesrv :md5sum-) "a076d4040c3b13d43930b340985ffc25")
(setf (get pck2::movesrv :datatype-) "pck2/movesrv")
(setf (get pck2::movesrv :request) pck2::movesrvRequest)
(setf (get pck2::movesrv :response) pck2::movesrvResponse)

(defmethod pck2::movesrvRequest
  (:response () (instance pck2::movesrvResponse :init)))

(setf (get pck2::movesrvRequest :md5sum-) "a076d4040c3b13d43930b340985ffc25")
(setf (get pck2::movesrvRequest :datatype-) "pck2/movesrvRequest")
(setf (get pck2::movesrvRequest :definition-)
      "string shape
int32 time
---
string return

")

(setf (get pck2::movesrvResponse :md5sum-) "a076d4040c3b13d43930b340985ffc25")
(setf (get pck2::movesrvResponse :datatype-) "pck2/movesrvResponse")
(setf (get pck2::movesrvResponse :definition-)
      "string shape
int32 time
---
string return

")



(provide :pck2/movesrv "a076d4040c3b13d43930b340985ffc25")


