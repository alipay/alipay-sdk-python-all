#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcFundStrategyCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcFundStrategyCreateResponse, self).__init__()
        self._fund_account_id = None
        self._fund_account_type = None
        self._name = None
        self._strategy_id = None

    @property
    def fund_account_id(self):
        return self._fund_account_id

    @fund_account_id.setter
    def fund_account_id(self, value):
        self._fund_account_id = value
    @property
    def fund_account_type(self):
        return self._fund_account_type

    @fund_account_type.setter
    def fund_account_type(self, value):
        self._fund_account_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def strategy_id(self):
        return self._strategy_id

    @strategy_id.setter
    def strategy_id(self, value):
        self._strategy_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcFundStrategyCreateResponse, self).parse_response_content(response_content)
        if 'fund_account_id' in response:
            self.fund_account_id = response['fund_account_id']
        if 'fund_account_type' in response:
            self.fund_account_type = response['fund_account_type']
        if 'name' in response:
            self.name = response['name']
        if 'strategy_id' in response:
            self.strategy_id = response['strategy_id']
