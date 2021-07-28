#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinancialnetPromotionApplyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetPromotionApplyQueryResponse, self).__init__()
        self._loan_order_no = None
        self._sign_order_no = None
        self._trace_id = None

    @property
    def loan_order_no(self):
        return self._loan_order_no

    @loan_order_no.setter
    def loan_order_no(self, value):
        self._loan_order_no = value
    @property
    def sign_order_no(self):
        return self._sign_order_no

    @sign_order_no.setter
    def sign_order_no(self, value):
        self._sign_order_no = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetPromotionApplyQueryResponse, self).parse_response_content(response_content)
        if 'loan_order_no' in response:
            self.loan_order_no = response['loan_order_no']
        if 'sign_order_no' in response:
            self.sign_order_no = response['sign_order_no']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
