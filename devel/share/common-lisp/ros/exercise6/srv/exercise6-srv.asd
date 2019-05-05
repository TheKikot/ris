
(cl:in-package :asdf)

(defsystem "exercise6-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "GetLocation" :depends-on ("_package_GetLocation"))
    (:file "_package_GetLocation" :depends-on ("_package"))
  ))