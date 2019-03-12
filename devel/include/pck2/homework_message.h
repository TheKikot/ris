// Generated by gencpp from file pck2/homework_message.msg
// DO NOT EDIT!


#ifndef PCK2_MESSAGE_HOMEWORK_MESSAGE_H
#define PCK2_MESSAGE_HOMEWORK_MESSAGE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace pck2
{
template <class ContainerAllocator>
struct homework_message_
{
  typedef homework_message_<ContainerAllocator> Type;

  homework_message_()
    : content()
    , number(0)  {
    }
  homework_message_(const ContainerAllocator& _alloc)
    : content(_alloc)
    , number(0)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _content_type;
  _content_type content;

   typedef int32_t _number_type;
  _number_type number;





  typedef boost::shared_ptr< ::pck2::homework_message_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pck2::homework_message_<ContainerAllocator> const> ConstPtr;

}; // struct homework_message_

typedef ::pck2::homework_message_<std::allocator<void> > homework_message;

typedef boost::shared_ptr< ::pck2::homework_message > homework_messagePtr;
typedef boost::shared_ptr< ::pck2::homework_message const> homework_messageConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pck2::homework_message_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pck2::homework_message_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace pck2

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'pck2': ['/home/kikot/ROS/src/pck2/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::pck2::homework_message_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pck2::homework_message_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pck2::homework_message_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pck2::homework_message_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pck2::homework_message_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pck2::homework_message_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pck2::homework_message_<ContainerAllocator> >
{
  static const char* value()
  {
    return "0dd088ad22ee351bec89d6fb19ccdc0d";
  }

  static const char* value(const ::pck2::homework_message_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x0dd088ad22ee351bULL;
  static const uint64_t static_value2 = 0xec89d6fb19ccdc0dULL;
};

template<class ContainerAllocator>
struct DataType< ::pck2::homework_message_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pck2/homework_message";
  }

  static const char* value(const ::pck2::homework_message_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pck2::homework_message_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string content\n\
int32 number\n\
";
  }

  static const char* value(const ::pck2::homework_message_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pck2::homework_message_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.content);
      stream.next(m.number);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct homework_message_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pck2::homework_message_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pck2::homework_message_<ContainerAllocator>& v)
  {
    s << indent << "content: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.content);
    s << indent << "number: ";
    Printer<int32_t>::stream(s, indent + "  ", v.number);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PCK2_MESSAGE_HOMEWORK_MESSAGE_H