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


class RegionalReplicationStatus(Model):
    """This is the regional replication status.

    :param region: The region where the gallery image version is published to.
    :type region: str
    :param state: This is the regional replication state. Possible values
     include: 'Unknown', 'Replicating', 'Completed', 'Failed'
    :type state: str or
     ~azure.mgmt.compute.v2018_06_01.models.ReplicationState
    :param details: The details of the replication status.
    :type details: str
    :param progress: It indicates progress of the replication job.
    :type progress: int
    """

    _attribute_map = {
        'region': {'key': 'region', 'type': 'str'},
        'state': {'key': 'state', 'type': 'ReplicationState'},
        'details': {'key': 'details', 'type': 'str'},
        'progress': {'key': 'progress', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(RegionalReplicationStatus, self).__init__(**kwargs)
        self.region = kwargs.get('region', None)
        self.state = kwargs.get('state', None)
        self.details = kwargs.get('details', None)
        self.progress = kwargs.get('progress', None)
