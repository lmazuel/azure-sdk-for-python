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


class CheckNameAvailabilityResponseBody(Model):
    """The response returned on a check bot name availability request by Bot
    Service Management.

    :param valid: boolean indicating whether the bot name is available for
     use.
    :type valid: bool
    :param message: description indicating why the bot name is invalid, if it
     is not available.
    :type message: str
    """

    _attribute_map = {
        'valid': {'key': 'valid', 'type': 'bool'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CheckNameAvailabilityResponseBody, self).__init__(**kwargs)
        self.valid = kwargs.get('valid', None)
        self.message = kwargs.get('message', None)
