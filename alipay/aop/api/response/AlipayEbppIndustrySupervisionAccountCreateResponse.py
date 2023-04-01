#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySupervisionAccountCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySupervisionAccountCreateResponse, self).__init__()
        self._merchant_account_no = None
        self._merchant_account_status = None

    @property
    def merchant_account_no(self):
        return self._merchant_account_no

    @merchant_account_no.setter
    def merchant_account_no(self, value):
        self._merchant_account_no = value
    @property
    def merchant_account_status(self):
        return self._merchant_account_status

    @merchant_account_status.setter
    def merchant_account_status(self, value):
        self._merchant_account_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySupervisionAccountCreateResponse, self).parse_response_content(response_content)
        if 'merchant_account_no' in response:
            self.merchant_account_no = response['merchant_account_no']
        if 'merchant_account_status' in response:
            self.merchant_account_status = response['merchant_account_status']
