#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRecycleMerchantassetPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleMerchantassetPayResponse, self).__init__()
        self._pay_link = None

    @property
    def pay_link(self):
        return self._pay_link

    @pay_link.setter
    def pay_link(self, value):
        self._pay_link = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleMerchantassetPayResponse, self).parse_response_content(response_content)
        if 'pay_link' in response:
            self.pay_link = response['pay_link']
