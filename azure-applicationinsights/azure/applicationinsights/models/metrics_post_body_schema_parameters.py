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


class MetricsPostBodySchemaParameters(Model):
    """The parameters for a single metrics query.

    All required parameters must be populated in order to send to Azure.

    :param metric_id: Required. Possible values include: 'requests/count',
     'requests/duration', 'requests/failed', 'users/count',
     'users/authenticated', 'pageViews/count', 'pageViews/duration',
     'client/processingDuration', 'client/receiveDuration',
     'client/networkDuration', 'client/sendDuration', 'client/totalDuration',
     'dependencies/count', 'dependencies/failed', 'dependencies/duration',
     'exceptions/count', 'exceptions/browser', 'exceptions/server',
     'sessions/count', 'performanceCounters/requestExecutionTime',
     'performanceCounters/requestsPerSecond',
     'performanceCounters/requestsInQueue',
     'performanceCounters/memoryAvailableBytes',
     'performanceCounters/exceptionsPerSecond',
     'performanceCounters/processCpuPercentage',
     'performanceCounters/processIOBytesPerSecond',
     'performanceCounters/processPrivateBytes',
     'performanceCounters/processorCpuPercentage',
     'availabilityResults/availabilityPercentage',
     'availabilityResults/duration', 'billing/telemetryCount',
     'customEvents/count'
    :type metric_id: str or ~azure.applicationinsights.models.MetricId
    :param timespan:
    :type timespan: str
    :param aggregation:
    :type aggregation: list[str or
     ~azure.applicationinsights.models.MetricsAggregation]
    :param interval:
    :type interval: timedelta
    :param segment:
    :type segment: list[str or
     ~azure.applicationinsights.models.MetricsSegment]
    :param top:
    :type top: int
    :param orderby:
    :type orderby: str
    :param filter:
    :type filter: str
    """

    _validation = {
        'metric_id': {'required': True},
    }

    _attribute_map = {
        'metric_id': {'key': 'metricId', 'type': 'str'},
        'timespan': {'key': 'timespan', 'type': 'str'},
        'aggregation': {'key': 'aggregation', 'type': '[MetricsAggregation]'},
        'interval': {'key': 'interval', 'type': 'duration'},
        'segment': {'key': 'segment', 'type': '[str]'},
        'top': {'key': 'top', 'type': 'int'},
        'orderby': {'key': 'orderby', 'type': 'str'},
        'filter': {'key': 'filter', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(MetricsPostBodySchemaParameters, self).__init__(**kwargs)
        self.metric_id = kwargs.get('metric_id', None)
        self.timespan = kwargs.get('timespan', None)
        self.aggregation = kwargs.get('aggregation', None)
        self.interval = kwargs.get('interval', None)
        self.segment = kwargs.get('segment', None)
        self.top = kwargs.get('top', None)
        self.orderby = kwargs.get('orderby', None)
        self.filter = kwargs.get('filter', None)
