#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceDataMonitordeviceQualitycenterModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceDataMonitordeviceQualitycenterModifyResponse, self).__init__()
        self._error_detail = None

    @property
    def error_detail(self):
        return self._error_detail

    @error_detail.setter
    def error_detail(self, value):
        self._error_detail = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceDataMonitordeviceQualitycenterModifyResponse, self).parse_response_content(response_content)
        if 'error_detail' in response:
            self.error_detail = response['error_detail']
