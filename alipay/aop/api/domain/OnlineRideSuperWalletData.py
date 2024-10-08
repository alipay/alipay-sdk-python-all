#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OnlineRideSuperWalletData(object):

    def __init__(self):
        self._has_remaining_balance = None
        self._super_wallet_status = None

    @property
    def has_remaining_balance(self):
        return self._has_remaining_balance

    @has_remaining_balance.setter
    def has_remaining_balance(self, value):
        self._has_remaining_balance = value
    @property
    def super_wallet_status(self):
        return self._super_wallet_status

    @super_wallet_status.setter
    def super_wallet_status(self, value):
        self._super_wallet_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.has_remaining_balance:
            if hasattr(self.has_remaining_balance, 'to_alipay_dict'):
                params['has_remaining_balance'] = self.has_remaining_balance.to_alipay_dict()
            else:
                params['has_remaining_balance'] = self.has_remaining_balance
        if self.super_wallet_status:
            if hasattr(self.super_wallet_status, 'to_alipay_dict'):
                params['super_wallet_status'] = self.super_wallet_status.to_alipay_dict()
            else:
                params['super_wallet_status'] = self.super_wallet_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OnlineRideSuperWalletData()
        if 'has_remaining_balance' in d:
            o.has_remaining_balance = d['has_remaining_balance']
        if 'super_wallet_status' in d:
            o.super_wallet_status = d['super_wallet_status']
        return o


