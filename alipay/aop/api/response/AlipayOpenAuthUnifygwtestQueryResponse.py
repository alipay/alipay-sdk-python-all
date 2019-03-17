#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAuthUnifygwtestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAuthUnifygwtestQueryResponse, self).__init__()
        self._des = None

    @property
    def des(self):
        return self._des

    @des.setter
    def des(self, value):
        self._des = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAuthUnifygwtestQueryResponse, self).parse_response_content(response_content)
        if 'des' in response:
            self.des = response['des']
