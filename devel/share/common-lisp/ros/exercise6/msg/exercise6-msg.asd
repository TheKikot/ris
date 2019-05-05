
(cl:in-package :asdf)

(defsystem "exercise6-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "RingLocation" :depends-on ("_package_RingLocation"))
    (:file "_package_RingLocation" :depends-on ("_package"))
  ))