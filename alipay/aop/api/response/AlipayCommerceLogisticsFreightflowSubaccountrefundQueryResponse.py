#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsFreightflowSubaccountrefundQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsFreightflowSubaccountrefundQueryResponse, self).__init__()
        self._real_refund_amt = None
        self._real_refund_amt_currency_value = None
        self._refund_status = None

    @property
    def real_refund_amt(self):
        return self._real_refund_amt

    @real_refund_amt.setter
    def real_refund_amt(self, value):
        self._real_refund_amt = value
    @property
    def real_refund_amt_currency_value(self):
        return self._real_refund_amt_currency_value

    @real_refund_amt_currency_value.setter
    def real_refund_amt_currency_value(self, value):
        self._real_refund_amt_currency_value = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsFreightflowSubaccountrefundQueryResponse, self).parse_response_content(response_content)
        if 'real_refund_amt' in response:
            self.real_refund_amt = response['real_refund_amt']
        if 'real_refund_amt_currency_value' in response:
            self.real_refund_amt_currency_value = response['real_refund_amt_currency_value']
        if 'refund_status' in response:
            self.refund_status = response['refund_status']
