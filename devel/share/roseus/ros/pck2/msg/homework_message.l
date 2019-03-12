;; Auto-generated. Do not edit!


(when (boundp 'pck2::homework_message)
  (if (not (find-package "PCK2"))
    (make-package "PCK2"))
  (shadow 'homework_message (find-package "PCK2")))
(unless (find-package "PCK2::HOMEWORK_MESSAGE")
  (make-package "PCK2::HOMEWORK_MESSAGE"))

(in-package "ROS")
;;//! \htmlinclude homework_message.msg.html


(defclass pck2::homework_message
  :super ros::object
  :slots (_content _number ))

(defmethod pck2::homework_message
  (:init
   (&key
    ((:content __content) "")
    ((:number __number) 0)
    )
   (send-super :init)
   (setq _content (string __content))
   (setq _number (round __number))
   self)
  (:content
   (&optional __content)
   (if __content (setq _content __content)) _content)
  (:number
   (&optional __number)
   (if __number (setq _number __number)) _number)
  (:serialization-length
   ()
   (+
    ;; string _content
    4 (length _content)
    ;; int32 _number
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _content
       (write-long (length _content) s) (princ _content s)
     ;; int32 _number
       (write-long _number s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _content
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _content (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int32 _number
     (setq _number (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get pck2::homework_message :md5sum-) "0dd088ad22ee351bec89d6fb19ccdc0d")
(setf (get pck2::homework_message :datatype-) "pck2/homework_message")
(setf (get pck2::homework_message :definition-)
      "string content
int32 number

")



(provide :pck2/homework_message "0dd088ad22ee351bec89d6fb19ccdc0d")


