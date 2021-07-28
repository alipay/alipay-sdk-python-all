#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAssetPointPointprodBudgetlibAddModel(object):

    def __init__(self):
        self._amount = None
        self._budget_code = None
        self._contract_pid = None
        self._memo = None
        self._operator = None
        self._order_no = None
        self._point_lib_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def budget_code(self):
        return self._budget_code

    @budget_code.setter
    def budget_code(self, value):
        self._budget_code = value
    @property
    def contract_pid(self):
        return self._contract_pid

    @contract_pid.setter
    def contract_pid(self, value):
        self._contract_pid = value
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
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def point_lib_id(self):
        return self._point_lib_id

    @point_lib_id.setter
    def point_lib_id(self, value):
        self._point_lib_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.budget_code:
            if hasattr(self.budget_code, 'to_alipay_dict'):
                params['budget_code'] = self.budget_code.to_alipay_dict()
            else:
                params['budget_code'] = self.budget_code
        if self.contract_pid:
            if hasattr(self.contract_pid, 'to_alipay_dict'):
                params['contract_pid'] = self.contract_pid.to_alipay_dict()
            else:
                params['contract_pid'] = self.contract_pid
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
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.point_lib_id:
            if hasattr(self.point_lib_id, 'to_alipay_dict'):
                params['point_lib_id'] = self.point_lib_id.to_alipay_dict()
            else:
                params['point_lib_id'] = self.point_lib_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAssetPointPointprodBudgetlibAddModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'budget_code' in d:
            o.budget_code = d['budget_code']
        if 'contract_pid' in d:
            o.contract_pid = d['contract_pid']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operator' in d:
            o.operator = d['operator']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'point_lib_id' in d:
            o.point_lib_id = d['point_lib_id']
        return o


