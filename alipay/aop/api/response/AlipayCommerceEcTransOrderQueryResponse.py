#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcTransOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcTransOrderQueryResponse, self).__init__()
        self._amount = None
        self._order_fee = None
        self._order_no = None
        self._out_biz_no = None
        self._pay_fund_order_id = None
        self._status = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def order_fee(self):
        return self._order_fee

    @order_fee.setter
    def order_fee(self, value):
        self._order_fee = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def pay_fund_order_id(self):
        return self._pay_fund_order_id

    @pay_fund_order_id.setter
    def pay_fund_order_id(self, value):
        self._pay_fund_order_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcTransOrderQueryResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'order_fee' in response:
            self.order_fee = response['order_fee']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'pay_fund_order_id' in response:
            self.pay_fund_order_id = response['pay_fund_order_id']
        if 'status' in response:
            self.status = response['status']
