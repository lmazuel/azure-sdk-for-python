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

from .proxy_resource import ProxyResource


class CustomDomain(ProxyResource):
    """Friendly domain name mapping to the endpoint hostname that the customer
    provides for branding purposes, e.g. www.consoto.com.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param host_name: Required. The host name of the custom domain. Must be a
     domain name.
    :type host_name: str
    :ivar resource_state: Resource status of the custom domain. Possible
     values include: 'Creating', 'Active', 'Deleting'
    :vartype resource_state: str or
     ~azure.mgmt.cdn.models.CustomDomainResourceState
    :ivar custom_https_provisioning_state: Provisioning status of Custom Https
     of the custom domain. Possible values include: 'Enabling', 'Enabled',
     'Disabling', 'Disabled', 'Failed'
    :vartype custom_https_provisioning_state: str or
     ~azure.mgmt.cdn.models.CustomHttpsProvisioningState
    :ivar custom_https_provisioning_substate: Provisioning substate shows the
     progress of custom HTTPS enabling/disabling process step by step. Possible
     values include: 'SubmittingDomainControlValidationRequest',
     'PendingDomainControlValidationREquestApproval',
     'DomainControlValidationRequestApproved',
     'DomainControlValidationRequestRejected',
     'DomainControlValidationRequestTimedOut', 'IssuingCertificate',
     'DeployingCertificate', 'CertificateDeployed', 'DeletingCertificate',
     'CertificateDeleted'
    :vartype custom_https_provisioning_substate: str or
     ~azure.mgmt.cdn.models.CustomHttpsProvisioningSubstate
    :param validation_data: Special validation or data may be required when
     delivering CDN to some regions due to local compliance reasons. E.g. ICP
     license number of a custom domain is required to deliver content in China.
    :type validation_data: str
    :ivar provisioning_state: Provisioning status of the custom domain.
    :vartype provisioning_state: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'host_name': {'required': True},
        'resource_state': {'readonly': True},
        'custom_https_provisioning_state': {'readonly': True},
        'custom_https_provisioning_substate': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'host_name': {'key': 'properties.hostName', 'type': 'str'},
        'resource_state': {'key': 'properties.resourceState', 'type': 'str'},
        'custom_https_provisioning_state': {'key': 'properties.customHttpsProvisioningState', 'type': 'str'},
        'custom_https_provisioning_substate': {'key': 'properties.customHttpsProvisioningSubstate', 'type': 'str'},
        'validation_data': {'key': 'properties.validationData', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, host_name: str, validation_data: str=None, **kwargs) -> None:
        super(CustomDomain, self).__init__(, **kwargs)
        self.host_name = host_name
        self.resource_state = None
        self.custom_https_provisioning_state = None
        self.custom_https_provisioning_substate = None
        self.validation_data = validation_data
        self.provisioning_state = None
