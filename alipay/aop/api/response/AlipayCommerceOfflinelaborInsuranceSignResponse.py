#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOfflinelaborInsuranceSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOfflinelaborInsuranceSignResponse, self).__init__()
        self._sign_page_url = None

    @property
    def sign_page_url(self):
        return self._sign_page_url

    @sign_page_url.setter
    def sign_page_url(self, value):
        self._sign_page_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOfflinelaborInsuranceSignResponse, self).parse_response_content(response_content)
        if 'sign_page_url' in response:
            self.sign_page_url = response['sign_page_url']
