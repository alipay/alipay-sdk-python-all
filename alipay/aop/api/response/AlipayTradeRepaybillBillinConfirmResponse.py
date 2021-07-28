#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeRepaybillBillinConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeRepaybillBillinConfirmResponse, self).__init__()
        self._bill_amount = None
        self._bill_no = None
        self._bill_status = None

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def bill_status(self):
        return self._bill_status

    @bill_status.setter
    def bill_status(self, value):
        self._bill_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeRepaybillBillinConfirmResponse, self).parse_response_content(response_content)
        if 'bill_amount' in response:
            self.bill_amount = response['bill_amount']
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'bill_status' in response:
            self.bill_status = response['bill_status']
