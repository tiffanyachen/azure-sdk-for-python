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

from .trigger_py3 import Trigger


class TumblingWindowTrigger(Trigger):
    """Trigger that schedules pipeline runs for all fixed time interval windows
    from a start time without gaps and also supports backfill scenarios (when
    start time is in the past).

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param description: Trigger description.
    :type description: str
    :ivar runtime_state: Indicates if trigger is running or not. Updated when
     Start/Stop APIs are called on the Trigger. Possible values include:
     'Started', 'Stopped', 'Disabled'
    :vartype runtime_state: str or
     ~azure.mgmt.datafactory.models.TriggerRuntimeState
    :param type: Required. Constant filled by server.
    :type type: str
    :param pipeline: Required. Pipeline for which runs are created when an
     event is fired for trigger window that is ready.
    :type pipeline: ~azure.mgmt.datafactory.models.TriggerPipelineReference
    :param frequency: Required. The frequency of the time windows. Possible
     values include: 'Minute', 'Hour'
    :type frequency: str or
     ~azure.mgmt.datafactory.models.TumblingWindowFrequency
    :param interval: Required. The interval of the time windows. The minimum
     interval allowed is 15 Minutes.
    :type interval: int
    :param start_time: Required. The start time for the time period for the
     trigger during which events are fired for windows that are ready. Only UTC
     time is currently supported.
    :type start_time: datetime
    :param end_time: The end time for the time period for the trigger during
     which events are fired for windows that are ready. Only UTC time is
     currently supported.
    :type end_time: datetime
    :param delay: Specifies how long the trigger waits past due time before
     triggering new run. It doesn't alter window start and end time. The
     default is 0. Type: string (or Expression with resultType string),
     pattern: ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type delay: object
    :param max_concurrency: Required. The max number of parallel time windows
     (ready for execution) for which a new run is triggered.
    :type max_concurrency: int
    :param retry_policy: Retry policy that will be applied for failed pipeline
     runs.
    :type retry_policy: ~azure.mgmt.datafactory.models.RetryPolicy
    :param depends_on: Tumbling window triggers that this trigger depends on.
    :type depends_on:
     list[~azure.mgmt.datafactory.models.TumblingWindowTriggerReference]
    """

    _validation = {
        'runtime_state': {'readonly': True},
        'type': {'required': True},
        'pipeline': {'required': True},
        'frequency': {'required': True},
        'interval': {'required': True},
        'start_time': {'required': True},
        'max_concurrency': {'required': True, 'maximum': 50, 'minimum': 1},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'description': {'key': 'description', 'type': 'str'},
        'runtime_state': {'key': 'runtimeState', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'pipeline': {'key': 'pipeline', 'type': 'TriggerPipelineReference'},
        'frequency': {'key': 'typeProperties.frequency', 'type': 'str'},
        'interval': {'key': 'typeProperties.interval', 'type': 'int'},
        'start_time': {'key': 'typeProperties.startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'typeProperties.endTime', 'type': 'iso-8601'},
        'delay': {'key': 'typeProperties.delay', 'type': 'object'},
        'max_concurrency': {'key': 'typeProperties.maxConcurrency', 'type': 'int'},
        'retry_policy': {'key': 'typeProperties.retryPolicy', 'type': 'RetryPolicy'},
        'depends_on': {'key': 'typeProperties.dependsOn', 'type': '[TumblingWindowTriggerReference]'},
    }

    def __init__(self, *, pipeline, frequency, interval: int, start_time, max_concurrency: int, additional_properties=None, description: str=None, end_time=None, delay=None, retry_policy=None, depends_on=None, **kwargs) -> None:
        super(TumblingWindowTrigger, self).__init__(additional_properties=additional_properties, description=description, **kwargs)
        self.pipeline = pipeline
        self.frequency = frequency
        self.interval = interval
        self.start_time = start_time
        self.end_time = end_time
        self.delay = delay
        self.max_concurrency = max_concurrency
        self.retry_policy = retry_policy
        self.depends_on = depends_on
        self.type = 'TumblingWindowTrigger'
