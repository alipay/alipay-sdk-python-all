#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskVerifyidentityCommonQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskVerifyidentityCommonQueryResponse, self).__init__()
        self._data = None
        self._message = None
        self._success = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskVerifyidentityCommonQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'message' in response:
            self.message = response['message']
        if 'success' in response:
            self.success = response['success']
