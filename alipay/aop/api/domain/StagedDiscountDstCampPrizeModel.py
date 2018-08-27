#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DiscountRateModel import DiscountRateModel


class StagedDiscountDstCampPrizeModel(object):

    def __init__(self):
        self._budget_id = None
        self._discount_rate_model_list = None
        self._id = None
        self._max_discount_amt = None

    @property
    def budget_id(self):
        return self._budget_id

    @budget_id.setter
    def budget_id(self, value):
        self._budget_id = value
    @property
    def discount_rate_model_list(self):
        return self._discount_rate_model_list

    @discount_rate_model_list.setter
    def discount_rate_model_list(self, value):
        if isinstance(value, list):
            self._discount_rate_model_list = list()
            for i in value:
                if isinstance(i, DiscountRateModel):
                    self._discount_rate_model_list.append(i)
                else:
                    self._discount_rate_model_list.append(DiscountRateModel.from_alipay_dict(i))
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


    def to_alipay_dict(self):
        params = dict()
        if self.budget_id:
            if hasattr(self.budget_id, 'to_alipay_dict'):
                params['budget_id'] = self.budget_id.to_alipay_dict()
            else:
                params['budget_id'] = self.budget_id
        if self.discount_rate_model_list:
            if isinstance(self.discount_rate_model_list, list):
                for i in range(0, len(self.discount_rate_model_list)):
                    element = self.discount_rate_model_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.discount_rate_model_list[i] = element.to_alipay_dict()
            if hasattr(self.discount_rate_model_list, 'to_alipay_dict'):
                params['discount_rate_model_list'] = self.discount_rate_model_list.to_alipay_dict()
            else:
                params['discount_rate_model_list'] = self.discount_rate_model_list
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StagedDiscountDstCampPrizeModel()
        if 'budget_id' in d:
            o.budget_id = d['budget_id']
        if 'discount_rate_model_list' in d:
            o.discount_rate_model_list = d['discount_rate_model_list']
        if 'id' in d:
            o.id = d['id']
        if 'max_discount_amt' in d:
            o.max_discount_amt = d['max_discount_amt']
        return o


