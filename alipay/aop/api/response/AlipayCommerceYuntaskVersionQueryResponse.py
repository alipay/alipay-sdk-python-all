#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceYuntaskVersionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceYuntaskVersionQueryResponse, self).__init__()
        self._version_code = None

    @property
    def version_code(self):
        return self._version_code

    @version_code.setter
    def version_code(self, value):
        self._version_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceYuntaskVersionQueryResponse, self).parse_response_content(response_content)
        if 'version_code' in response:
            self.version_code = response['version_code']
