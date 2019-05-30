#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarParkingOrderPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarParkingOrderPayResponse, self).__init__()
        self._advance_amount = None
        self._alipay_repayment_url = None
        self._fund_bill_list = None
        self._gmt_payment = None
        self._out_trade_no = None
        self._total_fee = None
        self._trade_no = None
        self._user_id = None

    @property
    def advance_amount(self):
        return self._advance_amount

    @advance_amount.setter
    def advance_amount(self, value):
        self._advance_amount = value
    @property
    def alipay_repayment_url(self):
        return self._alipay_repayment_url

    @alipay_repayment_url.setter
    def alipay_repayment_url(self, value):
        self._alipay_repayment_url = value
    @property
    def fund_bill_list(self):
        return self._fund_bill_list

    @fund_bill_list.setter
    def fund_bill_list(self, value):
        self._fund_bill_list = value
    @property
    def gmt_payment(self):
        return self._gmt_payment

    @gmt_payment.setter
    def gmt_payment(self, value):
        self._gmt_payment = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def total_fee(self):
        return self._total_fee

    @total_fee.setter
    def total_fee(self, value):
        self._total_fee = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarParkingOrderPayResponse, self).parse_response_content(response_content)
        if 'advance_amount' in response:
            self.advance_amount = response['advance_amount']
        if 'alipay_repayment_url' in response:
            self.alipay_repayment_url = response['alipay_repayment_url']
        if 'fund_bill_list' in response:
            self.fund_bill_list = response['fund_bill_list']
        if 'gmt_payment' in response:
            self.gmt_payment = response['gmt_payment']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'total_fee' in response:
            self.total_fee = response['total_fee']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'user_id' in response:
            self.user_id = response['user_id']
