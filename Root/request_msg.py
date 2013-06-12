#
# This class is automatically generated by mig. DO NOT EDIT THIS FILE.
# This class implements a Python interface to the 'request_msg'
# message type.
#

import tinyos.message.Message

# The default size of this message type in bytes.
DEFAULT_MESSAGE_SIZE = 10

# The Active Message type associated with this message.
AM_TYPE = 8

class request_msg(tinyos.message.Message.Message):
    # Create a new request_msg of size 10.
    def __init__(self, data="", addr=None, gid=None, base_offset=0, data_length=10):
        tinyos.message.Message.Message.__init__(self, data, addr, gid, base_offset, data_length)
        self.amTypeSet(AM_TYPE)
    
    # Get AM_TYPE
    def get_amType(cls):
        return AM_TYPE
    
    get_amType = classmethod(get_amType)
    
    #
    # Return a String representation of this message. Includes the
    # message type name and the non-indexed field values.
    #
    def __str__(self):
        s = "Message <request_msg> \n"
        try:
            s += "  [node_id=0x%x]\n" % (self.get_node_id())
        except:
            pass
        try:
            s += "  [transaction_number=0x%x]\n" % (self.get_transaction_number())
        except:
            pass
        try:
            s += "  [request_code=0x%x]\n" % (self.get_request_code())
        except:
            pass
        try:
            s += "  [request_device=0x%x]\n" % (self.get_request_device())
        except:
            pass
        try:
            s += "  [request_data=0x%x]\n" % (self.get_request_data())
        except:
            pass
        try:
            s += "  [reserved=";
            for i in range(0, 1):
                s += "0x%x " % (self.getElement_reserved(i) & 0xffff)
            s += "]\n";
        except:
            pass
        return s

    # Message-type-specific access methods appear below.

    #
    # Accessor methods for field: node_id
    #   Field type: int
    #   Offset (bits): 0
    #   Size (bits): 16
    #

    #
    # Return whether the field 'node_id' is signed (False).
    #
    def isSigned_node_id(self):
        return False
    
    #
    # Return whether the field 'node_id' is an array (False).
    #
    def isArray_node_id(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'node_id'
    #
    def offset_node_id(self):
        return (0 / 8)
    
    #
    # Return the offset (in bits) of the field 'node_id'
    #
    def offsetBits_node_id(self):
        return 0
    
    #
    # Return the value (as a int) of the field 'node_id'
    #
    def get_node_id(self):
        return self.getUIntElement(self.offsetBits_node_id(), 16, 1)
    
    #
    # Set the value of the field 'node_id'
    #
    def set_node_id(self, value):
        self.setUIntElement(self.offsetBits_node_id(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'node_id'
    #
    def size_node_id(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'node_id'
    #
    def sizeBits_node_id(self):
        return 16
    
    #
    # Accessor methods for field: transaction_number
    #   Field type: int
    #   Offset (bits): 16
    #   Size (bits): 16
    #

    #
    # Return whether the field 'transaction_number' is signed (False).
    #
    def isSigned_transaction_number(self):
        return False
    
    #
    # Return whether the field 'transaction_number' is an array (False).
    #
    def isArray_transaction_number(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'transaction_number'
    #
    def offset_transaction_number(self):
        return (16 / 8)
    
    #
    # Return the offset (in bits) of the field 'transaction_number'
    #
    def offsetBits_transaction_number(self):
        return 16
    
    #
    # Return the value (as a int) of the field 'transaction_number'
    #
    def get_transaction_number(self):
        return self.getUIntElement(self.offsetBits_transaction_number(), 16, 1)
    
    #
    # Set the value of the field 'transaction_number'
    #
    def set_transaction_number(self, value):
        self.setUIntElement(self.offsetBits_transaction_number(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'transaction_number'
    #
    def size_transaction_number(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'transaction_number'
    #
    def sizeBits_transaction_number(self):
        return 16
    
    #
    # Accessor methods for field: request_code
    #   Field type: short
    #   Offset (bits): 32
    #   Size (bits): 8
    #

    #
    # Return whether the field 'request_code' is signed (False).
    #
    def isSigned_request_code(self):
        return False
    
    #
    # Return whether the field 'request_code' is an array (False).
    #
    def isArray_request_code(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'request_code'
    #
    def offset_request_code(self):
        return (32 / 8)
    
    #
    # Return the offset (in bits) of the field 'request_code'
    #
    def offsetBits_request_code(self):
        return 32
    
    #
    # Return the value (as a short) of the field 'request_code'
    #
    def get_request_code(self):
        return self.getUIntElement(self.offsetBits_request_code(), 8, 1)
    
    #
    # Set the value of the field 'request_code'
    #
    def set_request_code(self, value):
        self.setUIntElement(self.offsetBits_request_code(), 8, value, 1)
    
    #
    # Return the size, in bytes, of the field 'request_code'
    #
    def size_request_code(self):
        return (8 / 8)
    
    #
    # Return the size, in bits, of the field 'request_code'
    #
    def sizeBits_request_code(self):
        return 8
    
    #
    # Accessor methods for field: request_device
    #   Field type: short
    #   Offset (bits): 40
    #   Size (bits): 8
    #

    #
    # Return whether the field 'request_device' is signed (False).
    #
    def isSigned_request_device(self):
        return False
    
    #
    # Return whether the field 'request_device' is an array (False).
    #
    def isArray_request_device(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'request_device'
    #
    def offset_request_device(self):
        return (40 / 8)
    
    #
    # Return the offset (in bits) of the field 'request_device'
    #
    def offsetBits_request_device(self):
        return 40
    
    #
    # Return the value (as a short) of the field 'request_device'
    #
    def get_request_device(self):
        return self.getUIntElement(self.offsetBits_request_device(), 8, 1)
    
    #
    # Set the value of the field 'request_device'
    #
    def set_request_device(self, value):
        self.setUIntElement(self.offsetBits_request_device(), 8, value, 1)
    
    #
    # Return the size, in bytes, of the field 'request_device'
    #
    def size_request_device(self):
        return (8 / 8)
    
    #
    # Return the size, in bits, of the field 'request_device'
    #
    def sizeBits_request_device(self):
        return 8
    
    #
    # Accessor methods for field: request_data
    #   Field type: int
    #   Offset (bits): 48
    #   Size (bits): 16
    #

    #
    # Return whether the field 'request_data' is signed (False).
    #
    def isSigned_request_data(self):
        return False
    
    #
    # Return whether the field 'request_data' is an array (False).
    #
    def isArray_request_data(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'request_data'
    #
    def offset_request_data(self):
        return (48 / 8)
    
    #
    # Return the offset (in bits) of the field 'request_data'
    #
    def offsetBits_request_data(self):
        return 48
    
    #
    # Return the value (as a int) of the field 'request_data'
    #
    def get_request_data(self):
        return self.getUIntElement(self.offsetBits_request_data(), 16, 1)
    
    #
    # Set the value of the field 'request_data'
    #
    def set_request_data(self, value):
        self.setUIntElement(self.offsetBits_request_data(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'request_data'
    #
    def size_request_data(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'request_data'
    #
    def sizeBits_request_data(self):
        return 16
    
    #
    # Accessor methods for field: reserved
    #   Field type: int[]
    #   Offset (bits): 64
    #   Size of each element (bits): 16
    #

    #
    # Return whether the field 'reserved' is signed (False).
    #
    def isSigned_reserved(self):
        return False
    
    #
    # Return whether the field 'reserved' is an array (True).
    #
    def isArray_reserved(self):
        return True
    
    #
    # Return the offset (in bytes) of the field 'reserved'
    #
    def offset_reserved(self, index1):
        offset = 64
        if index1 < 0 or index1 >= 1:
            raise IndexError
        offset += 0 + index1 * 16
        return (offset / 8)
    
    #
    # Return the offset (in bits) of the field 'reserved'
    #
    def offsetBits_reserved(self, index1):
        offset = 64
        if index1 < 0 or index1 >= 1:
            raise IndexError
        offset += 0 + index1 * 16
        return offset
    
    #
    # Return the entire array 'reserved' as a int[]
    #
    def get_reserved(self):
        tmp = [None]*1
        for index0 in range (0, self.numElements_reserved(0)):
                tmp[index0] = self.getElement_reserved(index0)
        return tmp
    
    #
    # Set the contents of the array 'reserved' from the given int[]
    #
    def set_reserved(self, value):
        for index0 in range(0, len(value)):
            self.setElement_reserved(index0, value[index0])

    #
    # Return an element (as a int) of the array 'reserved'
    #
    def getElement_reserved(self, index1):
        return self.getUIntElement(self.offsetBits_reserved(index1), 16, 1)
    
    #
    # Set an element of the array 'reserved'
    #
    def setElement_reserved(self, index1, value):
        self.setUIntElement(self.offsetBits_reserved(index1), 16, value, 1)
    
    #
    # Return the total size, in bytes, of the array 'reserved'
    #
    def totalSize_reserved(self):
        return (16 / 8)
    
    #
    # Return the total size, in bits, of the array 'reserved'
    #
    def totalSizeBits_reserved(self):
        return 16
    
    #
    # Return the size, in bytes, of each element of the array 'reserved'
    #
    def elementSize_reserved(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of each element of the array 'reserved'
    #
    def elementSizeBits_reserved(self):
        return 16
    
    #
    # Return the number of dimensions in the array 'reserved'
    #
    def numDimensions_reserved(self):
        return 1
    
    #
    # Return the number of elements in the array 'reserved'
    #
    def numElements_reserved():
        return 1
    
    #
    # Return the number of elements in the array 'reserved'
    # for the given dimension.
    #
    def numElements_reserved(self, dimension):
        array_dims = [ 1,  ]
        if dimension < 0 or dimension >= 1:
            raise IndexException
        if array_dims[dimension] == 0:
            raise IndexError
        return array_dims[dimension]
    
