#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeCommercialOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeCommercialOrderQueryResponse, self).__init__()
        self._order_type = None
        self._pay_time = None
        self._pay_trade_no = None
        self._price_id = None
        self._product_id = None
        self._status = None
        self._total_amount = None

    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def pay_trade_no(self):
        return self._pay_trade_no

    @pay_trade_no.setter
    def pay_trade_no(self, value):
        self._pay_trade_no = value
    @property
    def price_id(self):
        return self._price_id

    @price_id.setter
    def price_id(self, value):
        self._price_id = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeCommercialOrderQueryResponse, self).parse_response_content(response_content)
        if 'order_type' in response:
            self.order_type = response['order_type']
        if 'pay_time' in response:
            self.pay_time = response['pay_time']
        if 'pay_trade_no' in response:
            self.pay_trade_no = response['pay_trade_no']
        if 'price_id' in response:
            self.price_id = response['price_id']
        if 'product_id' in response:
            self.product_id = response['product_id']
        if 'status' in response:
            self.status = response['status']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
