#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSubscriptionCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSubscriptionCreateResponse, self).__init__()
        self._alipay_jump_schema = None
        self._alipay_schema = None
        self._pay_amount = None
        self._subscription_id = None

    @property
    def alipay_jump_schema(self):
        return self._alipay_jump_schema

    @alipay_jump_schema.setter
    def alipay_jump_schema(self, value):
        self._alipay_jump_schema = value
    @property
    def alipay_schema(self):
        return self._alipay_schema

    @alipay_schema.setter
    def alipay_schema(self, value):
        self._alipay_schema = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def subscription_id(self):
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self._subscription_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSubscriptionCreateResponse, self).parse_response_content(response_content)
        if 'alipay_jump_schema' in response:
            self.alipay_jump_schema = response['alipay_jump_schema']
        if 'alipay_schema' in response:
            self.alipay_schema = response['alipay_schema']
        if 'pay_amount' in response:
            self.pay_amount = response['pay_amount']
        if 'subscription_id' in response:
            self.subscription_id = response['subscription_id']
