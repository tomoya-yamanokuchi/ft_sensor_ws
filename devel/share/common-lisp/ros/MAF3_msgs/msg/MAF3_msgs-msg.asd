
(cl:in-package :asdf)

(defsystem "MAF3_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "MAF3_Raw" :depends-on ("_package_MAF3_Raw"))
    (:file "_package_MAF3_Raw" :depends-on ("_package"))
  ))