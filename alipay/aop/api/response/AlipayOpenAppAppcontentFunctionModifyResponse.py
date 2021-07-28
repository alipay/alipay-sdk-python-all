#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppAppcontentFunctionModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppAppcontentFunctionModifyResponse, self).__init__()
        self._service_code = None

    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppAppcontentFunctionModifyResponse, self).parse_response_content(response_content)
        if 'service_code' in response:
            self.service_code = response['service_code']
