#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialAntiepSceneSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntiepSceneSendResponse, self).__init__()
        self._biz_desc = None
        self._biz_result_code = None
        self._biz_retriable = None
        self._biz_success = None
        self._module_result_map = None

    @property
    def biz_desc(self):
        return self._biz_desc

    @biz_desc.setter
    def biz_desc(self, value):
        self._biz_desc = value
    @property
    def biz_result_code(self):
        return self._biz_result_code

    @biz_result_code.setter
    def biz_result_code(self, value):
        self._biz_result_code = value
    @property
    def biz_retriable(self):
        return self._biz_retriable

    @biz_retriable.setter
    def biz_retriable(self, value):
        self._biz_retriable = value
    @property
    def biz_success(self):
        return self._biz_success

    @biz_success.setter
    def biz_success(self, value):
        self._biz_success = value
    @property
    def module_result_map(self):
        return self._module_result_map

    @module_result_map.setter
    def module_result_map(self, value):
        self._module_result_map = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntiepSceneSendResponse, self).parse_response_content(response_content)
        if 'biz_desc' in response:
            self.biz_desc = response['biz_desc']
        if 'biz_result_code' in response:
            self.biz_result_code = response['biz_result_code']
        if 'biz_retriable' in response:
            self.biz_retriable = response['biz_retriable']
        if 'biz_success' in response:
            self.biz_success = response['biz_success']
        if 'module_result_map' in response:
            self.module_result_map = response['module_result_map']
