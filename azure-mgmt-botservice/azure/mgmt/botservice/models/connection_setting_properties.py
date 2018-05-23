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


class ConnectionSettingProperties(Model):
    """Properties for a Connection Setting Item.

    :param client_id: Client Id associated with the Connection Setting.
    :type client_id: str
    :param client_secret: Client Secret associated with the Connection Setting
    :type client_secret: str
    :param scopes: Scopes associated with the Connection Setting
    :type scopes: str
    :param service_provider_id: Service Provider Id associated with the
     Connection Setting
    :type service_provider_id: str
    :param service_provider_display_name: Service Provider Display Name
     associated with the Connection Setting
    :type service_provider_display_name: str
    :param parameters: Service Provider Parameters associated with the
     Connection Setting
    :type parameters:
     list[~azure.mgmt.botservice.models.ConnectionSettingParameter]
    """

    _attribute_map = {
        'client_id': {'key': 'clientId', 'type': 'str'},
        'client_secret': {'key': 'clientSecret', 'type': 'str'},
        'scopes': {'key': 'scopes', 'type': 'str'},
        'service_provider_id': {'key': 'serviceProviderId', 'type': 'str'},
        'service_provider_display_name': {'key': 'serviceProviderDisplayName', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '[ConnectionSettingParameter]'},
    }

    def __init__(self, **kwargs):
        super(ConnectionSettingProperties, self).__init__(**kwargs)
        self.client_id = kwargs.get('client_id', None)
        self.client_secret = kwargs.get('client_secret', None)
        self.scopes = kwargs.get('scopes', None)
        self.service_provider_id = kwargs.get('service_provider_id', None)
        self.service_provider_display_name = kwargs.get('service_provider_display_name', None)
        self.parameters = kwargs.get('parameters', None)