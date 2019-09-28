#  ----------------------------------------------------------------
# Copyright 2016 Cisco Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------

""" types.py

   Contains type definitions.

"""

from decimal import Decimal, getcontext
from .errors import YPYModelError, YPYError
from ._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST
from ._core._dm_meta_info import REFERENCE_IDENTITY_CLASS, ATTRIBUTE
from enum import Enum


class DELETE(object):
    """Marker class used to mark nodes that are to be deleted
    Assign DELETE object to a mark a leaf for deletion.
    A CRUD update operation will delete the leaf from the device it is on."""
    pass


class REMOVE(object):
    """Marker class used to mark nodes that are to be removed
    Assign REMOVE object to a mark a leaf for deletion.
    A CRUD update operation will delete the leaf from the device it is on."""
    pass


class MERGE(object):
    """Marker MERGE used to mark nodes that are to be merged
    Assign DELETE object to a mark a leaf for deletion.
    A CRUD update operation will delete the leaf from the device it is on."""

    def __init__(self, value=None):
        self._value = value

    def value(self):
        return self._value

    def set(self, value):
        self._value = value


class REPLACE(object):
    """Marker class used to mark nodes that are to be replaced
    Assign REPLACE object to a mark a leaf for deletion.
    A CRUD update operation will delete the leaf from the device it is on."""

    def __init__(self, value=None):
        self._value = value

    def value(self):
        return self._value

    def set(self, value):
        self._value = value


class CREATE(object):
    """Marker class used to mark nodes that are to be created
    Assign CREATE object to a mark a leaf for deletion.
    A CRUD update operation will delete the leaf from the device it is on."""

    def __init__(self, value=None):
        self._value = value

    def value(self):
        return self._value

    def set(self, value):
        self._value = value


class READ(object):
    """Marker class used to mark nodes that are to be read """
    pass


class Empty(object):
    """
        .. _ydk_models_types_Empty:

        Represents the empty type in YANG. The empty built-in type represents a leaf that does not have any
        value, it conveys information by its presence or absence.

    """
    def __eq__(self, rhs):
        if not isinstance(rhs, Empty):
            raise YPYModelError("Empty comparision error, invalid rhs\n")
        return True

    def __ne__(self, rhs):
        return not isinstance(rhs, Empty)

    __hash__ = object.__hash__


class Decimal64(object):
    """
        .. _ydk_models_types_Decimal64:

        Represents the decimal64 YANG type. The decimal64 type represents a
        subset of the real numbers, which can
        be represented by decimal numerals.  The value space of decimal64 is
        the set of numbers that can be obtained by multiplying a 64-bit
        signed integer by a negative power of ten, i.e., expressible as
        "i x 10^-n" where i is an integer64 and n is an integer between 1 and
        18, inclusively.
    """
    def __init__(self, str_val):
        self.s = str_val

    def __str__(self):

        return self.s

    def __eq__(self, rhs):
        if not isinstance(rhs, Decimal64):
            raise YPYModelError("Decimal64 comparision error, invalid rhs\n")
        return self.s == rhs.s

    def __ne__(self, rhs):
        if not isinstance(rhs, Decimal64):
            raise YPYModelError("Decimal64 comparision error, invalid rhs\n")
        return self.s != rhs.s

    def __lt__(self, rhs):
        if not isinstance(rhs, Decimal64):
            raise YPYModelError("Decimal64 comparision error, invalid rhs\n")
        if self.s is None:
            return True

        if rhs.s is None:
            return False

        getcontext().prec = 18
        self_dec = Decimal(self.s)
        rhs_dec = Decimal(rhs.s)
        return self_dec < rhs_dec

    def __le__(self, rhs):
        if not isinstance(rhs, Decimal64):
            raise YPYModelError("Decimal64 comparision error, invalid rhs\n")

        if self.s is None:
            return True

        if rhs.s is None:
            return False

        getcontext().prec = 18
        self_dec = Decimal(self.s)
        rhs_dec = Decimal(rhs.s)
        return self_dec <= rhs_dec

    def __gt__(self, rhs):
        if not isinstance(rhs, Decimal64):
            raise YPYModelError("Decimal64 comparision error, invalid rhs\n")

        if self.s is None:
            return False

        if rhs.s is None:
            return True

        getcontext().prec = 18
        self_dec = Decimal(self.s)
        rhs_dec = Decimal(rhs.s)

        return self_dec > rhs_dec

    def __ge__(self, rhs):
        if not isinstance(rhs, Decimal64):
            raise YPYModelError("Decimal64 comparision error, invalid rhs\n")

        if self.s is None:
            return False

        if rhs.s is None:
            return True

        getcontext().prec = 18
        self_dec = Decimal(self.s)
        rhs_dec = Decimal(rhs.s)

        return self_dec >= rhs_dec

    __hash__ = object.__hash__


class FixedBitsDict(object):
    """ Super class of all classes that represents the bits type in YANG

        A concrete implementation of this class has a dictionary.

       The bits built-in type represents a bit set.  That is, a bits value
       is a set of flags identified by small integer position numbers
       starting at 0.  Each bit number has an assigned name.
    """
    def __init__(self, dictionary, pos_map):
        self._dictionary = dictionary
        self._pos_map = pos_map

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __setitem__(self, key, item):
        if key not in self._dictionary:
            raise KeyError("The key {} is not defined.". format(key))
        self._dictionary[key] = item

    def __getitem__(self, key):
        return self._dictionary[key]

    def __str__(self):
        return " ".join([key for key in self._dictionary if self._dictionary[key] is True])

    def __ne__(self, rhs):
        return not self.__eq__(rhs)

    def _has_data(self):
        for key in self._dictionary:
            if self._dictionary[key]:
                return True
        return False

    __hash__ = object.__hash__


class YList(list):
    """ Represents a list with support for hanging a parent

        All YANG based entity classes that have lists in them use YList
        to represent the list.

        The "list" statement is used to define an interior data node in the
        schema tree.  A list node may exist in multiple instances in the data
        tree.  Each such instance is known as a list entry.  The "list"
        statement takes one argument, which is an identifier, followed by a
        block of substatements that holds detailed list information.

        A list entry is uniquely identified by the values of the list's keys,
        if defined.

    """
    def __init__(self):
        super(YList, self).__init__()
        self.parent = None
        self.name = None
        self.count = 0

    def __getitem__(self, key):
        if isinstance(key, slice):
            ret = YList()
            ret.parent = self.parent
            ret.name = self.name
            start = 0 if not key.start else key.start
            step = 1 if not key.step else key.step
            stop = len(self) if not key.stop else key.stop
            for k in range(start, stop, step):
                ret.append(super(YList, self).__getitem__(k))
        else:
            ret = super(YList, self).__getitem__(key)
        return ret

    def __getslice__(self, i, j):
        ret = YList()
        ret.parent = self.parent
        ret.name = self.name
        for item in super(YList, self).__getslice__(i, j):
            ret.append(item)
        return ret

    def append(self, item):
        super(YList, self).append(item)
        item.parent = self.parent
        if hasattr(item, 'ylist_key_names') and not item.ylist_key_names:
            setattr(item, '_index', self.count)
            self.count += 1

    def extend(self, items):
        for item in items:
            self.append(item)


class YListItem(object):
    def __init__(self, item, parent, name):
        self.item = item
        self.parent = parent
        self.name = name
        self.ylist_key_names = []

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.item.__class__.__name__.endswith('Identity'):
                return self.item.__class__.__name__ == other.item.__class__.__name__
            else:
                return self.item == other.item
        else:
            return False

    def __repr__(self):
        return str(self.item)

    def _has_data(self):
        if hasattr(self.item, '_has_data'):
            return self.item._has_data()
        else:
            # Enum, Identity, Python primitive types.
            return True

    __hash__ = object.__hash__


class YLeafList(YList):
    """ Represents an associate list with support for hanging a parent

        Leaf-list in YANG use YLeafList to represetn the list.

        The "leaf-list" statement is used to define an
        array of a particular type.  The "leaf-list" statement takes one
        argument, which is an identifier, followed by a block of
        substatements that holds detailed leaf-list information. Values in
        leaf-list should be unique.
    """

    def __init__(self):
        super(YLeafList, self).__init__()

    def __contains__(self, item):
        item_to_compare = item
        if isinstance(item, YListItem):
            item_to_compare = item.item
        for i in super(YLeafList, self).__iter__():
            if item_to_compare.__class__.__name__.endswith('Identity'):
                if item_to_compare.__class__.__name__ == i.item.__class__.__name__:
                    return True
            else:
                if i.item == item_to_compare:
                    return True
        return False

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if len(self) != len(other):
                return False
            for item in super(YLeafList, self).__iter__():
                if not other.__contains__(item):
                    return False
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __len__(self):
        return super(YLeafList, self).__len__()

    def __setitem__(self, key, item):
        lst_item = YListItem(item, self.parent, self.name)
        super(YLeafList, self).__setitem__(key, lst_item)

    def __getitem__(self, key):
        if isinstance(key, slice):
            ret = YLeafList()
            ret.parent = self.parent
            ret.name = self.name
            start = 0 if not key.start else key.start
            step = 1 if not key.step else key.step
            stop = len(self) if not key.stop else key.stop
            for k in range(start, stop, step):
                ret.append(super(YLeafList, self).__getitem__(k))
        else:
            ret = super(YLeafList, self).__getitem__(key)
        return ret

    def __getslice__(self, i, j):
        # override __getslice__ implemented by CPython
        ret = YLeafList()
        ret.parent = self.parent
        ret.name = self.name
        for item in super(YLeafList, self).__getslice__(i, j):
            ret.append(item)
        return ret

    def append(self, item):
        if item in self:
            index = self.index(item)
            raise YPYModelError("Value {} already in leaf-list: {}".format(item, self[index].name))
        lst_item = YListItem(item, self.parent, self.name)
        super(YLeafList, self).append(lst_item)

    def extend(self, items):
        for item in items:
            self.append(item)

    def pop(self, i=-1):
        lst_item = super(YLeafList, self).pop(i)
        return lst_item.item

    def remove(self, item):
        removed = False
        for i in super(YLeafList, self).__iter__():
            if i.item == item:
                super(YLeafList, self).remove(i)
                removed = True
        if not removed:
            raise ValueError("list.remove(x): {} not in list".format(item))

    def insert(self, key, item):
        if item in self:
            index = self.index(item)
            raise YPYModelError("Value {} already in leaf-list: {}".format(item, self[index].name))
        lst_item = YListItem(item, self.parent, self.name)
        super(YLeafList, self).insert(key, lst_item)

    def index(self, item):
        idx = 0
        for i in super(YLeafList, self).__iter__():
            if i.item == item:
                return idx
            idx += 1
        raise ValueError("{} is not in leaf-list".format(item))

    def count(self, item):
        cnt = 0
        for i in super(YLeafList, self).__iter__():
            if i.item == item:
                cnt += 1
        return cnt


def get_segment_path(entity):
    path = entity._common_path.rsplit('/', 1)[1]
    if hasattr(entity, '_index'):
        path += '[%s]' % entity._index
    return path


def _absolute_path(entity):
    path = get_segment_path(entity)
    if hasattr(entity, 'parent') and entity.parent:
        path = '/'.join([_absolute_path(entity.parent), path])
    return path


def get_absolute_path(entity):
    path = _absolute_path(entity)
    segments = path.split("/")
    module = segments[0].split(':', 1)[0]
    for i in range(1, len(segments)):
        del_str = module + ':'
        if del_str in segments[i]:
            segments[i] = segments[i].replace(del_str, '')
        else:
            if ':' in segments[i]:
                module = segments[i].split(':', 1)[0]
    path = '/'.join(segments)
    return '/' + path


def get_name_leaf_data(entity):
    leaf_name_data = {}
    for member in entity._meta_info().meta_info_class_members:
        value = getattr(entity, member.presentation_name)
        if value is None or isinstance(value, list) and value == []:
            continue

        if member.mtype in [ATTRIBUTE, REFERENCE_IDENTITY_CLASS]:
            leaf_name_data[member.name] = value
        elif member.mtype == REFERENCE_LEAFLIST and isinstance(value, list):
            for child in value:
                key = "%s[.='%s']" % (member.name, child)
                leaf_name_data[key] = ''
    return leaf_name_data


def get_children(entity):
    children = {}
    for member in entity._meta_info().meta_info_class_members:
        value = getattr(entity, member.presentation_name)
        if value is None or isinstance(value, list) and value == []:
            continue

        if member.mtype == REFERENCE_CLASS:
            abs_path = get_absolute_path(value)
            children[abs_path] = value
        elif member.mtype == REFERENCE_LIST:
            for child in value:
                abs_path = get_absolute_path(child)
                children[abs_path] = child
    return children


def entity_to_dict(entity):
    edict = {}
    abs_path = get_absolute_path(entity)
    ent_meta = entity._meta_info()
    if (hasattr(ent_meta, 'is_presence') and ent_meta.is_presence) or \
            abs_path.endswith(']'):
        edict[abs_path] = ''
    leaf_name_data = get_name_leaf_data(entity)
    for leaf_name, leaf_value in leaf_name_data.items():
        if leaf_name not in entity.ylist_key_names:
            edict["%s/%s" % (abs_path, leaf_name)] = leaf_value
    for name, child in get_children(entity).items():
        child_dict = entity_to_dict(child)
        for n, v in child_dict.items():
            edict[n] = v
    return edict


def entity_diff(ent1, ent2):
    if ent1 is None or ent2 is None or type(ent1) != type(ent2):
        raise YPYError("entity_diff: Incompatible arguments provided.")

    diffs = {}
    ent1_dict = entity_to_dict(ent1)
    ent2_dict = entity_to_dict(ent2)
    ent1_keys = sorted(ent1_dict.keys())
    ent2_keys = sorted(ent2_dict.keys())
    ent1_skip_keys = []
    for key in ent1_keys:
        if key in ent1_skip_keys:
            continue
        if key in ent2_keys:
            if ent1_dict[key] != ent2_dict[key]:
                diffs[key] = (ent1_dict[key], ent2_dict[key])
            ent2_keys.remove(key)
        else:
            diffs[key] = (ent1_dict[key], None)
            for dup_key in ent1_keys:
                if dup_key.startswith(key):
                    ent1_skip_keys.append(dup_key)
    ent2_skip_keys = []
    for key in ent2_keys:
        if key in ent2_skip_keys:
            continue
        diffs[key] = (None, ent2_dict[key])
        for dup_key in ent2_keys:
            if dup_key.startswith(key):
                ent2_skip_keys.append(dup_key)
    return diffs


def abs_path_to_entity(entity, abs_path):
    top_abs_path = get_absolute_path(entity)
    if top_abs_path == abs_path:
        return entity

    if top_abs_path in abs_path:
        leaf_name_data = get_name_leaf_data(entity)
        for leaf_name in leaf_name_data:
            if leaf_name not in entity.ylist_key_names:
                leaf_path = "%s/%s" % (top_abs_path, leaf_name)
                if leaf_path == abs_path:
                    return entity

        for child_abs_path, child in get_children(entity).items():
            if child_abs_path == abs_path:
                return child
            matching_entity = abs_path_to_entity(child, abs_path)
            if matching_entity:
                return matching_entity
    return None
