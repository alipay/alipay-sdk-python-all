#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleSolAssessInfo(object):

    def __init__(self):
        self._assess_amount = None
        self._assess_amount_max = None
        self._assess_amount_min = None
        self._estimate_result_id = None
        self._order_source_app_id = None
        self._pre_assess_amount = None
        self._product_code = None

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
    def estimate_result_id(self):
        return self._estimate_result_id

    @estimate_result_id.setter
    def estimate_result_id(self, value):
        self._estimate_result_id = value
    @property
    def order_source_app_id(self):
        return self._order_source_app_id

    @order_source_app_id.setter
    def order_source_app_id(self, value):
        self._order_source_app_id = value
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
        if self.estimate_result_id:
            if hasattr(self.estimate_result_id, 'to_alipay_dict'):
                params['estimate_result_id'] = self.estimate_result_id.to_alipay_dict()
            else:
                params['estimate_result_id'] = self.estimate_result_id
        if self.order_source_app_id:
            if hasattr(self.order_source_app_id, 'to_alipay_dict'):
                params['order_source_app_id'] = self.order_source_app_id.to_alipay_dict()
            else:
                params['order_source_app_id'] = self.order_source_app_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleSolAssessInfo()
        if 'assess_amount' in d:
            o.assess_amount = d['assess_amount']
        if 'assess_amount_max' in d:
            o.assess_amount_max = d['assess_amount_max']
        if 'assess_amount_min' in d:
            o.assess_amount_min = d['assess_amount_min']
        if 'estimate_result_id' in d:
            o.estimate_result_id = d['estimate_result_id']
        if 'order_source_app_id' in d:
            o.order_source_app_id = d['order_source_app_id']
        if 'pre_assess_amount' in d:
            o.pre_assess_amount = d['pre_assess_amount']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


