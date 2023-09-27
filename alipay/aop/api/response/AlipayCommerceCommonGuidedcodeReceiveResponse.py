#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceCommonGuidedcodeReceiveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCommonGuidedcodeReceiveResponse, self).__init__()
        self._guided_code = None
        self._guided_code_img = None
        self._guided_share_code = None

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
    @property
    def guided_share_code(self):
        return self._guided_share_code

    @guided_share_code.setter
    def guided_share_code(self, value):
        self._guided_share_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCommonGuidedcodeReceiveResponse, self).parse_response_content(response_content)
        if 'guided_code' in response:
            self.guided_code = response['guided_code']
        if 'guided_code_img' in response:
            self.guided_code_img = response['guided_code_img']
        if 'guided_share_code' in response:
            self.guided_share_code = response['guided_share_code']
