#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoRebateBalanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoRebateBalanceQueryResponse, self).__init__()
        self._item_id = None
        self._rebate_jfb = None
        self._rebate_rate = None
        self._registered = None
        self._sufficient_balance = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def rebate_jfb(self):
        return self._rebate_jfb

    @rebate_jfb.setter
    def rebate_jfb(self, value):
        self._rebate_jfb = value
    @property
    def rebate_rate(self):
        return self._rebate_rate

    @rebate_rate.setter
    def rebate_rate(self, value):
        self._rebate_rate = value
    @property
    def registered(self):
        return self._registered

    @registered.setter
    def registered(self, value):
        self._registered = value
    @property
    def sufficient_balance(self):
        return self._sufficient_balance

    @sufficient_balance.setter
    def sufficient_balance(self, value):
        self._sufficient_balance = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoRebateBalanceQueryResponse, self).parse_response_content(response_content)
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'rebate_jfb' in response:
            self.rebate_jfb = response['rebate_jfb']
        if 'rebate_rate' in response:
            self.rebate_rate = response['rebate_rate']
        if 'registered' in response:
            self.registered = response['registered']
        if 'sufficient_balance' in response:
            self.sufficient_balance = response['sufficient_balance']
