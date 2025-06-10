#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleQuestion import RecycleQuestion


class RecycleItemInfo(object):

    def __init__(self):
        self._assess_amount = None
        self._assess_amount_max = None
        self._assess_amount_min = None
        self._brand_code = None
        self._category_code = None
        self._pre_assess_amount = None
        self._product_code = None
        self._product_item_id = None
        self._product_name = None
        self._question_list = None

    @property
    def assess_amount(self):
        return self._assess_amount

    @assess_amount.setter
    def assess_amount(self, value):
        self._assess_amount = value
    @property
    def assess_amount_max(self):
        return self._assess_amount_max

    @assess_amount_max.setter
    def assess_amount_max(self, value):
        self._assess_amount_max = value
    @property
    def assess_amount_min(self):
        return self._assess_amount_min

    @assess_amount_min.setter
    def assess_amount_min(self, value):
        self._assess_amount_min = value
    @property
    def brand_code(self):
        return self._brand_code

    @brand_code.setter
    def brand_code(self, value):
        self._brand_code = value
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def pre_assess_amount(self):
        return self._pre_assess_amount

    @pre_assess_amount.setter
    def pre_assess_amount(self, value):
        self._pre_assess_amount = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_item_id(self):
        return self._product_item_id

    @product_item_id.setter
    def product_item_id(self, value):
        self._product_item_id = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def question_list(self):
        return self._question_list

    @question_list.setter
    def question_list(self, value):
        if isinstance(value, list):
            self._question_list = list()
            for i in value:
                if isinstance(i, RecycleQuestion):
                    self._question_list.append(i)
                else:
                    self._question_list.append(RecycleQuestion.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.assess_amount:
            if hasattr(self.assess_amount, 'to_alipay_dict'):
                params['assess_amount'] = self.assess_amount.to_alipay_dict()
            else:
                params['assess_amount'] = self.assess_amount
        if self.assess_amount_max:
            if hasattr(self.assess_amount_max, 'to_alipay_dict'):
                params['assess_amount_max'] = self.assess_amount_max.to_alipay_dict()
            else:
                params['assess_amount_max'] = self.assess_amount_max
        if self.assess_amount_min:
            if hasattr(self.assess_amount_min, 'to_alipay_dict'):
                params['assess_amount_min'] = self.assess_amount_min.to_alipay_dict()
            else:
                params['assess_amount_min'] = self.assess_amount_min
        if self.brand_code:
            if hasattr(self.brand_code, 'to_alipay_dict'):
                params['brand_code'] = self.brand_code.to_alipay_dict()
            else:
                params['brand_code'] = self.brand_code
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.pre_assess_amount:
            if hasattr(self.pre_assess_amount, 'to_alipay_dict'):
                params['pre_assess_amount'] = self.pre_assess_amount.to_alipay_dict()
            else:
                params['pre_assess_amount'] = self.pre_assess_amount
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.product_item_id:
            if hasattr(self.product_item_id, 'to_alipay_dict'):
                params['product_item_id'] = self.product_item_id.to_alipay_dict()
            else:
                params['product_item_id'] = self.product_item_id
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.question_list:
            if isinstance(self.question_list, list):
                for i in range(0, len(self.question_list)):
                    element = self.question_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.question_list[i] = element.to_alipay_dict()
            if hasattr(self.question_list, 'to_alipay_dict'):
                params['question_list'] = self.question_list.to_alipay_dict()
            else:
                params['question_list'] = self.question_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleItemInfo()
        if 'assess_amount' in d:
            o.assess_amount = d['assess_amount']
        if 'assess_amount_max' in d:
            o.assess_amount_max = d['assess_amount_max']
        if 'assess_amount_min' in d:
            o.assess_amount_min = d['assess_amount_min']
        if 'brand_code' in d:
            o.brand_code = d['brand_code']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'pre_assess_amount' in d:
            o.pre_assess_amount = d['pre_assess_amount']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_item_id' in d:
            o.product_item_id = d['product_item_id']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'question_list' in d:
            o.question_list = d['question_list']
        return o


