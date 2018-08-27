#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReduceDstCampPrizeModel(object):

    def __init__(self):
        self._budget_id = None
        self._id = None
        self._max_discount_amt = None
        self._reduce_amt_pre = None
        self._reduce_amt_suf = None

    @property
    def budget_id(self):
        return self._budget_id

    @budget_id.setter
    def budget_id(self, value):
        self._budget_id = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def max_discount_amt(self):
        return self._max_discount_amt

    @max_discount_amt.setter
    def max_discount_amt(self, value):
        self._max_discount_amt = value
    @property
    def reduce_amt_pre(self):
        return self._reduce_amt_pre

    @reduce_amt_pre.setter
    def reduce_amt_pre(self, value):
        self._reduce_amt_pre = value
    @property
    def reduce_amt_suf(self):
        return self._reduce_amt_suf

    @reduce_amt_suf.setter
    def reduce_amt_suf(self, value):
        self._reduce_amt_suf = value


    def to_alipay_dict(self):
        params = dict()
        if self.budget_id:
            if hasattr(self.budget_id, 'to_alipay_dict'):
                params['budget_id'] = self.budget_id.to_alipay_dict()
            else:
                params['budget_id'] = self.budget_id
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.max_discount_amt:
            if hasattr(self.max_discount_amt, 'to_alipay_dict'):
                params['max_discount_amt'] = self.max_discount_amt.to_alipay_dict()
            else:
                params['max_discount_amt'] = self.max_discount_amt
        if self.reduce_amt_pre:
            if hasattr(self.reduce_amt_pre, 'to_alipay_dict'):
                params['reduce_amt_pre'] = self.reduce_amt_pre.to_alipay_dict()
            else:
                params['reduce_amt_pre'] = self.reduce_amt_pre
        if self.reduce_amt_suf:
            if hasattr(self.reduce_amt_suf, 'to_alipay_dict'):
                params['reduce_amt_suf'] = self.reduce_amt_suf.to_alipay_dict()
            else:
                params['reduce_amt_suf'] = self.reduce_amt_suf
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReduceDstCampPrizeModel()
        if 'budget_id' in d:
            o.budget_id = d['budget_id']
        if 'id' in d:
            o.id = d['id']
        if 'max_discount_amt' in d:
            o.max_discount_amt = d['max_discount_amt']
        if 'reduce_amt_pre' in d:
            o.reduce_amt_pre = d['reduce_amt_pre']
        if 'reduce_amt_suf' in d:
            o.reduce_amt_suf = d['reduce_amt_suf']
        return o


