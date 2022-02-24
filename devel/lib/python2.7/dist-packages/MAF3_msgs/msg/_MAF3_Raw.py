# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from MAF3_msgs/MAF3_Raw.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class MAF3_Raw(genpy.Message):
  _md5sum = "88234e0056df7c10f369a7d34efefabf"
  _type = "MAF3_msgs/MAF3_Raw"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint16 Fz
uint16 Mx
uint16 My"""
  __slots__ = ['Fz','Mx','My']
  _slot_types = ['uint16','uint16','uint16']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       Fz,Mx,My

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MAF3_Raw, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.Fz is None:
        self.Fz = 0
      if self.Mx is None:
        self.Mx = 0
      if self.My is None:
        self.My = 0
    else:
      self.Fz = 0
      self.Mx = 0
      self.My = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3H().pack(_x.Fz, _x.Mx, _x.My))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 6
      (_x.Fz, _x.Mx, _x.My,) = _get_struct_3H().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3H().pack(_x.Fz, _x.Mx, _x.My))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 6
      (_x.Fz, _x.Mx, _x.My,) = _get_struct_3H().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3H = None
def _get_struct_3H():
    global _struct_3H
    if _struct_3H is None:
        _struct_3H = struct.Struct("<3H")
    return _struct_3H
