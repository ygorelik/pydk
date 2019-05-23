ydk.types module
================

types.py

Contains type definitions.


.. py:class:: ydk.types.DELETE()

	Bases: :class:`object`
	
	Marker class used to mark existing nodes that are to be deleted. 

	Assign `DELETE()` to a leaf for its deletion. A CRUD update operation will delete the leaf from the device when this marker is set.
	
	Assign `DELETE()` to a container object attribute `yfilter` in order to mark it for delete operation.


.. py:class:: ydk.types.REMOVE()

    Bases: :class:`object`
    
    Class marker, which is used to mark nodes that are to be deleted silently (no error developed, if the object does not exists). 

    Assign `REMOVE()` to a leaf for its deletion. A CRUD update operation will silently delete the leaf from the device when this marker is set.
    
    Assign `REMOVE()` to a container object attribute `yfilter` in order to mark it for remove operation.


.. py:class:: ydk.types.READ()

    Bases: :class:`object`
    
    Class marker, which is used to mark nodes that are to be read from device. 

    Assign `READ()` to a leaf in order to read specifically leaf value.
    
    Assign `READ()` to a container object attribute `yfilter` to mark it for read operation.


.. py:class:: ydk.types.CREATE(value=None)

    Bases: :class:`object`
    
    Class marker, which is used to mark nodes that are to be created. 

    Assign `CREATE(value)` to a leaf in order to create it with specified `value`.
    
    Assign `CREATE()` to a container object attribute `yfilter` to mark it for create operation.


.. py:class:: ydk.types.MERGE(value=None)

    Bases: :class:`object`
    
    Class marker, which is used to mark nodes that are to be merged with existing configuration. 

    Assign `MERGE(value)` to a leaf in order to create or replace it with specified `value`.
    
    Assign `MERGE()` to a container object attribute `yfilter` to mark it for merge operation.


.. py:class:: ydk.types.REPLACE(value=None)

    Bases: :class:`object`
    
    Class marker, which is used to mark nodes that are to be merged with existing configuration. 

    Assign `REPLACE(value)` to a leaf in order to replace its value with specified `value`.
    
    Assign `REPLACE()` to a container object attribute `yfilter` to mark it for replace operation.


.. py:class:: ydk.types.Decimal64(str_val)

	Bases: :class:`object`
	
	Represents the decimal64 YANG type. The decimal64 type represents a subset
	of the real numbers, which can be represented by decimal numerals. 
	 
	The value space of decimal64 is the set of numbers that can be obtained by multiplying 
	a 64-bit signed integer by a negative power of ten, i.e., expressible as “i x 10^-n” 
	where i is an integer64 and n is an integer between 1 and 18, inclusively.

	str_val
			String representation of the decimal64 number.
	
	
.. py:class:: ydk.types.Empty()

	Bases: :class:`object`
	
	Represents the empty type in YANG. The empty built-in type represents a leaf that does 
	not have any value, it conveys information by its presence or absence.


.. py:class:: ydk.types.FixedBitsDict(dictionary, pos_map)

	Bases: :class:`object`
	
	Super class of all classes that represents the bits type in YANG

	A concrete implementation of this class has a dictionary. The bits built-in type 
	represents a bit set. That is, a bits value is a set of flags identified by small 
	integer position numbers starting at 0. Each bit number has an assigned name.
	To set a bit use the name of the bit as a key into the dictionary and set the 
	value to True (False to unset).


.. py:class:: ydk.types.YList()

	Bases: :class:`list`
	
	Represents a list with support for hanging a parent.

	All YANG based entity classes that have lists in them 
	use YList to represent the list. 
	
.. py:class:: ydk.types.YLeafList()

	Bases: :class:`ydk.types.YList`

	Represents a leaf-list with support for hanging a parent.

	All YANG leaf-list is represented as YLeafList. YLeafList is 
	associative array, it contains unique elemenets.
	