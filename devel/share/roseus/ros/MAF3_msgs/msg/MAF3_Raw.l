;; Auto-generated. Do not edit!


(when (boundp 'MAF3_msgs::MAF3_Raw)
  (if (not (find-package "MAF3_MSGS"))
    (make-package "MAF3_MSGS"))
  (shadow 'MAF3_Raw (find-package "MAF3_MSGS")))
(unless (find-package "MAF3_MSGS::MAF3_RAW")
  (make-package "MAF3_MSGS::MAF3_RAW"))

(in-package "ROS")
;;//! \htmlinclude MAF3_Raw.msg.html


(defclass MAF3_msgs::MAF3_Raw
  :super ros::object
  :slots (_Fz _Mx _My ))

(defmethod MAF3_msgs::MAF3_Raw
  (:init
   (&key
    ((:Fz __Fz) 0)
    ((:Mx __Mx) 0)
    ((:My __My) 0)
    )
   (send-super :init)
   (setq _Fz (round __Fz))
   (setq _Mx (round __Mx))
   (setq _My (round __My))
   self)
  (:Fz
   (&optional __Fz)
   (if __Fz (setq _Fz __Fz)) _Fz)
  (:Mx
   (&optional __Mx)
   (if __Mx (setq _Mx __Mx)) _Mx)
  (:My
   (&optional __My)
   (if __My (setq _My __My)) _My)
  (:serialization-length
   ()
   (+
    ;; uint16 _Fz
    2
    ;; uint16 _Mx
    2
    ;; uint16 _My
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint16 _Fz
       (write-word _Fz s)
     ;; uint16 _Mx
       (write-word _Mx s)
     ;; uint16 _My
       (write-word _My s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint16 _Fz
     (setq _Fz (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _Mx
     (setq _Mx (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _My
     (setq _My (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get MAF3_msgs::MAF3_Raw :md5sum-) "88234e0056df7c10f369a7d34efefabf")
(setf (get MAF3_msgs::MAF3_Raw :datatype-) "MAF3_msgs/MAF3_Raw")
(setf (get MAF3_msgs::MAF3_Raw :definition-)
      "uint16 Fz
uint16 Mx
uint16 My
")



(provide :MAF3_msgs/MAF3_Raw "88234e0056df7c10f369a7d34efefabf")


