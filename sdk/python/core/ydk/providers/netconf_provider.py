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

""" providers.py

   Service Providers module. Current implementation supports the NetconfServiceProvider which
   uses ncclient (a Netconf client library) to provide CRUD services.

"""
import logging
from .provider import ServiceProvider
from ._provider_plugin import _ClientSPPlugin
from ._session_config import _SessionConfig
from ._ydk_types import _SessionTransportMode


class NetconfServiceProvider(ServiceProvider):
    """ NCClient based Netconf ServiceProvider

        Initialization parameter of NetconfServiceProvider

        kwargs:
            - address - The address of the netconf server
            - port  - The port to use default is 830
            - username - The name of the user
            - password - The password to use
            - protocol - one of either ssh or tcp
            - timeout  - Default to 60
    """

    def __init__(self, **kwargs):
        self.address = kwargs.get('address', '127.0.0.1')
        self.port = kwargs.get('port', 830)
        self.username = kwargs.get('username', 'admin')
        self.password = kwargs.get('password', 'admin')
        self.protocol = kwargs.get('protocol', 'ssh')
        self.timeout = kwargs.get('timeout', 60)
        self.key_filename = kwargs.get('key_filename', None)
        self.sp_instance = None
        self.with_defaults = kwargs.get('with_defaults', None)

        if self.protocol == 'tcp':
            self.session_config = _SessionConfig(
                                                 _SessionTransportMode.TCP,
                                                 self.address,
                                                 self.port,
                                                 self.username,
                                                 self.password,
                                                 self.key_filename)
        else:
            self.session_config = _SessionConfig(
                                           _SessionTransportMode.SSH,
                                           self.address,
                                           self.port,
                                           self.username,
                                           self.password,
                                           self.key_filename)

        self.netconf_sp_logger = logging.getLogger(__name__)
        self._connect()
        self.netconf_sp_logger.info('NetconfServiceProvider connected to %s:%s using %s'
                               % (self.address, self.port, self.protocol))

    def _connect(self):
        self.sp_instance = _ClientSPPlugin(self.timeout, use_native_client=False,
                                           onbox = (self.protocol == 'onbox'))

        self.sp_instance.connect(self.session_config)

    def close(self):
        """ Closes the netconf session """
        self.sp_instance.disconnect()
        if self.port is not None:
            self.netconf_sp_logger.info('NetconfServiceProvider disconnected from %s:%s using %s'
                                        % (self.address, self.port, self.protocol))
        else:
            self.netconf_sp_logger.info('NetconfServiceProvider disconnected from %s using %s'
                                        % (self.address, self.protocol))

    def encode(self, entity, operation, only_config=False):
        return self.sp_instance.encode(entity, operation, only_config)

    def decode(self, payload, read_filter):
        return self.sp_instance.decode(payload, read_filter)

    def execute(self, payload, operation):
        return self.sp_instance.execute_operation(payload, operation)

    def _get_capabilities(self):
        return self.sp_instance._get_capabilities()
