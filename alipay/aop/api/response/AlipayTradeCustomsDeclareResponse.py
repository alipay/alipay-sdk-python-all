#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeCustomsDeclareResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeCustomsDeclareResponse, self).__init__()
        self._alipay_declare_no = None
        self._currency = None
        self._identity_check = None
        self._out_trade_no = None
        self._pay_code = None
        self._pay_transaction_id = None
        self._total_amount = None
        self._trade_no = None
        self._ver_dept = None

    @property
    def alipay_declare_no(self):
        return self._alipay_declare_no

    @alipay_declare_no.setter
    def alipay_declare_no(self, value):
        self._alipay_declare_no = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def identity_check(self):
        return self._identity_check

    @identity_check.setter
    def identity_check(self, value):
        self._identity_check = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pay_code(self):
        return self._pay_code

    @pay_code.setter
    def pay_code(self, value):
        self._pay_code = value
    @property
    def pay_transaction_id(self):
        return self._pay_transaction_id

    @pay_transaction_id.setter
    def pay_transaction_id(self, value):
        self._pay_transaction_id = value
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
    @property
    def ver_dept(self):
        return self._ver_dept

    @ver_dept.setter
    def ver_dept(self, value):
        self._ver_dept = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeCustomsDeclareResponse, self).parse_response_content(response_content)
        if 'alipay_declare_no' in response:
            self.alipay_declare_no = response['alipay_declare_no']
        if 'currency' in response:
            self.currency = response['currency']
        if 'identity_check' in response:
            self.identity_check = response['identity_check']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'pay_code' in response:
            self.pay_code = response['pay_code']
        if 'pay_transaction_id' in response:
            self.pay_transaction_id = response['pay_transaction_id']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'ver_dept' in response:
            self.ver_dept = response['ver_dept']
