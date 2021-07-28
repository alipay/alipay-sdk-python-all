#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandBenefitVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandBenefitVerifyResponse, self).__init__()
        self._biz_ext = None
        self._detail_msg = None
        self._error_code = None
        self._result = None

    @property
    def biz_ext(self):
        return self._biz_ext

    @biz_ext.setter
    def biz_ext(self, value):
        self._biz_ext = value
    @property
    def detail_msg(self):
        return self._detail_msg

    @detail_msg.setter
    def detail_msg(self, value):
        self._detail_msg = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandBenefitVerifyResponse, self).parse_response_content(response_content)
        if 'biz_ext' in response:
            self.biz_ext = response['biz_ext']
        if 'detail_msg' in response:
            self.detail_msg = response['detail_msg']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'result' in response:
            self.result = response['result']
