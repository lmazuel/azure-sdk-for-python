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


class DataLakeAnalyticsAccountPropertiesBasic(Model):
    """The basic account specific properties that are associated with an
    underlying Data Lake Analytics account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provisioning_state: the provisioning status of the Data Lake
     Analytics account. Possible values include: 'Failed', 'Creating',
     'Running', 'Succeeded', 'Patching', 'Suspending', 'Resuming', 'Deleting',
     'Deleted', 'Undeleting', 'Canceled'
    :vartype provisioning_state: str or
     ~azure.mgmt.datalake.analytics.account.models.DataLakeAnalyticsAccountStatus
    :ivar state: the state of the Data Lake Analytics account. Possible values
     include: 'Active', 'Suspended'
    :vartype state: str or
     ~azure.mgmt.datalake.analytics.account.models.DataLakeAnalyticsAccountState
    :ivar creation_time: the account creation time.
    :vartype creation_time: datetime
    :ivar last_modified_time: the account last modified time.
    :vartype last_modified_time: datetime
    :ivar endpoint: the full CName endpoint for this account.
    :vartype endpoint: str
    :ivar account_id: The unique identifier associated with this Data Lake
     Analytics account.
    :vartype account_id: str
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'state': {'readonly': True},
        'creation_time': {'readonly': True},
        'last_modified_time': {'readonly': True},
        'endpoint': {'readonly': True},
        'account_id': {'readonly': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'DataLakeAnalyticsAccountStatus'},
        'state': {'key': 'state', 'type': 'DataLakeAnalyticsAccountState'},
        'creation_time': {'key': 'creationTime', 'type': 'iso-8601'},
        'last_modified_time': {'key': 'lastModifiedTime', 'type': 'iso-8601'},
        'endpoint': {'key': 'endpoint', 'type': 'str'},
        'account_id': {'key': 'accountId', 'type': 'str'},
    }

    def __init__(self):
        self.provisioning_state = None
        self.state = None
        self.creation_time = None
        self.last_modified_time = None
        self.endpoint = None
        self.account_id = None
