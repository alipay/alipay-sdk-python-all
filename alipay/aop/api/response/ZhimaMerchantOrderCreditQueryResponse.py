#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantOrderCreditQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantOrderCreditQueryResponse, self).__init__()
        self._channel = None
        self._cost = None
        self._credit_amount = None
        self._deposit = None
        self._finish_time = None
        self._fund_type = None
        self._merchant_id = None
        self._order_time = None
        self._out_order_no = None
        self._status = None
        self._zm_order_no = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value
    @property
    def credit_amount(self):
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, value):
        self._credit_amount = value
    @property
    def deposit(self):
        return self._deposit

    @deposit.setter
    def deposit(self, value):
        self._deposit = value
    @property
    def finish_time(self):
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value):
        self._finish_time = value
    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def zm_order_no(self):
        return self._zm_order_no

    @zm_order_no.setter
    def zm_order_no(self, value):
        self._zm_order_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantOrderCreditQueryResponse, self).parse_response_content(response_content)
        if 'channel' in response:
            self.channel = response['channel']
        if 'cost' in response:
            self.cost = response['cost']
        if 'credit_amount' in response:
            self.credit_amount = response['credit_amount']
        if 'deposit' in response:
            self.deposit = response['deposit']
        if 'finish_time' in response:
            self.finish_time = response['finish_time']
        if 'fund_type' in response:
            self.fund_type = response['fund_type']
        if 'merchant_id' in response:
            self.merchant_id = response['merchant_id']
        if 'order_time' in response:
            self.order_time = response['order_time']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'status' in response:
            self.status = response['status']
        if 'zm_order_no' in response:
            self.zm_order_no = response['zm_order_no']
