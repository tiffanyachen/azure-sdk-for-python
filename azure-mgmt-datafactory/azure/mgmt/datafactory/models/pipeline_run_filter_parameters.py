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


class PipelineRunFilterParameters(Model):
    """Query parameters for listing pipeline runs.

    All required parameters must be populated in order to send to Azure.

    :param continuation_token: The continuation token for getting the next
     page of results. Null for first page.
    :type continuation_token: str
    :param last_updated_after: Required. The time at or after which the
     pipeline run event was updated in 'ISO 8601' format.
    :type last_updated_after: datetime
    :param last_updated_before: Required. The time at or before which the
     pipeline run event was updated in 'ISO 8601' format.
    :type last_updated_before: datetime
    :param filters: List of filters.
    :type filters: list[~azure.mgmt.datafactory.models.PipelineRunQueryFilter]
    :param order_by: List of OrderBy option.
    :type order_by:
     list[~azure.mgmt.datafactory.models.PipelineRunQueryOrderBy]
    """

    _validation = {
        'last_updated_after': {'required': True},
        'last_updated_before': {'required': True},
    }

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'last_updated_after': {'key': 'lastUpdatedAfter', 'type': 'iso-8601'},
        'last_updated_before': {'key': 'lastUpdatedBefore', 'type': 'iso-8601'},
        'filters': {'key': 'filters', 'type': '[PipelineRunQueryFilter]'},
        'order_by': {'key': 'orderBy', 'type': '[PipelineRunQueryOrderBy]'},
    }

    def __init__(self, **kwargs):
        super(PipelineRunFilterParameters, self).__init__(**kwargs)
        self.continuation_token = kwargs.get('continuation_token', None)
        self.last_updated_after = kwargs.get('last_updated_after', None)
        self.last_updated_before = kwargs.get('last_updated_before', None)
        self.filters = kwargs.get('filters', None)
        self.order_by = kwargs.get('order_by', None)
