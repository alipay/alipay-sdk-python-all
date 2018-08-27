#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobileUrlDeviceverifyAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobileUrlDeviceverifyAddResponse, self).__init__()
        self._response = None

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        self._response = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobileUrlDeviceverifyAddResponse, self).parse_response_content(response_content)
        if 'response' in response:
            self.response = response['response']
