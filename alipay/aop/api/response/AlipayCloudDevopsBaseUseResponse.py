#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudDevopsBaseUseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudDevopsBaseUseResponse, self).__init__()
        self._biz_msg = None
        self._biz_result = None
        self._biz_status = None
        self._biz_trace = None
        self._service_code = None

    @property
    def biz_msg(self):
        return self._biz_msg

    @biz_msg.setter
    def biz_msg(self, value):
        self._biz_msg = value
    @property
    def biz_result(self):
        return self._biz_result

    @biz_result.setter
    def biz_result(self, value):
        self._biz_result = value
    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value
    @property
    def biz_trace(self):
        return self._biz_trace

    @biz_trace.setter
    def biz_trace(self, value):
        self._biz_trace = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudDevopsBaseUseResponse, self).parse_response_content(response_content)
        if 'biz_msg' in response:
            self.biz_msg = response['biz_msg']
        if 'biz_result' in response:
            self.biz_result = response['biz_result']
        if 'biz_status' in response:
            self.biz_status = response['biz_status']
        if 'biz_trace' in response:
            self.biz_trace = response['biz_trace']
        if 'service_code' in response:
            self.service_code = response['service_code']
