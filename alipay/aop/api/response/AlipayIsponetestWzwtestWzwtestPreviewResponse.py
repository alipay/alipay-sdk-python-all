#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIsponetestWzwtestWzwtestPreviewResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIsponetestWzwtestWzwtestPreviewResponse, self).__init__()
        self._s = None

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, value):
        self._s = value

    def parse_response_content(self, response_content):
        response = super(AlipayIsponetestWzwtestWzwtestPreviewResponse, self).parse_response_content(response_content)
        if 's' in response:
            self.s = response['s']
