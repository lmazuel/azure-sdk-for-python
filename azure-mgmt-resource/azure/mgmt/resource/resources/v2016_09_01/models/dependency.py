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


class Dependency(Model):
    """Deployment dependency information.

    :param depends_on: The list of dependencies.
    :type depends_on: list of :class:`BasicDependency
     <azure.mgmt.resource.resources.v2016_09_01.models.BasicDependency>`
    :param id: The ID of the dependency.
    :type id: str
    :param resource_type: The dependency resource type.
    :type resource_type: str
    :param resource_name: The dependency resource name.
    :type resource_name: str
    """

    _attribute_map = {
        'depends_on': {'key': 'dependsOn', 'type': '[BasicDependency]'},
        'id': {'key': 'id', 'type': 'str'},
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'resource_name': {'key': 'resourceName', 'type': 'str'},
    }

    def __init__(self, depends_on=None, id=None, resource_type=None, resource_name=None):
        self.depends_on = depends_on
        self.id = id
        self.resource_type = resource_type
        self.resource_name = resource_name
