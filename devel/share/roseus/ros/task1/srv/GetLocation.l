;; Auto-generated. Do not edit!


(when (boundp 'task1::GetLocation)
  (if (not (find-package "TASK1"))
    (make-package "TASK1"))
  (shadow 'GetLocation (find-package "TASK1")))
(unless (find-package "TASK1::GETLOCATION")
  (make-package "TASK1::GETLOCATION"))
(unless (find-package "TASK1::GETLOCATIONREQUEST")
  (make-package "TASK1::GETLOCATIONREQUEST"))
(unless (find-package "TASK1::GETLOCATIONRESPONSE")
  (make-package "TASK1::GETLOCATIONRESPONSE"))

(in-package "ROS")





(defclass task1::GetLocationRequest
  :super ros::object
  :slots ())

(defmethod task1::GetLocationRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass task1::GetLocationResponse
  :super ros::object
  :slots ())

(defmethod task1::GetLocationResponse
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass task1::GetLocation
  :super ros::object
  :slots ())

(setf (get task1::GetLocation :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get task1::GetLocation :datatype-) "task1/GetLocation")
(setf (get task1::GetLocation :request) task1::GetLocationRequest)
(setf (get task1::GetLocation :response) task1::GetLocationResponse)

(defmethod task1::GetLocationRequest
  (:response () (instance task1::GetLocationResponse :init)))

(setf (get task1::GetLocationRequest :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get task1::GetLocationRequest :datatype-) "task1/GetLocationRequest")
(setf (get task1::GetLocationRequest :definition-)
      "
---

")

(setf (get task1::GetLocationResponse :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get task1::GetLocationResponse :datatype-) "task1/GetLocationResponse")
(setf (get task1::GetLocationResponse :definition-)
      "
---

")



(provide :task1/GetLocation "d41d8cd98f00b204e9800998ecf8427e")


