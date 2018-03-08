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

from .resource import Resource


class CertificateContract(Resource):
    """Certificate details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type for API Management resource.
    :vartype type: str
    :param subject: Required. Subject attribute of the certificate.
    :type subject: str
    :param thumbprint: Required. Thumbprint of the certificate.
    :type thumbprint: str
    :param expiration_date: Required. Expiration date of the certificate. The
     date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified
     by the ISO 8601 standard.
    :type expiration_date: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'subject': {'required': True},
        'thumbprint': {'required': True},
        'expiration_date': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'subject': {'key': 'properties.subject', 'type': 'str'},
        'thumbprint': {'key': 'properties.thumbprint', 'type': 'str'},
        'expiration_date': {'key': 'properties.expirationDate', 'type': 'iso-8601'},
    }

    def __init__(self, *, subject: str, thumbprint: str, expiration_date, **kwargs) -> None:
        super(CertificateContract, self).__init__(, **kwargs)
        self.subject = subject
        self.thumbprint = thumbprint
        self.expiration_date = expiration_date
