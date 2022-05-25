#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceYuntaskGuidedcodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceYuntaskGuidedcodeQueryResponse, self).__init__()
        self._guided_code = None
        self._guided_code_img = None

    @property
    def guided_code(self):
        return self._guided_code

    @guided_code.setter
    def guided_code(self, value):
        self._guided_code = value
    @property
    def guided_code_img(self):
        return self._guided_code_img

    @guided_code_img.setter
    def guided_code_img(self, value):
        self._guided_code_img = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceYuntaskGuidedcodeQueryResponse, self).parse_response_content(response_content)
        if 'guided_code' in response:
            self.guided_code = response['guided_code']
        if 'guided_code_img' in response:
            self.guided_code_img = response['guided_code_img']
