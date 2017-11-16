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


class LinuxConfiguration(Model):
    """Specifies the Linux operating system settings on the virtual machine.
    <br><br>For a list of supported Linux distributions, see [Linux on
    Azure-Endorsed
    Distributions](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-endorsed-distros?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json)
    <br><br> For running non-endorsed distributions, see [Information for
    Non-Endorsed
    Distributions](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-create-upload-generic?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json).

    :param disable_password_authentication: Specifies whether password
     authentication should be disabled.
    :type disable_password_authentication: bool
    :param ssh: Specifies the ssh key configuration for a Linux OS.
    :type ssh: ~azure.mgmt.compute.v2017_12_01_preview.models.SshConfiguration
    """

    _attribute_map = {
        'disable_password_authentication': {'key': 'disablePasswordAuthentication', 'type': 'bool'},
        'ssh': {'key': 'ssh', 'type': 'SshConfiguration'},
    }

    def __init__(self, disable_password_authentication=None, ssh=None):
        self.disable_password_authentication = disable_password_authentication
        self.ssh = ssh
