#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SingleDstCampPrizeModel(object):

    def __init__(self):
        self._budget_id = None
        self._id = None
        self._reduce_amt = None

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
    def reduce_amt(self):
        return self._reduce_amt

    @reduce_amt.setter
    def reduce_amt(self, value):
        self._reduce_amt = value


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
        if self.reduce_amt:
            if hasattr(self.reduce_amt, 'to_alipay_dict'):
                params['reduce_amt'] = self.reduce_amt.to_alipay_dict()
            else:
                params['reduce_amt'] = self.reduce_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SingleDstCampPrizeModel()
        if 'budget_id' in d:
            o.budget_id = d['budget_id']
        if 'id' in d:
            o.id = d['id']
        if 'reduce_amt' in d:
            o.reduce_amt = d['reduce_amt']
        return o


