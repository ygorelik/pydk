
from ydk._core._dm_meta_info import _MetaInfoEnum
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
