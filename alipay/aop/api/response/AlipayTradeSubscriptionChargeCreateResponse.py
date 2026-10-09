#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSubscriptionChargeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSubscriptionChargeCreateResponse, self).__init__()
        self._cashier_url = None
        self._charge_mode = None
        self._current_period_end = None
        self._current_period_start = None
        self._item_id = None
        self._pay_amount = None
        self._payment_order_id = None
        self._payment_period_end = None
        self._payment_period_start = None
        self._subscription_id = None

    @property
    def cashier_url(self):
        return self._cashier_url

    @cashier_url.setter
    def cashier_url(self, value):
        self._cashier_url = value
    @property
    def charge_mode(self):
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, value):
        self._charge_mode = value
    @property
    def current_period_end(self):
        return self._current_period_end

    @current_period_end.setter
    def current_period_end(self, value):
        self._current_period_end = value
    @property
    def current_period_start(self):
        return self._current_period_start

    @current_period_start.setter
    def current_period_start(self, value):
        self._current_period_start = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def payment_order_id(self):
        return self._payment_order_id

    @payment_order_id.setter
    def payment_order_id(self, value):
        self._payment_order_id = value
    @property
    def payment_period_end(self):
        return self._payment_period_end

    @payment_period_end.setter
    def payment_period_end(self, value):
        self._payment_period_end = value
    @property
    def payment_period_start(self):
        return self._payment_period_start

    @payment_period_start.setter
    def payment_period_start(self, value):
        self._payment_period_start = value
    @property
    def subscription_id(self):
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self._subscription_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSubscriptionChargeCreateResponse, self).parse_response_content(response_content)
        if 'cashier_url' in response:
            self.cashier_url = response['cashier_url']
        if 'charge_mode' in response:
            self.charge_mode = response['charge_mode']
        if 'current_period_end' in response:
            self.current_period_end = response['current_period_end']
        if 'current_period_start' in response:
            self.current_period_start = response['current_period_start']
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'pay_amount' in response:
            self.pay_amount = response['pay_amount']
        if 'payment_order_id' in response:
            self.payment_order_id = response['payment_order_id']
        if 'payment_period_end' in response:
            self.payment_period_end = response['payment_period_end']
        if 'payment_period_start' in response:
            self.payment_period_start = response['payment_period_start']
        if 'subscription_id' in response:
            self.subscription_id = response['subscription_id']
