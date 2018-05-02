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


class KeyPhraseBatchResult(Model):
    """KeyPhraseBatchResult.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar documents:
    :vartype documents:
     list[~azure.cognitiveservices.language.textanalytics.models.KeyPhraseBatchResultItem]
    :ivar errors:
    :vartype errors:
     list[~azure.cognitiveservices.language.textanalytics.models.ErrorRecord]
    """

    _validation = {
        'documents': {'readonly': True},
        'errors': {'readonly': True},
    }

    _attribute_map = {
        'documents': {'key': 'documents', 'type': '[KeyPhraseBatchResultItem]'},
        'errors': {'key': 'errors', 'type': '[ErrorRecord]'},
    }

    def __init__(self, **kwargs) -> None:
        super(KeyPhraseBatchResult, self).__init__(**kwargs)
        self.documents = None
        self.errors = None
