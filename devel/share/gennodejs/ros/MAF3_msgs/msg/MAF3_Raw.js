// Auto-generated. Do not edit!

// (in-package MAF3_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class MAF3_Raw {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.Fz = null;
      this.Mx = null;
      this.My = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('Fz')) {
        this.Fz = initObj.Fz
      }
      else {
        this.Fz = 0;
      }
      if (initObj.hasOwnProperty('Mx')) {
        this.Mx = initObj.Mx
      }
      else {
        this.Mx = 0;
      }
      if (initObj.hasOwnProperty('My')) {
        this.My = initObj.My
      }
      else {
        this.My = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MAF3_Raw
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [Fz]
    bufferOffset = _serializer.uint16(obj.Fz, buffer, bufferOffset);
    // Serialize message field [Mx]
    bufferOffset = _serializer.uint16(obj.Mx, buffer, bufferOffset);
    // Serialize message field [My]
    bufferOffset = _serializer.uint16(obj.My, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MAF3_Raw
    let len;
    let data = new MAF3_Raw(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [Fz]
    data.Fz = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [Mx]
    data.Mx = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [My]
    data.My = _deserializer.uint16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 6;
  }

  static datatype() {
    // Returns string type for a message object
    return 'MAF3_msgs/MAF3_Raw';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f2737879b757edf1b6829d2f9ca33456';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MAF3_Raw(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.Fz !== undefined) {
      resolved.Fz = msg.Fz;
    }
    else {
      resolved.Fz = 0
    }

    if (msg.Mx !== undefined) {
      resolved.Mx = msg.Mx;
    }
    else {
      resolved.Mx = 0
    }

    if (msg.My !== undefined) {
      resolved.My = msg.My;
    }
    else {
      resolved.My = 0
    }

    return resolved;
    }
};

module.exports = MAF3_Raw;
