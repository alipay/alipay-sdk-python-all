#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceCommonRelationcodeReceiveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCommonRelationcodeReceiveResponse, self).__init__()
        self._url_code = None

    @property
    def url_code(self):
        return self._url_code

    @url_code.setter
    def url_code(self, value):
        self._url_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCommonRelationcodeReceiveResponse, self).parse_response_content(response_content)
        if 'url_code' in response:
            self.url_code = response['url_code']
