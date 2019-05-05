;; Auto-generated. Do not edit!


(when (boundp 'exercise6::GetLocation)
  (if (not (find-package "EXERCISE6"))
    (make-package "EXERCISE6"))
  (shadow 'GetLocation (find-package "EXERCISE6")))
(unless (find-package "EXERCISE6::GETLOCATION")
  (make-package "EXERCISE6::GETLOCATION"))
(unless (find-package "EXERCISE6::GETLOCATIONREQUEST")
  (make-package "EXERCISE6::GETLOCATIONREQUEST"))
(unless (find-package "EXERCISE6::GETLOCATIONRESPONSE")
  (make-package "EXERCISE6::GETLOCATIONRESPONSE"))

(in-package "ROS")





(defclass exercise6::GetLocationRequest
  :super ros::object
  :slots (_x _y ))

(defmethod exercise6::GetLocationRequest
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:serialization-length
   ()
   (+
    ;; float32 _x
    4
    ;; float32 _y
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _x
       (sys::poke _x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y
       (sys::poke _y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass exercise6::GetLocationResponse
  :super ros::object
  :slots ())

(defmethod exercise6::GetLocationResponse
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

(defclass exercise6::GetLocation
  :super ros::object
  :slots ())

(setf (get exercise6::GetLocation :md5sum-) "ff8d7d66dd3e4b731ef14a45d38888b6")
(setf (get exercise6::GetLocation :datatype-) "exercise6/GetLocation")
(setf (get exercise6::GetLocation :request) exercise6::GetLocationRequest)
(setf (get exercise6::GetLocation :response) exercise6::GetLocationResponse)

(defmethod exercise6::GetLocationRequest
  (:response () (instance exercise6::GetLocationResponse :init)))

(setf (get exercise6::GetLocationRequest :md5sum-) "ff8d7d66dd3e4b731ef14a45d38888b6")
(setf (get exercise6::GetLocationRequest :datatype-) "exercise6/GetLocationRequest")
(setf (get exercise6::GetLocationRequest :definition-)
      "float32 x
float32 y

---
")

(setf (get exercise6::GetLocationResponse :md5sum-) "ff8d7d66dd3e4b731ef14a45d38888b6")
(setf (get exercise6::GetLocationResponse :datatype-) "exercise6/GetLocationResponse")
(setf (get exercise6::GetLocationResponse :definition-)
      "float32 x
float32 y

---
")



(provide :exercise6/GetLocation "ff8d7d66dd3e4b731ef14a45d38888b6")


