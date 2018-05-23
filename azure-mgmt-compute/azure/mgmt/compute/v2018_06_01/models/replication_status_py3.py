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


class ReplicationStatus(Model):
    """This is the replication status of the gallery image version.

    :param aggregated_state: This is the aggregated replication status based
     on the regional replication status. Possible values include: 'Unknown',
     'InProgress', 'Completed', 'Failed'
    :type aggregated_state: str or
     ~azure.mgmt.compute.v2018_06_01.models.AggregatedReplicationState
    :param summary: This is a summary of replication status for each region.
    :type summary:
     list[~azure.mgmt.compute.v2018_06_01.models.RegionalReplicationStatus]
    """

    _attribute_map = {
        'aggregated_state': {'key': 'aggregatedState', 'type': 'AggregatedReplicationState'},
        'summary': {'key': 'summary', 'type': '[RegionalReplicationStatus]'},
    }

    def __init__(self, *, aggregated_state=None, summary=None, **kwargs) -> None:
        super(ReplicationStatus, self).__init__(**kwargs)
        self.aggregated_state = aggregated_state
        self.summary = summary
