// Auto-generated. Do not edit!

// (in-package pck2.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class movesrvRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.shape = null;
      this.time = null;
    }
    else {
      if (initObj.hasOwnProperty('shape')) {
        this.shape = initObj.shape
      }
      else {
        this.shape = '';
      }
      if (initObj.hasOwnProperty('time')) {
        this.time = initObj.time
      }
      else {
        this.time = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type movesrvRequest
    // Serialize message field [shape]
    bufferOffset = _serializer.string(obj.shape, buffer, bufferOffset);
    // Serialize message field [time]
    bufferOffset = _serializer.int32(obj.time, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type movesrvRequest
    let len;
    let data = new movesrvRequest(null);
    // Deserialize message field [shape]
    data.shape = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [time]
    data.time = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.shape.length;
    return length + 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'pck2/movesrvRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4eb052c7f02dc3d6b175b629829c67f8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string shape
    int32 time
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new movesrvRequest(null);
    if (msg.shape !== undefined) {
      resolved.shape = msg.shape;
    }
    else {
      resolved.shape = ''
    }

    if (msg.time !== undefined) {
      resolved.time = msg.time;
    }
    else {
      resolved.time = 0
    }

    return resolved;
    }
};

class movesrvResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.return = null;
    }
    else {
      if (initObj.hasOwnProperty('return')) {
        this.return = initObj.return
      }
      else {
        this.return = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type movesrvResponse
    // Serialize message field [return]
    bufferOffset = _serializer.string(obj.return, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type movesrvResponse
    let len;
    let data = new movesrvResponse(null);
    // Deserialize message field [return]
    data.return = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.return.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'pck2/movesrvResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8d02df2c0dff1a16a80230979e550820';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string return
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new movesrvResponse(null);
    if (msg.return !== undefined) {
      resolved.return = msg.return;
    }
    else {
      resolved.return = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: movesrvRequest,
  Response: movesrvResponse,
  md5sum() { return 'a076d4040c3b13d43930b340985ffc25'; },
  datatype() { return 'pck2/movesrv'; }
};
