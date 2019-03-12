// Generated by gencpp from file pck2/sumRequest.msg
// DO NOT EDIT!


#ifndef PCK2_MESSAGE_SUMREQUEST_H
#define PCK2_MESSAGE_SUMREQUEST_H


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
struct sumRequest_
{
  typedef sumRequest_<ContainerAllocator> Type;

  sumRequest_()
    : content()  {
    }
  sumRequest_(const ContainerAllocator& _alloc)
    : content(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _content_type;
  _content_type content;





  typedef boost::shared_ptr< ::pck2::sumRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pck2::sumRequest_<ContainerAllocator> const> ConstPtr;

}; // struct sumRequest_

typedef ::pck2::sumRequest_<std::allocator<void> > sumRequest;

typedef boost::shared_ptr< ::pck2::sumRequest > sumRequestPtr;
typedef boost::shared_ptr< ::pck2::sumRequest const> sumRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pck2::sumRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pck2::sumRequest_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::pck2::sumRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pck2::sumRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pck2::sumRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pck2::sumRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pck2::sumRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pck2::sumRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pck2::sumRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ccf899189e69ae877cd652bfc1b26630";
  }

  static const char* value(const ::pck2::sumRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xccf899189e69ae87ULL;
  static const uint64_t static_value2 = 0x7cd652bfc1b26630ULL;
};

template<class ContainerAllocator>
struct DataType< ::pck2::sumRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pck2/sumRequest";
  }

  static const char* value(const ::pck2::sumRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pck2::sumRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32[] content\n\
";
  }

  static const char* value(const ::pck2::sumRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pck2::sumRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.content);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct sumRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pck2::sumRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pck2::sumRequest_<ContainerAllocator>& v)
  {
    s << indent << "content[]" << std::endl;
    for (size_t i = 0; i < v.content.size(); ++i)
    {
      s << indent << "  content[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.content[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // PCK2_MESSAGE_SUMREQUEST_H
