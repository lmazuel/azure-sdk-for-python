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


class VaultSecretGroup(Model):
    """Describes a set of certificates which are all in the same Key Vault.

    :param source_vault: The relative URL of the Key Vault containing all of
     the certificates in VaultCertificates.
    :type source_vault:
     ~azure.mgmt.compute.v2017_12_01_preview.models.SubResource
    :param vault_certificates: The list of key vault references in SourceVault
     which contain certificates.
    :type vault_certificates:
     list[~azure.mgmt.compute.v2017_12_01_preview.models.VaultCertificate]
    """

    _attribute_map = {
        'source_vault': {'key': 'sourceVault', 'type': 'SubResource'},
        'vault_certificates': {'key': 'vaultCertificates', 'type': '[VaultCertificate]'},
    }

    def __init__(self, source_vault=None, vault_certificates=None):
        self.source_vault = source_vault
        self.vault_certificates = vault_certificates
