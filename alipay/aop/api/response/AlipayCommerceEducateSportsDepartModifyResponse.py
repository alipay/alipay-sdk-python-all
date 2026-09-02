#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateSportsDepartModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSportsDepartModifyResponse, self).__init__()
        self._department_code = None

    @property
    def department_code(self):
        return self._department_code

    @department_code.setter
    def department_code(self, value):
        self._department_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSportsDepartModifyResponse, self).parse_response_content(response_content)
        if 'department_code' in response:
            self.department_code = response['department_code']
