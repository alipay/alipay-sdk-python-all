#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccountBalanceInfo(object):

    def __init__(self):
        self._rule_group_id = None
        self._welfare_asset_balance = None
        self._welfare_asset_id = None

    @property
    def rule_group_id(self):
        return self._rule_group_id

    @rule_group_id.setter
    def rule_group_id(self, value):
        self._rule_group_id = value
    @property
    def welfare_asset_balance(self):
        return self._welfare_asset_balance

    @welfare_asset_balance.setter
    def welfare_asset_balance(self, value):
        self._welfare_asset_balance = value
    @property
    def welfare_asset_id(self):
        return self._welfare_asset_id

    @welfare_asset_id.setter
    def welfare_asset_id(self, value):
        self._welfare_asset_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.rule_group_id:
            if hasattr(self.rule_group_id, 'to_alipay_dict'):
                params['rule_group_id'] = self.rule_group_id.to_alipay_dict()
            else:
                params['rule_group_id'] = self.rule_group_id
        if self.welfare_asset_balance:
            if hasattr(self.welfare_asset_balance, 'to_alipay_dict'):
                params['welfare_asset_balance'] = self.welfare_asset_balance.to_alipay_dict()
            else:
                params['welfare_asset_balance'] = self.welfare_asset_balance
        if self.welfare_asset_id:
            if hasattr(self.welfare_asset_id, 'to_alipay_dict'):
                params['welfare_asset_id'] = self.welfare_asset_id.to_alipay_dict()
            else:
                params['welfare_asset_id'] = self.welfare_asset_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccountBalanceInfo()
        if 'rule_group_id' in d:
            o.rule_group_id = d['rule_group_id']
        if 'welfare_asset_balance' in d:
            o.welfare_asset_balance = d['welfare_asset_balance']
        if 'welfare_asset_id' in d:
            o.welfare_asset_id = d['welfare_asset_id']
        return o


