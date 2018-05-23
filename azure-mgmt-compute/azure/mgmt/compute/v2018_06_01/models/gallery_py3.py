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

from .resource_py3 import Resource


class Gallery(Resource):
    """Specifies information about the gallery that you want to create or update.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param description: The description of this gallery resource.
    :type description: str
    :param identifier:
    :type identifier: ~azure.mgmt.compute.v2018_06_01.models.GalleryIdentifier
    :ivar provisioning_state: The current state of the gallery. The
     provisioning state, which only appears in the response. Possible values
     include: 'Creating', 'Updating', 'Failed', 'Succeeded', 'Deleting',
     'Migrating'
    :vartype provisioning_state: str or
     ~azure.mgmt.compute.v2018_06_01.models.enum
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'identifier': {'key': 'properties.identifier', 'type': 'GalleryIdentifier'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, location: str, tags=None, description: str=None, identifier=None, **kwargs) -> None:
        super(Gallery, self).__init__(location=location, tags=tags, **kwargs)
        self.description = description
        self.identifier = identifier
        self.provisioning_state = None
