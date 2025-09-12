#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanHonorBankcardtokenGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanHonorBankcardtokenGetResponse, self).__init__()
        self._api_token = None
        self._valid_time = None

    @property
    def api_token(self):
        return self._api_token

    @api_token.setter
    def api_token(self, value):
        self._api_token = value
    @property
    def valid_time(self):
        return self._valid_time

    @valid_time.setter
    def valid_time(self, value):
        self._valid_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanHonorBankcardtokenGetResponse, self).parse_response_content(response_content)
        if 'api_token' in response:
            self.api_token = response['api_token']
        if 'valid_time' in response:
            self.valid_time = response['valid_time']
