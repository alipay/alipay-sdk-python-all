#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeMerchantCreditInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeMerchantCreditInitializeResponse, self).__init__()
        self._credit_quota = None

    @property
    def credit_quota(self):
        return self._credit_quota

    @credit_quota.setter
    def credit_quota(self, value):
        self._credit_quota = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeMerchantCreditInitializeResponse, self).parse_response_content(response_content)
        if 'credit_quota' in response:
            self.credit_quota = response['credit_quota']
