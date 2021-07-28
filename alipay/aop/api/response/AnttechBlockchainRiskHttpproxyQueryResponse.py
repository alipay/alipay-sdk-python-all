#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainRiskHttpproxyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainRiskHttpproxyQueryResponse, self).__init__()
        self._response = None
        self._success = None
        self._unique_id = None

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        self._response = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainRiskHttpproxyQueryResponse, self).parse_response_content(response_content)
        if 'response' in response:
            self.response = response['response']
        if 'success' in response:
            self.success = response['success']
        if 'unique_id' in response:
            self.unique_id = response['unique_id']
