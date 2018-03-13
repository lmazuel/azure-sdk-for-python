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

from .tracked_resource import TrackedResource


class Profile(TrackedResource):
    """CDN profile is a logical grouping of endpoints that share the same
    settings, such as CDN provider and pricing tier.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param sku: Required. The pricing tier (defines a CDN provider, feature
     list and rate) of the CDN profile.
    :type sku: ~azure.mgmt.cdn.models.Sku
    :ivar resource_state: Resource status of the profile. Possible values
     include: 'Creating', 'Active', 'Deleting', 'Disabled'
    :vartype resource_state: str or
     ~azure.mgmt.cdn.models.ProfileResourceState
    :ivar provisioning_state: Provisioning status of the profile.
    :vartype provisioning_state: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'sku': {'required': True},
        'resource_state': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'resource_state': {'key': 'properties.resourceState', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, location: str, sku, tags=None, **kwargs) -> None:
        super(Profile, self).__init__(location=location, tags=tags, **kwargs)
        self.sku = sku
        self.resource_state = None
        self.provisioning_state = None
