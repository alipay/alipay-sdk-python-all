#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WalletUseRule import WalletUseRule


class AlipayFundWalletRuleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundWalletRuleQueryResponse, self).__init__()
        self._wallet_use_rule = None

    @property
    def wallet_use_rule(self):
        return self._wallet_use_rule

    @wallet_use_rule.setter
    def wallet_use_rule(self, value):
        if isinstance(value, WalletUseRule):
            self._wallet_use_rule = value
        else:
            self._wallet_use_rule = WalletUseRule.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayFundWalletRuleQueryResponse, self).parse_response_content(response_content)
        if 'wallet_use_rule' in response:
            self.wallet_use_rule = response['wallet_use_rule']
