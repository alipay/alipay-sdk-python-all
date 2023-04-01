#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySupervisionAccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySupervisionAccountQueryResponse, self).__init__()
        self._account_balance = None
        self._masking_account_no = None
        self._merchant_account_status = None

    @property
    def account_balance(self):
        return self._account_balance

    @account_balance.setter
    def account_balance(self, value):
        self._account_balance = value
    @property
    def masking_account_no(self):
        return self._masking_account_no

    @masking_account_no.setter
    def masking_account_no(self, value):
        self._masking_account_no = value
    @property
    def merchant_account_status(self):
        return self._merchant_account_status

    @merchant_account_status.setter
    def merchant_account_status(self, value):
        self._merchant_account_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySupervisionAccountQueryResponse, self).parse_response_content(response_content)
        if 'account_balance' in response:
            self.account_balance = response['account_balance']
        if 'masking_account_no' in response:
            self.masking_account_no = response['masking_account_no']
        if 'merchant_account_status' in response:
            self.merchant_account_status = response['merchant_account_status']
