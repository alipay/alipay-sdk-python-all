#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeCreditPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeCreditPayResponse, self).__init__()
        self._buyer_user_id = None
        self._credit_biz_order_id = None
        self._gmt_payment = None
        self._open_id = None
        self._out_trade_no = None
        self._pre_auth_pay_amount = None
        self._total_amount = None
        self._trade_no = None

    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
    @property
    def credit_biz_order_id(self):
        return self._credit_biz_order_id

    @credit_biz_order_id.setter
    def credit_biz_order_id(self, value):
        self._credit_biz_order_id = value
    @property
    def gmt_payment(self):
        return self._gmt_payment

    @gmt_payment.setter
    def gmt_payment(self, value):
        self._gmt_payment = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pre_auth_pay_amount(self):
        return self._pre_auth_pay_amount

    @pre_auth_pay_amount.setter
    def pre_auth_pay_amount(self, value):
        self._pre_auth_pay_amount = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeCreditPayResponse, self).parse_response_content(response_content)
        if 'buyer_user_id' in response:
            self.buyer_user_id = response['buyer_user_id']
        if 'credit_biz_order_id' in response:
            self.credit_biz_order_id = response['credit_biz_order_id']
        if 'gmt_payment' in response:
            self.gmt_payment = response['gmt_payment']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'pre_auth_pay_amount' in response:
            self.pre_auth_pay_amount = response['pre_auth_pay_amount']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
