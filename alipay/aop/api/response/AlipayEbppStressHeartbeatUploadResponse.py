#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppStressHeartbeatUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppStressHeartbeatUploadResponse, self).__init__()
        self._next_status = None
        self._success = None

    @property
    def next_status(self):
        return self._next_status

    @next_status.setter
    def next_status(self, value):
        self._next_status = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppStressHeartbeatUploadResponse, self).parse_response_content(response_content)
        if 'next_status' in response:
            self.next_status = response['next_status']
        if 'success' in response:
            self.success = response['success']
