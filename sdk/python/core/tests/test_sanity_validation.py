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

from __future__ import absolute_import
import ydk.types as ytypes
import unittest
import logging

from ydk.services import CRUDService
from ydk.models.ydktest import ydktest_sanity as ysanity
from ydk.models.ydktest import ydktest_sanity_types as ysanity_types
from ydk.providers import NetconfServiceProvider, NativeNetconfServiceProvider
from ydk.types import Empty, DELETE, Decimal64
from ydk.errors import YPYError, YPYModelError, YPYServiceError, YPYServiceProviderError

from ydk.models.ydktest.ydktest_sanity import YdkEnumTestEnum, YdkEnumIntTestEnum

def enable_logging(level):
    log = logging.getLogger('ydk')
    log.setLevel(level)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
    handler.setFormatter(formatter)
    log.addHandler(handler)

class SanityTest(unittest.TestCase):
    PROVIDER_TYPE = "non-native"

    @classmethod
    def setUpClass(self):
        if SanityTest.PROVIDER_TYPE == "native":
            self.ncc = NativeNetconfServiceProvider(address='127.0.0.1',
                                                    username='admin',
                                                    password='admin',
                                                    protocol='ssh',
                                                    port=12022)
        else:
            self.ncc = NetconfServiceProvider(address='127.0.0.1',
                                              username='admin',
                                              password='admin',
                                              protocol='ssh',
                                              port=12022)
        self.crud = CRUDService()

    @classmethod
    def tearDownClass(self):
        runner = ysanity.Runner()
        self.crud.delete(self.ncc, runner)
        self.ncc.close()

    def setUp(self):
        runner = ysanity.Runner()
        self.crud.delete(self.ncc, runner)

    def _create_runner(self):
        runner = ysanity.Runner()
        runner.ytypes = runner.Ytypes()
        runner.ytypes.built_in_t = runner.ytypes.BuiltInT()
        return runner

    def test_int8_invalid(self):
        try:
            runner = self._create_runner()
            runner.yvalidate = False
            runner.ytypes.built_in_t.number8 = 8.5
            self.crud.create(self.ncc, runner)
        except YPYServiceProviderError as err:
            expected_msg = '<error-message xml:lang="en">"8.5" is not a valid value.</error-message>'
            self.assertTrue(expected_msg in err.message)
        else:
            raise Exception('YPYServiceProviderError was not raised as expected')

    def test_uint_invalid(self):
        try:
            runner = self._create_runner()
            runner.ytypes.built_in_t.u_number8 = -1
            runner.ytypes.built_in_t.yvalidate = False
            self.crud.create(self.ncc, runner)
        except YPYServiceProviderError as err:
            expected_msg = '<error-message xml:lang="en">"-1" is not a valid value.</error-message>'
            self.assertTrue(expected_msg in err.message)
        else:
            raise Exception('YPYServiceProviderError was not raised as expected')

    def test_string_invalid(self):
        runner = self._create_runner()
        runner.ytypes.built_in_t.name = ['name_str']
        runner.ytypes.yvalidate = False
        self.crud.create(self.ncc, runner)

    def test_empty_invalid(self):
        try:
            runner = self._create_runner()
            runner.ytypes.built_in_t.emptee = 1
            runner.ytypes.built_in_t.yvalidate = False
            self.crud.create(self.ncc, runner)
        except YPYServiceProviderError as err:
            expected_msg = '<error-message xml:lang="en">got unexpected data "1" for a container</error-message>'
            self.assertTrue(expected_msg in err.message.strip())
        else:
            raise Exception('YPYServiceProviderError was not raised as expected')

    def test_enum_invalid(self):
        try:
            runner = self._create_runner()
            runner.ytypes.built_in_t.enum_value = 'not an enum'
            runner.ytypes.built_in_t.yvalidate = False
            self.crud.create(self.ncc, runner)
        except YPYServiceProviderError as err:
            expected_msg = '<error-message xml:lang="en">"" is an invalid value.</error-message><error-info><bad-element>enum-value</bad-element>'
            self.assertTrue(expected_msg in err.message)
        else:
            raise Exception('YPYServiceProviderError was not raised as expected')

    def test_enum_range_invalid(self):
        try:
            runner = self._create_runner()
            runner.ytypes.built_in_t.enum_int_value = 20000
            runner.ytypes.built_in_t.yvalidate = False
            self.crud.create(self.ncc, runner)
        except YPYServiceProviderError as err:
            expected_msg = '<error-message xml:lang="en">"20000" is not a valid value.</error-message>'
            self.assertTrue(expected_msg in err.message)
        except YPYError as err:
            raise Exception('Unexpected exception occured: %s' % err.message.strip())
        else:
            raise Exception('YPYServiceProviderError was not raised as expected')

    def test_str_pattern_invalid(self):
        try:
            one = ysanity.Runner.LeafRef.One()
            one.name_of_one = '1.2.3'
            one.yvalidate = False
            self.crud.create(self.ncc, one)
        except YPYServiceProviderError as err:
            expected_msg = '<error-message xml:lang="en">"1.2.3" is an invalid value.</error-message>'
            self.assertTrue(expected_msg in err.message)
        except YPYError as err:
            raise Exception('Unexpected exception occured: %s' % err.message.strip())
        else:
            raise Exception('YPYServiceProviderError was not raised as expected')
            
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        SanityTest.PROVIDER_TYPE = sys.argv.pop()
    enable_logging(logging.ERROR)
    suite = unittest.TestLoader().loadTestsFromTestCase(SanityTest)
    ret = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(ret)
