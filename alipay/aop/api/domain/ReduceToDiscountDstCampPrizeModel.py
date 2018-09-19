#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReduceToDiscountDstCampPrizeModel(object):

    def __init__(self):
        self._budget_id = None
        self._id = None
        self._max_discount_amt = None
        self._reduce_to_discount_rate = None

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
    def reduce_to_discount_rate(self):
        return self._reduce_to_discount_rate

    @reduce_to_discount_rate.setter
    def reduce_to_discount_rate(self, value):
        self._reduce_to_discount_rate = value


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
        if self.reduce_to_discount_rate:
            if hasattr(self.reduce_to_discount_rate, 'to_alipay_dict'):
                params['reduce_to_discount_rate'] = self.reduce_to_discount_rate.to_alipay_dict()
            else:
                params['reduce_to_discount_rate'] = self.reduce_to_discount_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReduceToDiscountDstCampPrizeModel()
        if 'budget_id' in d:
            o.budget_id = d['budget_id']
        if 'id' in d:
            o.id = d['id']
        if 'max_discount_amt' in d:
            o.max_discount_amt = d['max_discount_amt']
        if 'reduce_to_discount_rate' in d:
            o.reduce_to_discount_rate = d['reduce_to_discount_rate']
        return o


