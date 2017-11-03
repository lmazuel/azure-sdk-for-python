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

from .directory_object import DirectoryObject


class ADGroup(DirectoryObject):
    """Active Directory group information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar object_id: The object ID.
    :vartype object_id: str
    :ivar object_type: The object type.
    :vartype object_type: str
    :ivar deletion_timestamp: The time at which the directory object was
     deleted.
    :vartype deletion_timestamp: datetime
    :param display_name: The display name of the group.
    :type display_name: str
    :param security_enabled: Whether the group is security-enable.
    :type security_enabled: bool
    :param mail: The primary email address of the group.
    :type mail: str
    """

    _validation = {
        'object_id': {'readonly': True},
        'object_type': {'readonly': True},
        'deletion_timestamp': {'readonly': True},
    }

    _attribute_map = {
        'object_id': {'key': 'objectId', 'type': 'str'},
        'object_type': {'key': 'objectType', 'type': 'str'},
        'deletion_timestamp': {'key': 'deletionTimestamp', 'type': 'iso-8601'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'security_enabled': {'key': 'securityEnabled', 'type': 'bool'},
        'mail': {'key': 'mail', 'type': 'str'},
    }

    def __init__(self, display_name=None, security_enabled=None, mail=None):
        super(ADGroup, self).__init__()
        self.display_name = display_name
        self.security_enabled = security_enabled
        self.mail = mail
