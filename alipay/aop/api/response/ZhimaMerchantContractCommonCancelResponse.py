#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantContractCommonCancelResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantContractCommonCancelResponse, self).__init__()
        self._biz_data = None
        self._biz_result = None
        self._result_code = None
        self._result_desc = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def biz_result(self):
        return self._biz_result

    @biz_result.setter
    def biz_result(self, value):
        self._biz_result = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_desc(self):
        return self._result_desc

    @result_desc.setter
    def result_desc(self, value):
        self._result_desc = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantContractCommonCancelResponse, self).parse_response_content(response_content)
        if 'biz_data' in response:
            self.biz_data = response['biz_data']
        if 'biz_result' in response:
            self.biz_result = response['biz_result']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_desc' in response:
            self.result_desc = response['result_desc']
