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

class sumRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.content = null;
    }
    else {
      if (initObj.hasOwnProperty('content')) {
        this.content = initObj.content
      }
      else {
        this.content = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type sumRequest
    // Serialize message field [content]
    bufferOffset = _arraySerializer.int32(obj.content, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type sumRequest
    let len;
    let data = new sumRequest(null);
    // Deserialize message field [content]
    data.content = _arrayDeserializer.int32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 4 * object.content.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'pck2/sumRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ccf899189e69ae877cd652bfc1b26630';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32[] content
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new sumRequest(null);
    if (msg.content !== undefined) {
      resolved.content = msg.content;
    }
    else {
      resolved.content = []
    }

    return resolved;
    }
};

class sumResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.comment = null;
    }
    else {
      if (initObj.hasOwnProperty('comment')) {
        this.comment = initObj.comment
      }
      else {
        this.comment = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type sumResponse
    // Serialize message field [comment]
    bufferOffset = _serializer.int32(obj.comment, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type sumResponse
    let len;
    let data = new sumResponse(null);
    // Deserialize message field [comment]
    data.comment = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'pck2/sumResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '91e9f7dcfa8636513f40912ab8826294';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 comment
    
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new sumResponse(null);
    if (msg.comment !== undefined) {
      resolved.comment = msg.comment;
    }
    else {
      resolved.comment = 0
    }

    return resolved;
    }
};

module.exports = {
  Request: sumRequest,
  Response: sumResponse,
  md5sum() { return 'eff151ed5a6df648d5c30ca5d71ccbda'; },
  datatype() { return 'pck2/sum'; }
};
