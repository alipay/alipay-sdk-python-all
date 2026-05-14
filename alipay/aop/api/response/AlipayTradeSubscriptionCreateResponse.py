#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSubscriptionCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSubscriptionCreateResponse, self).__init__()
        self._alipay_jump_schema = None
        self._alipay_schema = None
        self._order_no = None
        self._pay_amount = None
        self._promotion_info = None
        self._subscription_id = None
        self._trial_end = None
        self._trial_start = None

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
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def promotion_info(self):
        return self._promotion_info

    @promotion_info.setter
    def promotion_info(self, value):
        self._promotion_info = value
    @property
    def subscription_id(self):
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self._subscription_id = value
    @property
    def trial_end(self):
        return self._trial_end

    @trial_end.setter
    def trial_end(self, value):
        self._trial_end = value
    @property
    def trial_start(self):
        return self._trial_start

    @trial_start.setter
    def trial_start(self, value):
        self._trial_start = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSubscriptionCreateResponse, self).parse_response_content(response_content)
        if 'alipay_jump_schema' in response:
            self.alipay_jump_schema = response['alipay_jump_schema']
        if 'alipay_schema' in response:
            self.alipay_schema = response['alipay_schema']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'pay_amount' in response:
            self.pay_amount = response['pay_amount']
        if 'promotion_info' in response:
            self.promotion_info = response['promotion_info']
        if 'subscription_id' in response:
            self.subscription_id = response['subscription_id']
        if 'trial_end' in response:
            self.trial_end = response['trial_end']
        if 'trial_start' in response:
            self.trial_start = response['trial_start']
