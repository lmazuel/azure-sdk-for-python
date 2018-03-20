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


class DeploymentExtended(Model):
    """Deployment information.

    All required parameters must be populated in order to send to Azure.

    :param id: The ID of the deployment.
    :type id: str
    :param name: Required. The name of the deployment.
    :type name: str
    :param properties: Deployment properties.
    :type properties:
     ~azure.mgmt.resource.resources.v2016_02_01.models.DeploymentPropertiesExtended
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'DeploymentPropertiesExtended'},
    }

    def __init__(self, *, name: str, id: str=None, properties=None, **kwargs) -> None:
        super(DeploymentExtended, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.properties = properties
