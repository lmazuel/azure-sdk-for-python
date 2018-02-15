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

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.clusters_operations import ClustersOperations
from .operations.applications_operations import ApplicationsOperations
from .operations.location_operations import LocationOperations
from .operations.configurations_operations import ConfigurationsOperations
from .operations.extension_operations import ExtensionOperations
from .operations.script_actions_operations import ScriptActionsOperations
from .operations.script_execution_history_operations import ScriptExecutionHistoryOperations
from .operations.operations import Operations
from . import models


class HDInsightManagementClientConfiguration(AzureConfiguration):
    """Configuration for HDInsightManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription credentials which uniquely
     identify Microsoft Azure subscription. The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(HDInsightManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-hdinsight/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class HDInsightManagementClient(object):
    """HDInsight Management Client

    :ivar config: Configuration for client.
    :vartype config: HDInsightManagementClientConfiguration

    :ivar clusters: Clusters operations
    :vartype clusters: azure.mgmt.hdinsight.operations.ClustersOperations
    :ivar applications: Applications operations
    :vartype applications: azure.mgmt.hdinsight.operations.ApplicationsOperations
    :ivar location: Location operations
    :vartype location: azure.mgmt.hdinsight.operations.LocationOperations
    :ivar configurations: Configurations operations
    :vartype configurations: azure.mgmt.hdinsight.operations.ConfigurationsOperations
    :ivar extension: Extension operations
    :vartype extension: azure.mgmt.hdinsight.operations.ExtensionOperations
    :ivar script_actions: ScriptActions operations
    :vartype script_actions: azure.mgmt.hdinsight.operations.ScriptActionsOperations
    :ivar script_execution_history: ScriptExecutionHistory operations
    :vartype script_execution_history: azure.mgmt.hdinsight.operations.ScriptExecutionHistoryOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.hdinsight.operations.Operations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription credentials which uniquely
     identify Microsoft Azure subscription. The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = HDInsightManagementClientConfiguration(credentials, subscription_id, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2015-03-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.clusters = ClustersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.applications = ApplicationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.location = LocationOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.configurations = ConfigurationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.extension = ExtensionOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.script_actions = ScriptActionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.script_execution_history = ScriptExecutionHistoryOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
