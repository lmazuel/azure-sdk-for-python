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
    :type depends_on:
     list[~azure.mgmt.resource.resources.v2017_05_10.models.BasicDependency]
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

    def __init__(self, **kwargs):
        super(Dependency, self).__init__(**kwargs)
        self.depends_on = kwargs.get('depends_on', None)
        self.id = kwargs.get('id', None)
        self.resource_type = kwargs.get('resource_type', None)
        self.resource_name = kwargs.get('resource_name', None)
