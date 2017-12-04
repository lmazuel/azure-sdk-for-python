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


class CheckSkuAvailabilityResult(Model):
    """Check SKU availability result.

    :param kind: The Kind of the resource. Possible values include:
     'Academic', 'Bing.Autosuggest', 'Bing.Autosuggest.v7',
     'Bing.CustomSearch', 'Bing.Search', 'Bing.Search.v7', 'Bing.Speech',
     'Bing.SpellCheck', 'Bing.SpellCheck.v7', 'ComputerVision',
     'ContentModerator', 'CustomSpeech', 'Emotion', 'Face', 'LUIS',
     'Recommendations', 'SpeakerRecognition', 'Speech', 'SpeechTranslation',
     'TextAnalytics', 'TextTranslation', 'WebLM'
    :type kind: str or ~azure.mgmt.cognitiveservices.models.Kind
    :param type: The Type of the resource.
    :type type: str
    :param sku_name: The SKU of Cognitive Services account. Possible values
     include: 'F0', 'P0', 'P1', 'P2', 'S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6'
    :type sku_name: str or ~azure.mgmt.cognitiveservices.models.SkuName
    :param sku_available: Indicates the given SKU is available or not.
    :type sku_available: bool
    :param reason: Reason why the SKU is not available.
    :type reason: str
    :param message: Additional error message.
    :type message: str
    """

    _attribute_map = {
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'sku_name': {'key': 'skuName', 'type': 'str'},
        'sku_available': {'key': 'skuAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, kind=None, type=None, sku_name=None, sku_available=None, reason=None, message=None):
        self.kind = kind
        self.type = type
        self.sku_name = sku_name
        self.sku_available = sku_available
        self.reason = reason
        self.message = message
