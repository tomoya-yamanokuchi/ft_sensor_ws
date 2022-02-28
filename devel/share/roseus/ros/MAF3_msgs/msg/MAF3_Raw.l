;; Auto-generated. Do not edit!


(when (boundp 'MAF3_msgs::MAF3_Raw)
  (if (not (find-package "MAF3_MSGS"))
    (make-package "MAF3_MSGS"))
  (shadow 'MAF3_Raw (find-package "MAF3_MSGS")))
(unless (find-package "MAF3_MSGS::MAF3_RAW")
  (make-package "MAF3_MSGS::MAF3_RAW"))

(in-package "ROS")
;;//! \htmlinclude MAF3_Raw.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass MAF3_msgs::MAF3_Raw
  :super ros::object
  :slots (_header _Fz _Mx _My ))

(defmethod MAF3_msgs::MAF3_Raw
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:Fz __Fz) 0)
    ((:Mx __Mx) 0)
    ((:My __My) 0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _Fz (round __Fz))
   (setq _Mx (round __Mx))
   (setq _My (round __My))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
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
    ;; std_msgs/Header _header
    (send _header :serialization-length)
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
     ;; std_msgs/Header _header
       (send _header :serialize s)
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
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; uint16 _Fz
     (setq _Fz (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _Mx
     (setq _Mx (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _My
     (setq _My (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get MAF3_msgs::MAF3_Raw :md5sum-) "f2737879b757edf1b6829d2f9ca33456")
(setf (get MAF3_msgs::MAF3_Raw :datatype-) "MAF3_msgs/MAF3_Raw")
(setf (get MAF3_msgs::MAF3_Raw :definition-)
      "Header header
uint16 Fz
uint16 Mx
uint16 My
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

")



(provide :MAF3_msgs/MAF3_Raw "f2737879b757edf1b6829d2f9ca33456")


