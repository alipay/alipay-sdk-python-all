#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAccountCashpoolCreateModel(object):

    def __init__(self):
        self._cash_pool_name = None
        self._cash_pool_status = None
        self._memo = None
        self._operator = None

    @property
    def cash_pool_name(self):
        return self._cash_pool_name

    @cash_pool_name.setter
    def cash_pool_name(self, value):
        self._cash_pool_name = value
    @property
    def cash_pool_status(self):
        return self._cash_pool_status

    @cash_pool_status.setter
    def cash_pool_status(self, value):
        self._cash_pool_status = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value


    def to_alipay_dict(self):
        params = dict()
        if self.cash_pool_name:
            if hasattr(self.cash_pool_name, 'to_alipay_dict'):
                params['cash_pool_name'] = self.cash_pool_name.to_alipay_dict()
            else:
                params['cash_pool_name'] = self.cash_pool_name
        if self.cash_pool_status:
            if hasattr(self.cash_pool_status, 'to_alipay_dict'):
                params['cash_pool_status'] = self.cash_pool_status.to_alipay_dict()
            else:
                params['cash_pool_status'] = self.cash_pool_status
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAccountCashpoolCreateModel()
        if 'cash_pool_name' in d:
            o.cash_pool_name = d['cash_pool_name']
        if 'cash_pool_status' in d:
            o.cash_pool_status = d['cash_pool_status']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operator' in d:
            o.operator = d['operator']
        return o


