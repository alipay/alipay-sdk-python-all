#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsumeExtend(object):

    def __init__(self):
        self._mall_assign_store = None
        self._show_wallet_info_balance = None

    @property
    def mall_assign_store(self):
        return self._mall_assign_store

    @mall_assign_store.setter
    def mall_assign_store(self, value):
        self._mall_assign_store = value
    @property
    def show_wallet_info_balance(self):
        return self._show_wallet_info_balance

    @show_wallet_info_balance.setter
    def show_wallet_info_balance(self, value):
        self._show_wallet_info_balance = value


    def to_alipay_dict(self):
        params = dict()
        if self.mall_assign_store:
            if hasattr(self.mall_assign_store, 'to_alipay_dict'):
                params['mall_assign_store'] = self.mall_assign_store.to_alipay_dict()
            else:
                params['mall_assign_store'] = self.mall_assign_store
        if self.show_wallet_info_balance:
            if hasattr(self.show_wallet_info_balance, 'to_alipay_dict'):
                params['show_wallet_info_balance'] = self.show_wallet_info_balance.to_alipay_dict()
            else:
                params['show_wallet_info_balance'] = self.show_wallet_info_balance
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsumeExtend()
        if 'mall_assign_store' in d:
            o.mall_assign_store = d['mall_assign_store']
        if 'show_wallet_info_balance' in d:
            o.show_wallet_info_balance = d['show_wallet_info_balance']
        return o


