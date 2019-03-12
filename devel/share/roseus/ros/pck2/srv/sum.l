;; Auto-generated. Do not edit!


(when (boundp 'pck2::sum)
  (if (not (find-package "PCK2"))
    (make-package "PCK2"))
  (shadow 'sum (find-package "PCK2")))
(unless (find-package "PCK2::SUM")
  (make-package "PCK2::SUM"))
(unless (find-package "PCK2::SUMREQUEST")
  (make-package "PCK2::SUMREQUEST"))
(unless (find-package "PCK2::SUMRESPONSE")
  (make-package "PCK2::SUMRESPONSE"))

(in-package "ROS")





(defclass pck2::sumRequest
  :super ros::object
  :slots (_content ))

(defmethod pck2::sumRequest
  (:init
   (&key
    ((:content __content) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _content __content)
   self)
  (:content
   (&optional __content)
   (if __content (setq _content __content)) _content)
  (:serialization-length
   ()
   (+
    ;; int32[] _content
    (* 4    (length _content)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32[] _content
     (write-long (length _content) s)
     (dotimes (i (length _content))
       (write-long (elt _content i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32[] _content
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _content (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _content i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(defclass pck2::sumResponse
  :super ros::object
  :slots (_comment ))

(defmethod pck2::sumResponse
  (:init
   (&key
    ((:comment __comment) 0)
    )
   (send-super :init)
   (setq _comment (round __comment))
   self)
  (:comment
   (&optional __comment)
   (if __comment (setq _comment __comment)) _comment)
  (:serialization-length
   ()
   (+
    ;; int32 _comment
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _comment
       (write-long _comment s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _comment
     (setq _comment (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass pck2::sum
  :super ros::object
  :slots ())

(setf (get pck2::sum :md5sum-) "eff151ed5a6df648d5c30ca5d71ccbda")
(setf (get pck2::sum :datatype-) "pck2/sum")
(setf (get pck2::sum :request) pck2::sumRequest)
(setf (get pck2::sum :response) pck2::sumResponse)

(defmethod pck2::sumRequest
  (:response () (instance pck2::sumResponse :init)))

(setf (get pck2::sumRequest :md5sum-) "eff151ed5a6df648d5c30ca5d71ccbda")
(setf (get pck2::sumRequest :datatype-) "pck2/sumRequest")
(setf (get pck2::sumRequest :definition-)
      "int32[] content
---
int32 comment


")

(setf (get pck2::sumResponse :md5sum-) "eff151ed5a6df648d5c30ca5d71ccbda")
(setf (get pck2::sumResponse :datatype-) "pck2/sumResponse")
(setf (get pck2::sumResponse :definition-)
      "int32[] content
---
int32 comment


")



(provide :pck2/sum "eff151ed5a6df648d5c30ca5d71ccbda")


