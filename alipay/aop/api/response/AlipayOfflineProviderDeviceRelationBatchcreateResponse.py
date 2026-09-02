#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderDeviceRelationBatchcreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderDeviceRelationBatchcreateResponse, self).__init__()
        self._insert_count = None
        self._update_count = None

    @property
    def insert_count(self):
        return self._insert_count

    @insert_count.setter
    def insert_count(self, value):
        self._insert_count = value
    @property
    def update_count(self):
        return self._update_count

    @update_count.setter
    def update_count(self, value):
        self._update_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderDeviceRelationBatchcreateResponse, self).parse_response_content(response_content)
        if 'insert_count' in response:
            self.insert_count = response['insert_count']
        if 'update_count' in response:
            self.update_count = response['update_count']
