﻿# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------
import unittest
import asyncio

from azure.mgmt.storage.v2017_06_01.storage_management_client_async import StorageManagementClientAsync
from azure.mgmt.storage.v2017_06_01 import models

from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer


class MgmtStorageTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtStorageTest, self).setUp()
        self.storage_client = self.create_mgmt_client(
            StorageManagementClientAsync
        )
        self.loop = asyncio.get_event_loop()

    def test_storage_usage_async(self):
        async def test_usages():
            return [obj async for obj in self.storage_client.usage.list()]
        future = test_usages()
        usages = self.loop.run_until_complete(future)
        # usages = []
        # async_iterator = self.storage_client.usage.list()
        # async for obj in async_iterator:
        #     usages.append(obj)        
        self.assertGreater(len(usages), 0)

    @ResourceGroupPreparer()
    def test_storage_accounts_async(self, resource_group, location):
        account_name = self.get_resource_name('pyarmstorage18')

        future = self.storage_client.storage_accounts.check_name_availability(
            account_name
        )
        result_check = self.loop.run_until_complete(future)
        self.assertTrue(result_check.name_available)
        self.assertFalse(result_check.reason)
        self.assertFalse(result_check.message)

        params_create = models.StorageAccountCreateParameters(
            sku=models.Sku(models.SkuName.standard_lrs),
            kind=models.Kind.storage,
            location=location,
        )
        future = self.storage_client.storage_accounts.create(
            resource_group.name,
            account_name,
            params_create,
        )
        result_create = self.loop.run_until_complete(future)
        self.loop.run_until_complete(result_create)
        storage_account = result_create.result()
        self.assertEqual(storage_account.name, account_name)

        future = self.storage_client.storage_accounts.get_properties(
            resource_group.name,
            account_name,
        )
        storage_account = self.loop.run_until_complete(future)
        self.assertEqual(storage_account.name, account_name)

        # result_list_keys = self.storage_client.storage_accounts.list_keys(
        #     resource_group.name,
        #     account_name,
        # )
        # keys = {v.key_name: (v.value, v.permissions) for v in result_list_keys.keys}
        # self.assertEqual(len(keys), 2)
        # self.assertGreater(len(keys['key1'][0]), 0)
        # self.assertGreater(len(keys['key1'][0]), 0)

        # result_regen_keys = self.storage_client.storage_accounts.regenerate_key(
        #     resource_group.name,
        #     account_name,
        #     "key1"
        # )
        # new_keys = {v.key_name: (v.value, v.permissions) for v in result_regen_keys.keys}
        # self.assertEqual(len(new_keys), 2)
        # self.assertNotEqual(
        #     new_keys['key1'][0],
        #     keys['key1'][0],
        # )
        # self.assertEqual(
        #     new_keys['key2'][0],
        #     keys['key2'][0],
        # )

        # result_list = self.storage_client.storage_accounts.list_by_resource_group(
        #     resource_group.name,
        # )
        # result_list = list(result_list)
        # self.assertGreater(len(result_list), 0)

        # result_list = self.storage_client.storage_accounts.list()
        # result_list = list(result_list)
        # self.assertGreater(len(result_list), 0)

        # storage_account = self.storage_client.storage_accounts.update(
        #     resource_group.name,
        #     account_name,
        #     models.StorageAccountUpdateParameters(
        #         sku=models.Sku(models.SkuName.standard_grs)
        #     )
        # )

        # should there be a test of the update operation?

        future = self.storage_client.storage_accounts.delete(
            resource_group.name,
            account_name,
        )
        self.loop.run_until_complete(future)

#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
