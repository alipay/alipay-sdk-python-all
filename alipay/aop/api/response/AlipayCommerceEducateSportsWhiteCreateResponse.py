#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateSportsWhiteCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSportsWhiteCreateResponse, self).__init__()
        self._white_code_list = None

    @property
    def white_code_list(self):
        return self._white_code_list

    @white_code_list.setter
    def white_code_list(self, value):
        if isinstance(value, list):
            self._white_code_list = list()
            for i in value:
                self._white_code_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSportsWhiteCreateResponse, self).parse_response_content(response_content)
        if 'white_code_list' in response:
            self.white_code_list = response['white_code_list']
