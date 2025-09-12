#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryOfflinelaborProjectCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryOfflinelaborProjectCreateResponse, self).__init__()
        self._register_url = None

    @property
    def register_url(self):
        return self._register_url

    @register_url.setter
    def register_url(self, value):
        self._register_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryOfflinelaborProjectCreateResponse, self).parse_response_content(response_content)
        if 'register_url' in response:
            self.register_url = response['register_url']
