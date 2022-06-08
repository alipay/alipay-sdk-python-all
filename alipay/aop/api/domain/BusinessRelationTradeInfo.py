#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessRelationTradeInfo(object):

    def __init__(self):
        self._avg_trade_amount = None
        self._total_trade_amount = None
        self._trade_count = None
        self._user_count = None
        self._user_trade_amount = None

    @property
    def avg_trade_amount(self):
        return self._avg_trade_amount

    @avg_trade_amount.setter
    def avg_trade_amount(self, value):
        self._avg_trade_amount = value
    @property
    def total_trade_amount(self):
        return self._total_trade_amount

    @total_trade_amount.setter
    def total_trade_amount(self, value):
        self._total_trade_amount = value
    @property
    def trade_count(self):
        return self._trade_count

    @trade_count.setter
    def trade_count(self, value):
        self._trade_count = value
    @property
    def user_count(self):
        return self._user_count

    @user_count.setter
    def user_count(self, value):
        self._user_count = value
    @property
    def user_trade_amount(self):
        return self._user_trade_amount

    @user_trade_amount.setter
    def user_trade_amount(self, value):
        self._user_trade_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.avg_trade_amount:
            if hasattr(self.avg_trade_amount, 'to_alipay_dict'):
                params['avg_trade_amount'] = self.avg_trade_amount.to_alipay_dict()
            else:
                params['avg_trade_amount'] = self.avg_trade_amount
        if self.total_trade_amount:
            if hasattr(self.total_trade_amount, 'to_alipay_dict'):
                params['total_trade_amount'] = self.total_trade_amount.to_alipay_dict()
            else:
                params['total_trade_amount'] = self.total_trade_amount
        if self.trade_count:
            if hasattr(self.trade_count, 'to_alipay_dict'):
                params['trade_count'] = self.trade_count.to_alipay_dict()
            else:
                params['trade_count'] = self.trade_count
        if self.user_count:
            if hasattr(self.user_count, 'to_alipay_dict'):
                params['user_count'] = self.user_count.to_alipay_dict()
            else:
                params['user_count'] = self.user_count
        if self.user_trade_amount:
            if hasattr(self.user_trade_amount, 'to_alipay_dict'):
                params['user_trade_amount'] = self.user_trade_amount.to_alipay_dict()
            else:
                params['user_trade_amount'] = self.user_trade_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessRelationTradeInfo()
        if 'avg_trade_amount' in d:
            o.avg_trade_amount = d['avg_trade_amount']
        if 'total_trade_amount' in d:
            o.total_trade_amount = d['total_trade_amount']
        if 'trade_count' in d:
            o.trade_count = d['trade_count']
        if 'user_count' in d:
            o.user_count = d['user_count']
        if 'user_trade_amount' in d:
            o.user_trade_amount = d['user_trade_amount']
        return o


