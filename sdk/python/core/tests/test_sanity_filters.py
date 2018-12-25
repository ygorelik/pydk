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

"""test_sanity_levels.py
sanity test for ydktest-sanity.yang
"""
from __future__ import absolute_import

import unittest
from compare import is_equal

try:
    from ydk.models.ydktest.ydktest_sanity import Runner, ChildIdentityIdentity, YdkEnumTestEnum
except:
    from ydk.models.ydktest.ydktest_sanity.runner.runner import Runner
    from ydk.models.ydktest.ydktest_sanity.ydktest_sanity import ChildIdentityIdentity, YdkEnumTestEnum
from ydk.providers import NetconfServiceProvider, NativeNetconfServiceProvider
from ydk.services import CRUDService
from ydk.types import READ, REPLACE, CREATE, MERGE, REMOVE

class SanityYang(unittest.TestCase):
    PROVIDER_TYPE = "non-native"

    @classmethod
    def setUpClass(self):
        if SanityYang.PROVIDER_TYPE == "native":
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
        runner = Runner()
        self.crud.delete(self.ncc, runner)
        self.ncc.close()

    def setUp(self):
        runner = Runner()
        self.crud.delete(self.ncc, runner)

    def test_read_on_ref_class(self):
        r_1 = Runner()
        r_1.one.number, r_1.one.name = 1, 'runner:one:name'
        self.crud.create(self.ncc, r_1)
        r_2 = Runner()

        r_2.one = READ()
        r_2 = self.crud.read(self.ncc, r_2)
        self.assertEqual(is_equal(r_1, r_2), True)

    def test_read_on_leaf(self):
        r_1 = Runner()
        r_1.one.number, r_1.one.name = 1, 'runner:one:name'
        self.crud.create(self.ncc, r_1)
        r_2 = Runner()
        r_2.one.number = READ()
        r_2 = self.crud.read(self.ncc, r_2)
        self.assertEqual(r_2.one.number, r_1.one.number)

        # this will also read r_2.one.name, not able to read only one of them
        r_2 = Runner()
        r_2.one.number = 1
        r_2 = self.crud.read(self.ncc, r_2)
        self.assertEqual(r_2.one.number, r_1.one.number)

        # no such value, will return empty data
        r_2 = Runner()
        r_2.one.number = 2
        r_2 = self.crud.read(self.ncc, r_2)
        self.assertNotEqual(r_2.one.number, r_1.one.number)

    def test_read_on_ref_enum_class(self):
        r_1 = Runner.Ytypes.BuiltInT()
        r_1.enum_value = YdkEnumTestEnum.local
        self.crud.create(self.ncc, r_1)

        r_2 = Runner.Ytypes.BuiltInT()
        r_2.enum_value = READ()
        r_2 = self.crud.read(self.ncc, r_2)
        self.assertEqual(is_equal(r_1, r_2), True)

        r_2 = Runner.Ytypes.BuiltInT()
        r_2.enum_value = YdkEnumTestEnum.local
        r_2 = self.crud.read(self.ncc, r_2)
        self.assertEqual(is_equal(r_1, r_2), True)

        # no such value, nothing returned
        r_2 = Runner.Ytypes.BuiltInT()
        r_2.enum_value = YdkEnumTestEnum.remote
        r_2 = self.crud.read(self.ncc, r_2)
        self.assertNotEqual(is_equal(r_1, r_2), True)

    def test_read_on_ref_list(self):
        r_1 = Runner.OneList()
        l_1, l_2 = Runner.OneList.Ldata(), Runner.OneList.Ldata()
        l_1.number, l_2.number = 1, 2
        r_1.ldata.extend([l_1, l_2])
        self.crud.create(self.ncc, r_1)

        r_2 = Runner.OneList()
        r_2.ldata = READ()
        r_2 = self.crud.read(self.ncc, r_2)

        self.assertEqual(is_equal(r_1, r_2), True)

    def test_read_on_list_with_key(self):
        r_1 = Runner.OneList()
        l_1, l_2 = Runner.OneList.Ldata(), Runner.OneList.Ldata()
        l_1.number, l_2.number = 1, 2
        r_1.ldata.extend([l_1, l_2])
        self.crud.create(self.ncc, r_1)

        r_2 = Runner.OneList()
        r_2.ldata.extend([l_1])
        r_2 = self.crud.read(self.ncc, r_2)

        r_3 = Runner.OneList()
        r_3.ldata.extend([l_1])
        self.assertEqual(is_equal(r_2, r_3), True)

    def test_read_on_leaflist(self):
        r_1 = Runner.Ytypes.BuiltInT()
        r_1.llstring.extend(['1', '2', '3'])
        self.crud.create(self.ncc, r_1)
        r_2 = Runner.Ytypes.BuiltInT()
        r_2.llstring.extend(['1', '2', '3'])
        runner_read = self.crud.read(self.ncc, r_2)

        self.assertEqual(is_equal(r_1, runner_read), True)

        r_2 = Runner.Ytypes.BuiltInT()
        # invalid input, user should use READ()
        # or the same data on device
        r_2.llstring.extend(['something else'])
        runner_read = self.crud.read(self.ncc, r_2)
        self.assertNotEqual(is_equal(r_1, runner_read), True)

    def test_read_on_identity_ref(self):
        r_1 = Runner.Ytypes.BuiltInT()
        r_1.identity_ref_value = ChildIdentityIdentity()
        self.crud.create(self.ncc, r_1)
        r_2 = Runner.Ytypes.BuiltInT()
        r_2.identity_ref_value = READ()
        r_2 = self.crud.read(self.ncc, r_2)
        self.assertEqual(is_equal(r_1, r_2), True)

        r_2 = Runner.Ytypes.BuiltInT()
        r_2.identity_ref_value = ChildIdentityIdentity()
        r_2 = self.crud.read(self.ncc, r_2)
        self.assertEqual(is_equal(r_1, r_2), True)

    def test_read_only_config(self):
        r_1 = Runner()
        r_1.one.number, r_1.one.name = 1, 'runner:one:name'
        self.crud.create(self.ncc, r_1)
        r_2, r_3 = Runner(), Runner()
        r_2.one.number, r_3.one.number = READ(), READ()

        r_2 = self.crud.read(self.ncc, r_2, only_config=True)
        r_3 = self.crud.read(self.ncc, r_3)
        # ysanity only have config data, ok to compare
        self.assertEqual(is_equal(r_2, r_3), True)

    def test_decoder(self):
        # send payload to device
        runner = Runner()
        element = Runner.OneList.Ldata()
        element.number = 5
        element.name = 'five'
        runner.one_list.ldata.append(element)

        self.crud.create(self.ncc, runner)

        self.crud.read(self.ncc, Runner.OneList.Ldata())

    def test_replace_on_leaf(self):
        one = Runner.One()
        one.number, one.name = 1, 'runner-one-name'
        self.crud.create(self.ncc, one)

        filter = Runner.One()
        filter.number = READ()
        r = self.crud.read(self.ncc, filter)
        self.assertEqual(r.number, one.number)

        # Replace leaf value and verify
        one = Runner.One()
        one.name = REPLACE('runner_one_name')
        one.number = MERGE(2)
        self.crud.update(self.ncc, one)

        filter = Runner.One()
        filter.name = READ()
        filter.number = READ()
        r = self.crud.read(self.ncc, filter)
        self.assertEqual(r.name, 'runner_one_name')
        self.assertEqual(r.number, 2)

        one = Runner.One()
        one.number = REMOVE()
        self.crud.update(self.ncc, one)

        one.number = CREATE(3)
        self.crud.update(self.ncc, one)

        r = self.crud.read(self.ncc, Runner.One())
        self.assertEqual(r.name, 'runner_one_name')
        self.assertEqual(r.number, 3)

    def test_replace_on_enum(self):
        # Create and verify
        btc = Runner.Ytypes.BuiltInT()
        btc.enum_value = YdkEnumTestEnum.local
        self.crud.create(self.ncc, btc)

        filter = Runner.Ytypes.BuiltInT()
        filter.enum_value = READ()
        r = self.crud.read(self.ncc, filter)
        self.assertTrue(is_equal(r, btc))

        # Replace and Verify
        btr = Runner.Ytypes.BuiltInT()
        btr.enum_value = REPLACE(YdkEnumTestEnum.remote)
        self.crud.update(self.ncc, btr)

        r = self.crud.read(self.ncc, filter)
        self.assertEqual(r.enum_value, YdkEnumTestEnum.remote)

    def test_create_identity_ref(self):
        # Create and Verify
        btc = Runner.Ytypes.BuiltInT()
        btc.identity_ref_value = CREATE(ChildIdentityIdentity())
        self.crud.update(self.ncc, btc)

        filter = Runner.Ytypes.BuiltInT()
        filter.identity_ref_value = READ()
        r = self.crud.read(self.ncc, filter)
        self.assertTrue(is_equal(r.identity_ref_value, ChildIdentityIdentity()))

    def test_replace_on_list(self):
        one_list = Runner.OneList()
        ld1, ld2 = Runner.OneList.Ldata(), Runner.OneList.Ldata()
        ld1.number, ld2.number = 1, 2
        one_list.ldata.extend([ld1, ld2])
        self.crud.create(self.ncc, one_list)

        filter = Runner.OneList.Ldata()
        filter.number = 2
        r = self.crud.read(self.ncc, filter)
        self.assertTrue(is_equal(r, ld2))

        # Merge and Verify
        one_merge = Runner.OneList()
        ld3 = Runner.OneList.Ldata()
        ld3.number = 3
        one_merge.ldata.append(ld3)

        one_merge.yfilter = MERGE()
        self.crud.update(self.ncc, one_merge)

        r = self.crud.read(self.ncc, Runner.OneList())
        self.assertEqual(len(r.ldata), 3)

        # Replace and Verify
        replace = Runner.OneList()
        replace.ldata.append(ld3)
        replace.yfilter = REPLACE()
        self.crud.update(self.ncc, replace)

        r = self.crud.read(self.ncc, Runner.OneList())
        self.assertEqual(len(r.ldata), 1)

    def test_replace_on_container(self):
        one = Runner.One()
        one.number, one.name = 1, 'runner-one-name'
        self.crud.create(self.ncc, one)

        filter = Runner.One()
        r = self.crud.read(self.ncc, filter)
        self.assertEqual(one.number, r.number)

        # Replace container value and verify
        one.yfilter = REPLACE()
        one.name = 'runner_one_name'
        one.number = 2
        self.crud.update(self.ncc, one)

        r = self.crud.read(self.ncc, filter)
        self.assertEqual(r.name, 'runner_one_name')
        self.assertEqual(r.number, 2)

        one.yfilter = REMOVE()
        self.crud.update(self.ncc, one)

        r = self.crud.read(self.ncc, Runner.One())
        self.assertIsNone(r.name)
        self.assertIsNone(r.number)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        SanityYang.PROVIDER_TYPE = sys.argv.pop()
    suite = unittest.TestLoader().loadTestsFromTestCase(SanityYang)
    ret = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(ret)
