#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerZmcardScoreCertifyResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerZmcardScoreCertifyResponse, self).__init__()
        self._biz_code = None
        self._certify_result = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def certify_result(self):
        return self._certify_result

    @certify_result.setter
    def certify_result(self, value):
        self._certify_result = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerZmcardScoreCertifyResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'certify_result' in response:
            self.certify_result = response['certify_result']
