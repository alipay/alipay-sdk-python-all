#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceAdDatasetSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdDatasetSyncResponse, self).__init__()
        self._data_id = None

    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdDatasetSyncResponse, self).parse_response_content(response_content)
        if 'data_id' in response:
            self.data_id = response['data_id']
