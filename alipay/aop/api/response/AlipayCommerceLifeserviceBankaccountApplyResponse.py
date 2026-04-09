#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLifeserviceBankaccountApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLifeserviceBankaccountApplyResponse, self).__init__()
        self._apply_url = None

    @property
    def apply_url(self):
        return self._apply_url

    @apply_url.setter
    def apply_url(self, value):
        self._apply_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLifeserviceBankaccountApplyResponse, self).parse_response_content(response_content)
        if 'apply_url' in response:
            self.apply_url = response['apply_url']
