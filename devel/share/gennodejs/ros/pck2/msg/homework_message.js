// Auto-generated. Do not edit!

// (in-package pck2.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class homework_message {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.content = null;
      this.number = null;
    }
    else {
      if (initObj.hasOwnProperty('content')) {
        this.content = initObj.content
      }
      else {
        this.content = '';
      }
      if (initObj.hasOwnProperty('number')) {
        this.number = initObj.number
      }
      else {
        this.number = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type homework_message
    // Serialize message field [content]
    bufferOffset = _serializer.string(obj.content, buffer, bufferOffset);
    // Serialize message field [number]
    bufferOffset = _serializer.int32(obj.number, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type homework_message
    let len;
    let data = new homework_message(null);
    // Deserialize message field [content]
    data.content = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [number]
    data.number = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.content.length;
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'pck2/homework_message';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0dd088ad22ee351bec89d6fb19ccdc0d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string content
    int32 number
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new homework_message(null);
    if (msg.content !== undefined) {
      resolved.content = msg.content;
    }
    else {
      resolved.content = ''
    }

    if (msg.number !== undefined) {
      resolved.number = msg.number;
    }
    else {
      resolved.number = 0
    }

    return resolved;
    }
};

module.exports = homework_message;
