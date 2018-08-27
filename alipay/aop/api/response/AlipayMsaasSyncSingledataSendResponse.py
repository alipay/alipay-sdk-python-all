#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMsaasSyncSingledataSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasSyncSingledataSendResponse, self).__init__()
        self._oplog_id = None
        self._return_code = None
        self._return_reason = None
        self._success = None

    @property
    def oplog_id(self):
        return self._oplog_id

    @oplog_id.setter
    def oplog_id(self, value):
        self._oplog_id = value
    @property
    def return_code(self):
        return self._return_code

    @return_code.setter
    def return_code(self, value):
        self._return_code = value
    @property
    def return_reason(self):
        return self._return_reason

    @return_reason.setter
    def return_reason(self, value):
        self._return_reason = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayMsaasSyncSingledataSendResponse, self).parse_response_content(response_content)
        if 'oplog_id' in response:
            self.oplog_id = response['oplog_id']
        if 'return_code' in response:
            self.return_code = response['return_code']
        if 'return_reason' in response:
            self.return_reason = response['return_reason']
        if 'success' in response:
            self.success = response['success']
