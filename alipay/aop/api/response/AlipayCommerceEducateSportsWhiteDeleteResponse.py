#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateSportsWhiteDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSportsWhiteDeleteResponse, self).__init__()
        self._white_code = None

    @property
    def white_code(self):
        return self._white_code

    @white_code.setter
    def white_code(self, value):
        self._white_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSportsWhiteDeleteResponse, self).parse_response_content(response_content)
        if 'white_code' in response:
            self.white_code = response['white_code']
