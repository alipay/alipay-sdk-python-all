#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AccountBalanceInfo import AccountBalanceInfo


class MybankEcnyWelfarewalletBalanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankEcnyWelfarewalletBalanceQueryResponse, self).__init__()
        self._account_balance_info_list = None
        self._wallet_balance = None
        self._wallet_id = None
        self._wallet_status = None

    @property
    def account_balance_info_list(self):
        return self._account_balance_info_list

    @account_balance_info_list.setter
    def account_balance_info_list(self, value):
        if isinstance(value, list):
            self._account_balance_info_list = list()
            for i in value:
                if isinstance(i, AccountBalanceInfo):
                    self._account_balance_info_list.append(i)
                else:
                    self._account_balance_info_list.append(AccountBalanceInfo.from_alipay_dict(i))
    @property
    def wallet_balance(self):
        return self._wallet_balance

    @wallet_balance.setter
    def wallet_balance(self, value):
        self._wallet_balance = value
    @property
    def wallet_id(self):
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, value):
        self._wallet_id = value
    @property
    def wallet_status(self):
        return self._wallet_status

    @wallet_status.setter
    def wallet_status(self, value):
        self._wallet_status = value

    def parse_response_content(self, response_content):
        response = super(MybankEcnyWelfarewalletBalanceQueryResponse, self).parse_response_content(response_content)
        if 'account_balance_info_list' in response:
            self.account_balance_info_list = response['account_balance_info_list']
        if 'wallet_balance' in response:
            self.wallet_balance = response['wallet_balance']
        if 'wallet_id' in response:
            self.wallet_id = response['wallet_id']
        if 'wallet_status' in response:
            self.wallet_status = response['wallet_status']
