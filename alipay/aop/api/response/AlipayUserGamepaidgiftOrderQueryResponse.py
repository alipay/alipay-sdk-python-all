#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserGamepaidgiftOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserGamepaidgiftOrderQueryResponse, self).__init__()
        self._bill_money = None
        self._paid_gift_id = None
        self._pay_time = None
        self._platform_order_id = None
        self._quantity = None
        self._refund_time = None
        self._role_id = None
        self._server_id = None
        self._status = None

    @property
    def bill_money(self):
        return self._bill_money

    @bill_money.setter
    def bill_money(self, value):
        self._bill_money = value
    @property
    def paid_gift_id(self):
        return self._paid_gift_id

    @paid_gift_id.setter
    def paid_gift_id(self, value):
        self._paid_gift_id = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def platform_order_id(self):
        return self._platform_order_id

    @platform_order_id.setter
    def platform_order_id(self, value):
        self._platform_order_id = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def refund_time(self):
        return self._refund_time

    @refund_time.setter
    def refund_time(self, value):
        self._refund_time = value
    @property
    def role_id(self):
        return self._role_id

    @role_id.setter
    def role_id(self, value):
        self._role_id = value
    @property
    def server_id(self):
        return self._server_id

    @server_id.setter
    def server_id(self, value):
        self._server_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserGamepaidgiftOrderQueryResponse, self).parse_response_content(response_content)
        if 'bill_money' in response:
            self.bill_money = response['bill_money']
        if 'paid_gift_id' in response:
            self.paid_gift_id = response['paid_gift_id']
        if 'pay_time' in response:
            self.pay_time = response['pay_time']
        if 'platform_order_id' in response:
            self.platform_order_id = response['platform_order_id']
        if 'quantity' in response:
            self.quantity = response['quantity']
        if 'refund_time' in response:
            self.refund_time = response['refund_time']
        if 'role_id' in response:
            self.role_id = response['role_id']
        if 'server_id' in response:
            self.server_id = response['server_id']
        if 'status' in response:
            self.status = response['status']
