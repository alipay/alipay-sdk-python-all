#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandContractStatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandContractStatusQueryResponse, self).__init__()
        self._sign_result_desc = None
        self._sign_status = None

    @property
    def sign_result_desc(self):
        return self._sign_result_desc

    @sign_result_desc.setter
    def sign_result_desc(self, value):
        self._sign_result_desc = value
    @property
    def sign_status(self):
        return self._sign_status

    @sign_status.setter
    def sign_status(self, value):
        self._sign_status = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandContractStatusQueryResponse, self).parse_response_content(response_content)
        if 'sign_result_desc' in response:
            self.sign_result_desc = response['sign_result_desc']
        if 'sign_status' in response:
            self.sign_status = response['sign_status']
