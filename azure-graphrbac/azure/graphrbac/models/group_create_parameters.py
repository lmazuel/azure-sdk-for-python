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


class GroupCreateParameters(Model):
    """Request parameters for creating a new group.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param display_name: Group display name
    :type display_name: str
    :ivar mail_enabled: Whether the group is mail-enabled. Must be false. This
     is because only pure security groups can be created using the Graph API.
     Default value: False .
    :vartype mail_enabled: bool
    :param mail_nickname: Mail nickname
    :type mail_nickname: str
    :ivar security_enabled: Whether the group is a security group. Must be
     true. This is because only pure security groups can be created using the
     Graph API. Default value: True .
    :vartype security_enabled: bool
    """

    _validation = {
        'display_name': {'required': True},
        'mail_enabled': {'required': True, 'constant': True},
        'mail_nickname': {'required': True},
        'security_enabled': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'mail_enabled': {'key': 'mailEnabled', 'type': 'bool'},
        'mail_nickname': {'key': 'mailNickname', 'type': 'str'},
        'security_enabled': {'key': 'securityEnabled', 'type': 'bool'},
    }

    mail_enabled = False

    security_enabled = True

    def __init__(self, display_name, mail_nickname, additional_properties=None):
        super(GroupCreateParameters, self).__init__()
        self.additional_properties = additional_properties
        self.display_name = display_name
        self.mail_nickname = mail_nickname
