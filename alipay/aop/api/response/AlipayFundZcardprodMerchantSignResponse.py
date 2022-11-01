#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundZcardprodMerchantSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundZcardprodMerchantSignResponse, self).__init__()
        self._account_id = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundZcardprodMerchantSignResponse, self).parse_response_content(response_content)
        if 'account_id' in response:
            self.account_id = response['account_id']
