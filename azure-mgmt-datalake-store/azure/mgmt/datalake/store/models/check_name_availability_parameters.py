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


class CheckNameAvailabilityParameters(Model):
    """Data Lake Store account name availability check parameters.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name: the Data Lake Store name to check availability for.
    :type name: str
    :ivar type: the Resource type. Note: This should not be set by the user,
     as the constant value is Microsoft.DataLakeStore/accounts. Default value:
     "Microsoft.DataLakeStore/accounts" .
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

    type = "Microsoft.DataLakeStore/accounts"

    def __init__(self, name):
        self.name = name
