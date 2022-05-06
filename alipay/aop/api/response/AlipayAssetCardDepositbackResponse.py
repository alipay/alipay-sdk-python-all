#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAssetCardDepositbackResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAssetCardDepositbackResponse, self).__init__()
        self._depositback_amount = None
        self._depositback_bill_no = None

    @property
    def depositback_amount(self):
        return self._depositback_amount

    @depositback_amount.setter
    def depositback_amount(self, value):
        self._depositback_amount = value
    @property
    def depositback_bill_no(self):
        return self._depositback_bill_no

    @depositback_bill_no.setter
    def depositback_bill_no(self, value):
        self._depositback_bill_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayAssetCardDepositbackResponse, self).parse_response_content(response_content)
        if 'depositback_amount' in response:
            self.depositback_amount = response['depositback_amount']
        if 'depositback_bill_no' in response:
            self.depositback_bill_no = response['depositback_bill_no']
