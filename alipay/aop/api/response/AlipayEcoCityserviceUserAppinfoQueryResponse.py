#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoCityserviceUserAppinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCityserviceUserAppinfoQueryResponse, self).__init__()
        self._biz_type = None
        self._result_code = None
        self._result_context = None
        self._result_msg = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_context(self):
        return self._result_context

    @result_context.setter
    def result_context(self, value):
        self._result_context = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoCityserviceUserAppinfoQueryResponse, self).parse_response_content(response_content)
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_context' in response:
            self.result_context = response['result_context']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
