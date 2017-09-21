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

from .proxy_only_resource import ProxyOnlyResource


class MSDeployStatus(ProxyOnlyResource):
    """MSDeploy ARM response.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar deployer: Username of deployer
    :vartype deployer: str
    :ivar provisioning_state: Provisioning state. Possible values include:
     'accepted', 'running', 'succeeded', 'failed', 'canceled'
    :vartype provisioning_state: str or :class:`MSDeployProvisioningState
     <azure.mgmt.web.models.MSDeployProvisioningState>`
    :ivar start_time: Start time of deploy operation
    :vartype start_time: datetime
    :ivar end_time: End time of deploy operation
    :vartype end_time: datetime
    :ivar complete: Whether the deployment operation has completed
    :vartype complete: bool
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'deployer': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
        'complete': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'deployer': {'key': 'properties.deployer', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'MSDeployProvisioningState'},
        'start_time': {'key': 'properties.startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'properties.endTime', 'type': 'iso-8601'},
        'complete': {'key': 'properties.complete', 'type': 'bool'},
    }

    def __init__(self, kind=None):
        super(MSDeployStatus, self).__init__(kind=kind)
        self.deployer = None
        self.provisioning_state = None
        self.start_time = None
        self.end_time = None
        self.complete = None
