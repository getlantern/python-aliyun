# -*- coding:utf-8 -*-
# Copyright 2014, Quixey Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

import datetime
import dateutil.parser
import mox
import time
import unittest

from aliyun.ecs import connection as ecs


class RegionTest(unittest.TestCase):

    def testEqual(self):
        region1 = ecs.Region('regionid1', 'regionname1')
        region2 = ecs.Region('regionid1', 'regionname1')
        self.assertEqual(region1, region2)

    def testIDNotEqual(self):
        region1 = ecs.Region('regionid1', 'regionname1')
        region2 = ecs.Region('regionid2', 'regionname1')
        self.assertNotEqual(region1, region2)

    def testNameNotEqual(self):
        region1 = ecs.Region('regionid1', 'regionname1')
        region2 = ecs.Region('regionid1', 'regionname2')
        self.assertNotEqual(region1, region2)

    def testRepr(self):
        region = ecs.Region('region', 'name')
        self.assertTrue(repr(region).startswith('<Region region (name) at '))


class InstanceTest(unittest.TestCase):

    def setUp(self):
        self.now = datetime.datetime.now()
        self.instance1 = ecs.Instance(
            'id',
            'name',
            'imageId',
            'regionId',
            'instanceType',
            'hostname',
            'status',
            ['sg1', 'sg2'],
            ['ip1', 'ip2'],
            ['ip3', 'ip4'],
            'accounting',
            1, 1, self.now, self.now, 'p',
            'desc', 'cluster', [], 'z')

    def testEqual(self):
        instance2 = ecs.Instance(
            'id',
            'name',
            'imageId',
            'regionId',
            'instanceType',
            'hostname',
            'status',
            ['sg1', 'sg2'],
            ['ip1', 'ip2'],
            ['ip3', 'ip4'],
            'accounting',
            1, 1, self.now, self.now, 'p',
            'desc', 'cluster', [], 'z')

        self.assertEqual(self.instance1, instance2)

    def testNotEqual(self):
        instance2 = ecs.Instance(
            'id',
            'name',
            'imageId',
            'regionId',
            'instanceType',
            'hostname2',
            'status',
            ['sg1', 'sg2'],
            ['ip1', 'ip2'],
            ['ip3', 'ip4'],
            'accounting',
            1, 1, self.now, self.now, 'p',
            'desc', 'cluster', [], 'z')

        self.assertNotEqual(self.instance1, instance2)

    def testRepr(self):
        self.assertTrue(repr(self.instance1).startswith('<Instance id at'))


class InstanceStatusTest(unittest.TestCase):

    def testEqual(self):
        is1 = ecs.InstanceStatus('i1', 'running')
        is2 = ecs.InstanceStatus('i1', 'running')
        self.assertEqual(is1, is2)

    def testNotEqual(self):
        is1 = ecs.InstanceStatus('i1', 'running')
        is2 = ecs.InstanceStatus('i1', 'stopped')
        self.assertNotEqual(is1, is2)

    def testRepr(self):
        is1 = ecs.InstanceStatus('i1', 'running')
        self.assertTrue(repr(is1).startswith('<InstanceId i1 is running at'))


class InstanceTypeTest(unittest.TestCase):

    def testEqual(self):
        t1 = ecs.InstanceType('t1', 4, 2)
        t2 = ecs.InstanceType('t1', 4, 2)
        self.assertEqual(t1, t2)

    def testNotEqual(self):
        t1 = ecs.InstanceType('t1', 4, 2)
        t2 = ecs.InstanceType('t1', 4, 3)
        self.assertNotEqual(t1, t2)

    def testRepr(self):
        t1 = ecs.InstanceType('t1', 4, 2)
        self.assertTrue(repr(t1).startswith('<InstanceType t1'))


class SnapshotTest(unittest.TestCase):

    def setUp(self):
        self.now = datetime.datetime.now()

    def testEqual(self):
        s1 = ecs.Snapshot('s1', 'sn', 100, self.now)
        s2 = ecs.Snapshot('s1', 'sn', 100, self.now)
        self.assertEqual(s1, s2)

    def testNotEqual(self):
        s1 = ecs.Snapshot('s1', 'sn', 100, self.now)
        s2 = ecs.Snapshot('s1', 'sn', 99, self.now)
        self.assertNotEqual(s1, s2)

    def testRepr(self):
        s1 = ecs.Snapshot('s1', 'sn', 100, self.now)
        self.assertTrue(repr(s1).startswith('<Snapshot s1 is 100% ready at'))


class AutoSnapshotPolicyTest(unittest.TestCase):

    def testEqual(self):
        asp1 = ecs.AutoSnapshotPolicy(False, 1, 1, False, False, 1, 1, False)
        asp2 = ecs.AutoSnapshotPolicy(False, 1, 1, False, False, 1, 1, False)
        self.assertEqual(asp1, asp2)

    def testNotEqual(self):
        asp1 = ecs.AutoSnapshotPolicy(False, 1, 1, False, False, 1, 1, False)
        asp2 = ecs.AutoSnapshotPolicy(True, 1, 1, False, False, 1, 1, False)
        self.assertNotEqual(asp1, asp2)

    def testRepr(self):
        asp = ecs.AutoSnapshotPolicy(False, 1, 1, False, False, 1, 1, False)
        self.assertTrue(repr(asp).startswith('<AutoSnapshotPolicy at'))


class AutoSnapshotExecutionStatusTest(unittest.TestCase):

    def testEqual(self):
        ases1 = ecs.AutoSnapshotExecutionStatus('system-status', 'data-status')
        ases2 = ecs.AutoSnapshotExecutionStatus('system-status', 'data-status')
        self.assertEqual(ases1, ases2)

    def testNotEqual(self):
        ases1 = ecs.AutoSnapshotExecutionStatus('system-status', 'data-status')
        ases2 = ecs.AutoSnapshotExecutionStatus('not-equal', 'data-status')
        self.assertNotEqual(ases1, ases2)

    def testRepr(self):
        ases = ecs.AutoSnapshotExecutionStatus('system-status', 'data-status')
        self.assertTrue(repr(ases).startswith('<AutoSnapshotExecutionStatus '))


class AutoSnapshotPolicyStatusTest(unittest.TestCase):

    def setUp(self):
        self.policy = ecs.AutoSnapshotPolicy(False, 1, 1, False, False, 1, 1, False)
        self.status = ecs.AutoSnapshotExecutionStatus('system-status', 'data-status')

    def testEqual(self):
        asps1 = ecs.AutoSnapshotPolicyStatus(self.status, self.policy)
        status2 = ecs.AutoSnapshotExecutionStatus('system-status', 'data-status')
        policy2 = ecs.AutoSnapshotPolicy(False, 1, 1, False, False, 1, 1, False)
        asps2 = ecs.AutoSnapshotPolicyStatus(status2, policy2)
        self.assertEqual(asps1, asps2)

    def testNotEqual(self):
        asps1 = ecs.AutoSnapshotPolicyStatus(self.status, self.policy)
        status2 = ecs.AutoSnapshotExecutionStatus('system-status', 'data-status')
        policy2 = ecs.AutoSnapshotPolicy(True, 1, 1, False, False, 1, 1, False)
        asps2 = ecs.AutoSnapshotPolicyStatus(status2, policy2)
        self.assertNotEqual(asps1, asps2)

    def testRepr(self):
        asps1 = ecs.AutoSnapshotPolicyStatus(self.status, self.policy)
        self.assertTrue(repr(asps1).startswith('<AutoSnapshotPolicyStatus at'))

class DiskTest(unittest.TestCase):

    def testEqual(self):
        d1 = ecs.Disk('d1', 'system', 'cloud', 5)
        d2 = ecs.Disk('d1', 'system', 'cloud', 5)
        self.assertEqual(d1, d2)

    def testNotEqual(self):
        d1 = ecs.Disk('d1', 'system', 'cloud', 5)
        d2 = ecs.Disk('d1', 'system', 'cloud', 6)
        self.assertNotEqual(d1, d2)

    def testRepr(self):
        d1 = ecs.Disk('d1', 'system', 'cloud', 5)
        self.assertTrue(
            repr(d1).startswith('<Disk d1 of type system is 5GB at'))


class DiskMappingTest(unittest.TestCase):

    def testEqual(self):
        dm1 = ecs.DiskMapping('category', 1)
        dm2 = ecs.DiskMapping('category', 1)
        self.assertEqual(dm1, dm2)

    def testNotEqual(self):
        dm1 = ecs.DiskMapping('category', 1)
        dm2 = ecs.DiskMapping('category', 2)
        self.assertNotEqual(dm1, dm2)

    def testRepr(self):
        dm = ecs.DiskMapping('category')
        self.assertTrue(repr(dm).startswith('<DiskMapping None type category'))


class ImageTest(unittest.TestCase):

    def testEqual(self):
        i1 = ecs.Image('i1', 'version', 'name', 'desc', 1, 'arch', 'owner', 'os')
        i2 = ecs.Image('i1', 'version', 'name', 'desc', 1, 'arch', 'owner', 'os')
        self.assertEqual(i1, i2)

    def testNotEqual(self):
        i1 = ecs.Image('i1', 'version', 'name', 'desc', 1, 'arch', 'owner', 'os')
        i2 = ecs.Image('i2', 'version', 'name', 'desc', 1, 'arch', 'owner', 'os')
        self.assertNotEqual(i1, i2)

    def testRepr(self):
        i1 = ecs.Image('i1', 'version', 'name', 'desc', 1, 'arch', 'owner', 'os')
        self.assertTrue(repr(i1).startswith(
            '<Image i1(desc) for platform os and arch arch'))


class SecurityGroupInfoTest(unittest.TestCase):

    def testEqual(self):
        sg1 = ecs.SecurityGroupInfo('sg1', 'desc')
        sg2 = ecs.SecurityGroupInfo('sg1', 'desc')
        self.assertEqual(sg1, sg2)

    def testNotEqual(self):
        sg1 = ecs.SecurityGroupInfo('sg1', 'desc')
        sg2 = ecs.SecurityGroupInfo('sg2', 'desc')
        self.assertNotEqual(sg1, sg2)

    def testRepr(self):
        sg1 = ecs.SecurityGroupInfo('sg1', 'desc1')
        self.assertTrue(repr(sg1).startswith('<SecurityGroupInfo sg1'))


class SecurityGroupPermission(unittest.TestCase):

    def testEqual(self):
        p1 = ecs.SecurityGroupPermission('TCP', '22/22', '1.1.1.1/32', None,
                                         'Accept', 'internet')
        p2 = ecs.SecurityGroupPermission('TCP', '22/22', '1.1.1.1/32', None,
                                         'Accept', 'internet')
        self.assertEqual(p1, p2)

    def testNotEqual(self):
        p1 = ecs.SecurityGroupPermission('TCP', '22/22', '1.1.1.1/32', None,
                                         'Accept', 'internet')
        p2 = ecs.SecurityGroupPermission('TCP', '22/22', '1.1.1.1/32', None,
                                         'Reject', 'internet')
        self.assertNotEqual(p1, p2)

    def testRepr(self):
        p1 = ecs.SecurityGroupPermission('TCP', '22/22', '1.1.1.1/32', None,
                                         'Accept', 'internet')
        self.assertTrue(repr(p1).startswith(
            '<SecurityGroupPermission Accept TCP 22/22 from 1.1.1.1/32 at'))


class SecurityGroupTest(unittest.TestCase):

    def testEqual(self):
        p1 = ecs.SecurityGroupPermission('TCP', '22/22', '1.1.1.1/32', None,
                                         'Accept', 'internet')
        p2 = ecs.SecurityGroupPermission('TCP', '22/22', '1.1.1.1/32', None,
                                         'Accept', 'internet')
        sg1 = ecs.SecurityGroup('r', 'sg1', 'd', [p1])
        sg2 = ecs.SecurityGroup('r', 'sg1', 'd', [p2])
        self.assertEqual(sg1, sg2)

    def testNotEqual(self):
        p1 = ecs.SecurityGroupPermission('TCP', '22/22', '1.1.1.1/32', None,
                                         'Accept', 'internet')
        p2 = ecs.SecurityGroupPermission('TCP', '22/22', '1.1.1.1/32', None,
                                         'Reject', 'internet')
        sg1 = ecs.SecurityGroup('r', 'sg1', 'd', [p1])
        sg2 = ecs.SecurityGroup('r', 'sg1', 'd', [p2])
        self.assertNotEqual(sg1, sg2)

    def testRepr(self):
        p1 = ecs.SecurityGroupPermission('TCP', '22/22', '1.1.1.1/32', None,
                                         'Accept', 'internet')
        sg1 = ecs.SecurityGroup('r', 'sg1', 'd', [p1])
        self.assertTrue(repr(sg1).startswith(
            '<SecurityGroup sg1, d at'))

class ZoneTest(unittest.TestCase):

    def testEqualSimple(self):
        z1 = ecs.Zone('id1', 'name1')
        z2 = ecs.Zone('id1', 'name1')
        self.assertEqual(z1, z2)

    def testEqualFull(self):
        z1 = ecs.Zone('id1', 'name1', ['resource1'], ['disktype1'])
        z2 = ecs.Zone('id1', 'name1', ['resource1'], ['disktype1'])
        self.assertEqual(z1, z2)

    def testNotEqual(self):
        z1 = ecs.Zone('id1', 'name1')
        z2 = ecs.Zone('id2', 'name2')
        self.assertNotEqual(z1, z2)

    def testNotEqualDeep(self):
        z1 = ecs.Zone('id1', 'name1', ['resource1'], ['disktype1'])
        z2 = ecs.Zone('id1', 'name1', ['resource2'], ['disktype2'])
        self.assertNotEqual(z1, z2)

    def testRepr(self):
        z = ecs.Zone('id', 'name')
        self.assertTrue(repr(z).startswith('<Zone id (name) at'))

    def testDiskSupported(self):
        z1 = ecs.Zone('id', 'name', ['resource1'], ['disktype1'])
        self.assertTrue(z1.disk_supported('disktype1'))

    def testResourceCreationSupported(self):
        z1 = ecs.Zone('id', 'name', ['resource1'], ['disktype1'])
        self.assertTrue(z1.resource_creation_supported('resource1'))
