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


class EventGridEvent(Model):
    """Properties of an event published to an Event Grid topic.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. An unique identifier for the event.
    :type id: str
    :param topic: The resource path of the event source.
    :type topic: str
    :param subject: Required. A resource path relative to the topic path.
    :type subject: str
    :param data: Required. Event data specific to the event type.
    :type data: object
    :param event_type: Required. The type of the event that occurred.
    :type event_type: str
    :param event_time: Required. The time (in UTC) the event was generated.
    :type event_time: datetime
    :ivar metadata_version: The schema version of the event metadata.
    :vartype metadata_version: str
    :param data_version: Required. The schema version of the data object.
    :type data_version: str
    """

    _validation = {
        'id': {'required': True},
        'subject': {'required': True},
        'data': {'required': True},
        'event_type': {'required': True},
        'event_time': {'required': True},
        'metadata_version': {'readonly': True},
        'data_version': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'topic': {'key': 'topic', 'type': 'str'},
        'subject': {'key': 'subject', 'type': 'str'},
        'data': {'key': 'data', 'type': 'object'},
        'event_type': {'key': 'eventType', 'type': 'str'},
        'event_time': {'key': 'eventTime', 'type': 'iso-8601'},
        'metadata_version': {'key': 'metadataVersion', 'type': 'str'},
        'data_version': {'key': 'dataVersion', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(EventGridEvent, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.topic = kwargs.get('topic', None)
        self.subject = kwargs.get('subject', None)
        self.data = kwargs.get('data', None)
        self.event_type = kwargs.get('event_type', None)
        self.event_time = kwargs.get('event_time', None)
        self.metadata_version = None
        self.data_version = kwargs.get('data_version', None)
