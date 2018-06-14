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


class AzureFunctionReceiver(Model):
    """An azure function receiver.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the azure function receiver. Names must
     be unique across all receivers within an action group.
    :type name: str
    :param function_app_resource_id: Required. The azure resource id of the
     function app.
    :type function_app_resource_id: str
    :param function_name: Required. The function name in the function app.
    :type function_name: str
    :param http_trigger_url: Required. The http trigger url where http request
     sent to.
    :type http_trigger_url: str
    """

    _validation = {
        'name': {'required': True},
        'function_app_resource_id': {'required': True},
        'function_name': {'required': True},
        'http_trigger_url': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'function_app_resource_id': {'key': 'functionAppResourceId', 'type': 'str'},
        'function_name': {'key': 'functionName', 'type': 'str'},
        'http_trigger_url': {'key': 'httpTriggerUrl', 'type': 'str'},
    }

    def __init__(self, *, name: str, function_app_resource_id: str, function_name: str, http_trigger_url: str, **kwargs) -> None:
        super(AzureFunctionReceiver, self).__init__(**kwargs)
        self.name = name
        self.function_app_resource_id = function_app_resource_id
        self.function_name = function_name
        self.http_trigger_url = http_trigger_url