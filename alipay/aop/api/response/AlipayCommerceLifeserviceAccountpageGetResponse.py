#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLifeserviceAccountpageGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLifeserviceAccountpageGetResponse, self).__init__()
        self._pay_url = None

    @property
    def pay_url(self):
        return self._pay_url

    @pay_url.setter
    def pay_url(self, value):
        self._pay_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLifeserviceAccountpageGetResponse, self).parse_response_content(response_content)
        if 'pay_url' in response:
            self.pay_url = response['pay_url']
