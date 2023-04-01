#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcServiceOrderBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcServiceOrderBindResponse, self).__init__()
        self._order_id = None
        self._sign_contract_url = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def sign_contract_url(self):
        return self._sign_contract_url

    @sign_contract_url.setter
    def sign_contract_url(self, value):
        self._sign_contract_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcServiceOrderBindResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'sign_contract_url' in response:
            self.sign_contract_url = response['sign_contract_url']
