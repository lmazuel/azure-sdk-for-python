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


class ManagedIntegrationRuntimeNode(Model):
    """Properties of integration runtime node.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :ivar node_id: The managed integration runtime node id.
    :vartype node_id: str
    :ivar status: The managed integration runtime node status. Possible values
     include: 'Starting', 'Available', 'Recycling', 'Unavailable'
    :vartype status: str or
     ~azure.mgmt.datafactory.models.ManagedIntegrationRuntimeNodeStatus
    :param errors: The errors that occurred on this integration runtime node.
    :type errors:
     list[~azure.mgmt.datafactory.models.ManagedIntegrationRuntimeError]
    """

    _validation = {
        'node_id': {'readonly': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'node_id': {'key': 'nodeId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'errors': {'key': 'errors', 'type': '[ManagedIntegrationRuntimeError]'},
    }

    def __init__(self, *, additional_properties=None, errors=None, **kwargs) -> None:
        super(ManagedIntegrationRuntimeNode, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.node_id = None
        self.status = None
        self.errors = errors
