#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class SsdataDataserviceMetainfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(SsdataDataserviceMetainfoSyncResponse, self).__init__()
        self._is_sync_success = None
        self._sync_result = None

    @property
    def is_sync_success(self):
        return self._is_sync_success

    @is_sync_success.setter
    def is_sync_success(self, value):
        self._is_sync_success = value
    @property
    def sync_result(self):
        return self._sync_result

    @sync_result.setter
    def sync_result(self, value):
        self._sync_result = value

    def parse_response_content(self, response_content):
        response = super(SsdataDataserviceMetainfoSyncResponse, self).parse_response_content(response_content)
        if 'is_sync_success' in response:
            self.is_sync_success = response['is_sync_success']
        if 'sync_result' in response:
            self.sync_result = response['sync_result']
