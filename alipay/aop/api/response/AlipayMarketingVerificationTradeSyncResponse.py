#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingVerificationTradeSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingVerificationTradeSyncResponse, self).__init__()
        self._operation_id = None
        self._request_id = None

    @property
    def operation_id(self):
        return self._operation_id

    @operation_id.setter
    def operation_id(self, value):
        self._operation_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingVerificationTradeSyncResponse, self).parse_response_content(response_content)
        if 'operation_id' in response:
            self.operation_id = response['operation_id']
        if 'request_id' in response:
            self.request_id = response['request_id']
