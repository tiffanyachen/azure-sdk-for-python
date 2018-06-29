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


class IntegrationRuntimeNodeMonitoringData(Model):
    """Monitoring data for integration runtime node.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :ivar node_name: Name of the integration runtime node.
    :vartype node_name: str
    :ivar available_memory_in_mb: Available memory (MB) on the integration
     runtime node.
    :vartype available_memory_in_mb: int
    :ivar cpu_utilization: CPU percentage on the integration runtime node.
    :vartype cpu_utilization: float
    :ivar concurrent_jobs_limit: Maximum concurrent jobs on the integration
     runtime node.
    :vartype concurrent_jobs_limit: int
    :ivar concurrent_jobs_running: The number of jobs currently running on the
     integration runtime node.
    :vartype concurrent_jobs_running: int
    :ivar max_concurrent_jobs: The maximum concurrent jobs in this integration
     runtime.
    :vartype max_concurrent_jobs: int
    :ivar sent_bytes: Sent bytes on the integration runtime node.
    :vartype sent_bytes: float
    :ivar received_bytes: Received bytes on the integration runtime node.
    :vartype received_bytes: float
    """

    _validation = {
        'node_name': {'readonly': True},
        'available_memory_in_mb': {'readonly': True},
        'cpu_utilization': {'readonly': True},
        'concurrent_jobs_limit': {'readonly': True},
        'concurrent_jobs_running': {'readonly': True},
        'max_concurrent_jobs': {'readonly': True},
        'sent_bytes': {'readonly': True},
        'received_bytes': {'readonly': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'node_name': {'key': 'nodeName', 'type': 'str'},
        'available_memory_in_mb': {'key': 'availableMemoryInMB', 'type': 'int'},
        'cpu_utilization': {'key': 'cpuUtilization', 'type': 'float'},
        'concurrent_jobs_limit': {'key': 'concurrentJobsLimit', 'type': 'int'},
        'concurrent_jobs_running': {'key': 'concurrentJobsRunning', 'type': 'int'},
        'max_concurrent_jobs': {'key': 'maxConcurrentJobs', 'type': 'int'},
        'sent_bytes': {'key': 'sentBytes', 'type': 'float'},
        'received_bytes': {'key': 'receivedBytes', 'type': 'float'},
    }

    def __init__(self, *, additional_properties=None, **kwargs) -> None:
        super(IntegrationRuntimeNodeMonitoringData, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.node_name = None
        self.available_memory_in_mb = None
        self.cpu_utilization = None
        self.concurrent_jobs_limit = None
        self.concurrent_jobs_running = None
        self.max_concurrent_jobs = None
        self.sent_bytes = None
        self.received_bytes = None
