; Auto-generated. Do not edit!


(cl:in-package MAF3_msgs-msg)


;//! \htmlinclude MAF3_Raw.msg.html

(cl:defclass <MAF3_Raw> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (Fz
    :reader Fz
    :initarg :Fz
    :type cl:fixnum
    :initform 0)
   (Mx
    :reader Mx
    :initarg :Mx
    :type cl:fixnum
    :initform 0)
   (My
    :reader My
    :initarg :My
    :type cl:fixnum
    :initform 0))
)

(cl:defclass MAF3_Raw (<MAF3_Raw>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MAF3_Raw>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MAF3_Raw)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name MAF3_msgs-msg:<MAF3_Raw> is deprecated: use MAF3_msgs-msg:MAF3_Raw instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <MAF3_Raw>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader MAF3_msgs-msg:header-val is deprecated.  Use MAF3_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'Fz-val :lambda-list '(m))
(cl:defmethod Fz-val ((m <MAF3_Raw>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader MAF3_msgs-msg:Fz-val is deprecated.  Use MAF3_msgs-msg:Fz instead.")
  (Fz m))

(cl:ensure-generic-function 'Mx-val :lambda-list '(m))
(cl:defmethod Mx-val ((m <MAF3_Raw>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader MAF3_msgs-msg:Mx-val is deprecated.  Use MAF3_msgs-msg:Mx instead.")
  (Mx m))

(cl:ensure-generic-function 'My-val :lambda-list '(m))
(cl:defmethod My-val ((m <MAF3_Raw>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader MAF3_msgs-msg:My-val is deprecated.  Use MAF3_msgs-msg:My instead.")
  (My m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MAF3_Raw>) ostream)
  "Serializes a message object of type '<MAF3_Raw>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'Fz)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'Fz)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'Mx)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'Mx)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'My)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'My)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MAF3_Raw>) istream)
  "Deserializes a message object of type '<MAF3_Raw>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'Fz)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'Fz)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'Mx)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'Mx)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'My)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'My)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MAF3_Raw>)))
  "Returns string type for a message object of type '<MAF3_Raw>"
  "MAF3_msgs/MAF3_Raw")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MAF3_Raw)))
  "Returns string type for a message object of type 'MAF3_Raw"
  "MAF3_msgs/MAF3_Raw")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MAF3_Raw>)))
  "Returns md5sum for a message object of type '<MAF3_Raw>"
  "f2737879b757edf1b6829d2f9ca33456")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MAF3_Raw)))
  "Returns md5sum for a message object of type 'MAF3_Raw"
  "f2737879b757edf1b6829d2f9ca33456")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MAF3_Raw>)))
  "Returns full string definition for message of type '<MAF3_Raw>"
  (cl:format cl:nil "Header header~%uint16 Fz~%uint16 Mx~%uint16 My~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MAF3_Raw)))
  "Returns full string definition for message of type 'MAF3_Raw"
  (cl:format cl:nil "Header header~%uint16 Fz~%uint16 Mx~%uint16 My~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MAF3_Raw>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MAF3_Raw>))
  "Converts a ROS message object to a list"
  (cl:list 'MAF3_Raw
    (cl:cons ':header (header msg))
    (cl:cons ':Fz (Fz msg))
    (cl:cons ':Mx (Mx msg))
    (cl:cons ':My (My msg))
))
