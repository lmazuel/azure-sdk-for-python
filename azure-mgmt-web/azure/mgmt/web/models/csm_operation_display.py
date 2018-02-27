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


class CsmOperationDisplay(Model):
    """Meta data about operation used for display in portal.

    :param provider:
    :type provider: str
    :param resource:
    :type resource: str
    :param operation:
    :type operation: str
    :param description:
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, provider=None, resource=None, operation=None, description=None):
        super(CsmOperationDisplay, self).__init__()
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description
