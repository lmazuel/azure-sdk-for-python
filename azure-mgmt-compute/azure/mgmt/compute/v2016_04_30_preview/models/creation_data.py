# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CreationData(Model):
    """Data used when creating a disk.

    :param create_option: Possible values include: 'Empty', 'Attach',
     'FromImage', 'Import', 'Copy', 'Restore'
    :type create_option: str or
     ~azure.mgmt.compute.v2016_04_30_preview.models.DiskCreateOption
    :param storage_account_id: If createOption is Import, the Azure Resource
     Manager identifier of the storage account containing the blob to import as
     a disk. Required only if the blob is in a different subscription
    :type storage_account_id: str
    :param image_reference: Disk source information.
    :type image_reference:
     ~azure.mgmt.compute.v2016_04_30_preview.models.ImageDiskReference
    :param source_uri: If createOption is Import, this is a SAS URI to a blob
     to be imported into a managed disk. If createOption is Copy, this is a
     relative Uri containing the id of the source snapshot to be copied into a
     managed disk.
    :type source_uri: str
    :param source_resource_id: If createOption is Copy, this is the ARM id of
     the source snapshot or disk. If createOption is Restore, this is the
     ARM-like id of the source disk restore point.
    :type source_resource_id: str
    """

    _validation = {
        'create_option': {'required': True},
    }

    _attribute_map = {
        'create_option': {'key': 'createOption', 'type': 'DiskCreateOption'},
        'storage_account_id': {'key': 'storageAccountId', 'type': 'str'},
        'image_reference': {'key': 'imageReference', 'type': 'ImageDiskReference'},
        'source_uri': {'key': 'sourceUri', 'type': 'str'},
        'source_resource_id': {'key': 'sourceResourceId', 'type': 'str'},
    }

    def __init__(self, create_option, storage_account_id=None, image_reference=None, source_uri=None, source_resource_id=None):
        self.create_option = create_option
        self.storage_account_id = storage_account_id
        self.image_reference = image_reference
        self.source_uri = source_uri
        self.source_resource_id = source_resource_id
