#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoBasicBizinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoBasicBizinfoQueryResponse, self).__init__()
        self._biz_inst = None
        self._biz_type = None
        self._data_code = None
        self._org_result_code = None
        self._org_result_msg = None
        self._result_code = None
        self._result_context = None
        self._result_msg = None

    @property
    def biz_inst(self):
        return self._biz_inst

    @biz_inst.setter
    def biz_inst(self, value):
        self._biz_inst = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def data_code(self):
        return self._data_code

    @data_code.setter
    def data_code(self, value):
        self._data_code = value
    @property
    def org_result_code(self):
        return self._org_result_code

    @org_result_code.setter
    def org_result_code(self, value):
        self._org_result_code = value
    @property
    def org_result_msg(self):
        return self._org_result_msg

    @org_result_msg.setter
    def org_result_msg(self, value):
        self._org_result_msg = value
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
        response = super(AlipayEcoBasicBizinfoQueryResponse, self).parse_response_content(response_content)
        if 'biz_inst' in response:
            self.biz_inst = response['biz_inst']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'data_code' in response:
            self.data_code = response['data_code']
        if 'org_result_code' in response:
            self.org_result_code = response['org_result_code']
        if 'org_result_msg' in response:
            self.org_result_msg = response['org_result_msg']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_context' in response:
            self.result_context = response['result_context']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
