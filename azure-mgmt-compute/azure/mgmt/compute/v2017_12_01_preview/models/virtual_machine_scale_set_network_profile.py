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


class VirtualMachineScaleSetNetworkProfile(Model):
    """Describes a virtual machine scale set network profile.

    :param health_probe: A reference to a load balancer probe used to
     determine the health of an instance in the virtual machine scale set. The
     reference will be in the form:
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/loadBalancers/{loadBalancerName}/probes/{probeName}'.
    :type health_probe:
     ~azure.mgmt.compute.v2017_12_01_preview.models.ApiEntityReference
    :param network_interface_configurations: The list of network
     configurations.
    :type network_interface_configurations:
     list[~azure.mgmt.compute.v2017_12_01_preview.models.VirtualMachineScaleSetNetworkConfiguration]
    """

    _attribute_map = {
        'health_probe': {'key': 'healthProbe', 'type': 'ApiEntityReference'},
        'network_interface_configurations': {'key': 'networkInterfaceConfigurations', 'type': '[VirtualMachineScaleSetNetworkConfiguration]'},
    }

    def __init__(self, health_probe=None, network_interface_configurations=None):
        self.health_probe = health_probe
        self.network_interface_configurations = network_interface_configurations
