#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotContentSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotContentSyncResponse, self).__init__()
        self._message = None
        self._sync_result_code = None
        self._sync_token = None

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def sync_result_code(self):
        return self._sync_result_code

    @sync_result_code.setter
    def sync_result_code(self, value):
        self._sync_result_code = value
    @property
    def sync_token(self):
        return self._sync_token

    @sync_token.setter
    def sync_token(self, value):
        self._sync_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotContentSyncResponse, self).parse_response_content(response_content)
        if 'message' in response:
            self.message = response['message']
        if 'sync_result_code' in response:
            self.sync_result_code = response['sync_result_code']
        if 'sync_token' in response:
            self.sync_token = response['sync_token']
