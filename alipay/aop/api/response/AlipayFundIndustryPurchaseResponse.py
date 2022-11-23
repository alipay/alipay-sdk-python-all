#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundIndustryPurchaseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundIndustryPurchaseResponse, self).__init__()
        self._amount = None
        self._gmt_pay = None
        self._operation_id = None
        self._out_request_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def gmt_pay(self):
        return self._gmt_pay

    @gmt_pay.setter
    def gmt_pay(self, value):
        self._gmt_pay = value
    @property
    def operation_id(self):
        return self._operation_id

    @operation_id.setter
    def operation_id(self, value):
        self._operation_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundIndustryPurchaseResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'gmt_pay' in response:
            self.gmt_pay = response['gmt_pay']
        if 'operation_id' in response:
            self.operation_id = response['operation_id']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
