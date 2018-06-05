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

from .dataset_storage_format_py3 import DatasetStorageFormat


class ParquetFormat(DatasetStorageFormat):
    """The data stored in Parquet format.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param serializer: Serializer. Type: string (or Expression with resultType
     string).
    :type serializer: object
    :param deserializer: Deserializer. Type: string (or Expression with
     resultType string).
    :type deserializer: object
    :param type: Required. Constant filled by server.
    :type type: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'serializer': {'key': 'serializer', 'type': 'object'},
        'deserializer': {'key': 'deserializer', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, *, additional_properties=None, serializer=None, deserializer=None, **kwargs) -> None:
        super(ParquetFormat, self).__init__(additional_properties=additional_properties, serializer=serializer, deserializer=deserializer, **kwargs)
        self.type = 'ParquetFormat'
