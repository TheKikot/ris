
(cl:in-package :asdf)

(defsystem "pck2-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "movesrv" :depends-on ("_package_movesrv"))
    (:file "_package_movesrv" :depends-on ("_package"))
    (:file "sum" :depends-on ("_package_sum"))
    (:file "_package_sum" :depends-on ("_package"))
  ))