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

from .api_entity_base_contract import ApiEntityBaseContract


class ApiContractProperties(ApiEntityBaseContract):
    """Api Entity Properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param description: Description of the API. May include HTML formatting
     tags.
    :type description: str
    :param authentication_settings: Collection of authentication settings
     included into this API.
    :type authentication_settings:
     ~azure.mgmt.apimanagement.models.AuthenticationSettingsContract
    :param subscription_key_parameter_names: Protocols over which API is made
     available.
    :type subscription_key_parameter_names:
     ~azure.mgmt.apimanagement.models.SubscriptionKeyParameterNamesContract
    :param api_type: Type of API. Possible values include: 'http', 'soap'
    :type api_type: str or ~azure.mgmt.apimanagement.models.ApiType
    :param api_revision: Describes the Revision of the Api. If no value is
     provided, default revision 1 is created
    :type api_revision: str
    :param api_version: Indicates the Version identifier of the API if the API
     is versioned
    :type api_version: str
    :ivar is_current: Indicates if API revision is current api revision.
    :vartype is_current: bool
    :ivar is_online: Indicates if API revision is accessible via the gateway.
    :vartype is_online: bool
    :param api_version_set_id: A resource identifier for the related
     ApiVersionSet.
    :type api_version_set_id: str
    :param display_name: API name.
    :type display_name: str
    :param service_url: Absolute URL of the backend service implementing this
     API.
    :type service_url: str
    :param path: Required. Relative URL uniquely identifying this API and all
     of its resource paths within the API Management service instance. It is
     appended to the API endpoint base URL specified during the service
     instance creation to form a public URL for this API.
    :type path: str
    :param protocols: Describes on which protocols the operations in this API
     can be invoked.
    :type protocols: list[str or ~azure.mgmt.apimanagement.models.Protocol]
    :param api_version_set:
    :type api_version_set:
     ~azure.mgmt.apimanagement.models.ApiVersionSetContractDetails
    """

    _validation = {
        'api_revision': {'max_length': 100, 'min_length': 1},
        'api_version': {'max_length': 100},
        'is_current': {'readonly': True},
        'is_online': {'readonly': True},
        'display_name': {'max_length': 300, 'min_length': 1},
        'service_url': {'max_length': 2000, 'min_length': 0},
        'path': {'required': True, 'max_length': 400, 'min_length': 0},
    }

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'authentication_settings': {'key': 'authenticationSettings', 'type': 'AuthenticationSettingsContract'},
        'subscription_key_parameter_names': {'key': 'subscriptionKeyParameterNames', 'type': 'SubscriptionKeyParameterNamesContract'},
        'api_type': {'key': 'type', 'type': 'str'},
        'api_revision': {'key': 'apiRevision', 'type': 'str'},
        'api_version': {'key': 'apiVersion', 'type': 'str'},
        'is_current': {'key': 'isCurrent', 'type': 'bool'},
        'is_online': {'key': 'isOnline', 'type': 'bool'},
        'api_version_set_id': {'key': 'apiVersionSetId', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'service_url': {'key': 'serviceUrl', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'protocols': {'key': 'protocols', 'type': '[Protocol]'},
        'api_version_set': {'key': 'apiVersionSet', 'type': 'ApiVersionSetContractDetails'},
    }

    def __init__(self, **kwargs):
        super(ApiContractProperties, self).__init__(**kwargs)
        self.display_name = kwargs.get('display_name', None)
        self.service_url = kwargs.get('service_url', None)
        self.path = kwargs.get('path', None)
        self.protocols = kwargs.get('protocols', None)
        self.api_version_set = kwargs.get('api_version_set', None)
