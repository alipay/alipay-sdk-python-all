#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceYuntaskGuidedcodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceYuntaskGuidedcodeQueryResponse, self).__init__()
        self._guided_code = None

    @property
    def guided_code(self):
        return self._guided_code

    @guided_code.setter
    def guided_code(self, value):
        self._guided_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceYuntaskGuidedcodeQueryResponse, self).parse_response_content(response_content)
        if 'guided_code' in response:
            self.guided_code = response['guided_code']
