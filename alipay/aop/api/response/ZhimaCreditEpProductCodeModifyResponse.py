#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpProductCodeModifyResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpProductCodeModifyResponse, self).__init__()
        self._result = None
        self._result_info = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def result_info(self):
        return self._result_info

    @result_info.setter
    def result_info(self, value):
        self._result_info = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpProductCodeModifyResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'result_info' in response:
            self.result_info = response['result_info']
