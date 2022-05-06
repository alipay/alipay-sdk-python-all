#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankPaymentTradeBusinessOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankPaymentTradeBusinessOrderQueryResponse, self).__init__()
        self._biz_scene = None
        self._currency_value = None
        self._order_no = None
        self._order_status = None
        self._out_trade_no = None
        self._pay_amt = None
        self._product_code = None
        self._refund_amt = None
        self._retry = None
        self._settle_amt = None
        self._trade_amt = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def currency_value(self):
        return self._currency_value

    @currency_value.setter
    def currency_value(self, value):
        self._currency_value = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pay_amt(self):
        return self._pay_amt

    @pay_amt.setter
    def pay_amt(self, value):
        self._pay_amt = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def refund_amt(self):
        return self._refund_amt

    @refund_amt.setter
    def refund_amt(self, value):
        self._refund_amt = value
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
    @property
    def settle_amt(self):
        return self._settle_amt

    @settle_amt.setter
    def settle_amt(self, value):
        self._settle_amt = value
    @property
    def trade_amt(self):
        return self._trade_amt

    @trade_amt.setter
    def trade_amt(self, value):
        self._trade_amt = value

    def parse_response_content(self, response_content):
        response = super(MybankPaymentTradeBusinessOrderQueryResponse, self).parse_response_content(response_content)
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'currency_value' in response:
            self.currency_value = response['currency_value']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'pay_amt' in response:
            self.pay_amt = response['pay_amt']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'refund_amt' in response:
            self.refund_amt = response['refund_amt']
        if 'retry' in response:
            self.retry = response['retry']
        if 'settle_amt' in response:
            self.settle_amt = response['settle_amt']
        if 'trade_amt' in response:
            self.trade_amt = response['trade_amt']
