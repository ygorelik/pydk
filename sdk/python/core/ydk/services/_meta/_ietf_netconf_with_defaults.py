
import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST, ANYXML_CLASS
from ydk._core._dm_meta_info import REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'WithDefaultsModeEnum' : _MetaInfoEnum('WithDefaultsModeEnum',
        'ydk.models.ydktest.ietf_netconf_with_defaults', 'WithDefaultsModeEnum',
        '''Possible modes to report default data.''',
        {
            'report-all':'report_all',
            'report-all-tagged':'report_all_tagged',
            'trim':'trim',
            'explicit':'explicit',
        }, 'ietf-netconf-with-defaults', _yang_ns._namespaces['ietf-netconf-with-defaults']),
}
