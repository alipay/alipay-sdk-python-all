#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAccountCashpoolStatusModifyModel(object):

    def __init__(self):
        self._adjust_status = None
        self._cash_pool_id = None
        self._memo = None
        self._operator = None

    @property
    def adjust_status(self):
        return self._adjust_status

    @adjust_status.setter
    def adjust_status(self, value):
        self._adjust_status = value
    @property
    def cash_pool_id(self):
        return self._cash_pool_id

    @cash_pool_id.setter
    def cash_pool_id(self, value):
        self._cash_pool_id = value
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
        if self.adjust_status:
            if hasattr(self.adjust_status, 'to_alipay_dict'):
                params['adjust_status'] = self.adjust_status.to_alipay_dict()
            else:
                params['adjust_status'] = self.adjust_status
        if self.cash_pool_id:
            if hasattr(self.cash_pool_id, 'to_alipay_dict'):
                params['cash_pool_id'] = self.cash_pool_id.to_alipay_dict()
            else:
                params['cash_pool_id'] = self.cash_pool_id
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
        o = AlipayAccountCashpoolStatusModifyModel()
        if 'adjust_status' in d:
            o.adjust_status = d['adjust_status']
        if 'cash_pool_id' in d:
            o.cash_pool_id = d['cash_pool_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operator' in d:
            o.operator = d['operator']
        return o


