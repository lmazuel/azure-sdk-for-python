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


class CheckNameAvailabilityInput(Model):
    """Input of CheckNameAvailability API.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name: The resource name to validate.
    :type name: str
    :ivar type: The type of the resource whose name is to be validated.
     Default value: "Microsoft.Cdn/Profiles/Endpoints" .
    :vartype type: str
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    type = "Microsoft.Cdn/Profiles/Endpoints"

    def __init__(self, name):
        super(CheckNameAvailabilityInput, self).__init__()
        self.name = name
