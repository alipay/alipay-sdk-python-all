#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerversionDevicegrayModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerversionDevicegrayModifyResponse, self).__init__()
        self._gray_code = None

    @property
    def gray_code(self):
        return self._gray_code

    @gray_code.setter
    def gray_code(self, value):
        self._gray_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerversionDevicegrayModifyResponse, self).parse_response_content(response_content)
        if 'gray_code' in response:
            self.gray_code = response['gray_code']
