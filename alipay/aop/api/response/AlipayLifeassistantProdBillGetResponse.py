#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayLifeassistantProdBillGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayLifeassistantProdBillGetResponse, self).__init__()
        self._amount = None
        self._order_id = None
        self._order_item = None
        self._pay_time = None
        self._pay_type = None
        self._payee = None
        self._trade_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_item(self):
        return self._order_item

    @order_item.setter
    def order_item(self, value):
        self._order_item = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def payee(self):
        return self._payee

    @payee.setter
    def payee(self, value):
        self._payee = value
    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        self._trade_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayLifeassistantProdBillGetResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'order_item' in response:
            self.order_item = response['order_item']
        if 'pay_time' in response:
            self.pay_time = response['pay_time']
        if 'pay_type' in response:
            self.pay_type = response['pay_type']
        if 'payee' in response:
            self.payee = response['payee']
        if 'trade_type' in response:
            self.trade_type = response['trade_type']
