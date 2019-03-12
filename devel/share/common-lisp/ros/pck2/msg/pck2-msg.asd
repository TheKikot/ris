
(cl:in-package :asdf)

(defsystem "pck2-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Hello" :depends-on ("_package_Hello"))
    (:file "_package_Hello" :depends-on ("_package"))
    (:file "homework_message" :depends-on ("_package_homework_message"))
    (:file "_package_homework_message" :depends-on ("_package"))
  ))