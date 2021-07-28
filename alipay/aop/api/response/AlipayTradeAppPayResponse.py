#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeAppPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeAppPayResponse, self).__init__()
        self._credit_agreement_id = None
        self._credit_biz_order_id = None
        self._credit_pay_mode = None
        self._merchant_order_no = None
        self._out_trade_no = None
        self._seller_id = None
        self._total_amount = None
        self._trade_no = None

    @property
    def credit_agreement_id(self):
        return self._credit_agreement_id

    @credit_agreement_id.setter
    def credit_agreement_id(self, value):
        self._credit_agreement_id = value
    @property
    def credit_biz_order_id(self):
        return self._credit_biz_order_id

    @credit_biz_order_id.setter
    def credit_biz_order_id(self, value):
        self._credit_biz_order_id = value
    @property
    def credit_pay_mode(self):
        return self._credit_pay_mode

    @credit_pay_mode.setter
    def credit_pay_mode(self, value):
        self._credit_pay_mode = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
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
        response = super(AlipayTradeAppPayResponse, self).parse_response_content(response_content)
        if 'credit_agreement_id' in response:
            self.credit_agreement_id = response['credit_agreement_id']
        if 'credit_biz_order_id' in response:
            self.credit_biz_order_id = response['credit_biz_order_id']
        if 'credit_pay_mode' in response:
            self.credit_pay_mode = response['credit_pay_mode']
        if 'merchant_order_no' in response:
            self.merchant_order_no = response['merchant_order_no']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'seller_id' in response:
            self.seller_id = response['seller_id']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
