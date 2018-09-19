#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradePayConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradePayConsultResponse, self).__init__()
        self._extend_infos = None
        self._refer_result = None
        self._result_code = None
        self._result_msg = None

    @property
    def extend_infos(self):
        return self._extend_infos

    @extend_infos.setter
    def extend_infos(self, value):
        self._extend_infos = value
    @property
    def refer_result(self):
        return self._refer_result

    @refer_result.setter
    def refer_result(self, value):
        self._refer_result = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradePayConsultResponse, self).parse_response_content(response_content)
        if 'extend_infos' in response:
            self.extend_infos = response['extend_infos']
        if 'refer_result' in response:
            self.refer_result = response['refer_result']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
