#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsPeriodDTO import InsPeriodDTO


class PurchaseInsurePlanDTO(object):

    def __init__(self):
        self._current_selected = None
        self._ins_period = None
        self._insure_plan_name = None
        self._original_refer_premium = None
        self._per_refer_premium = None
        self._per_refer_sum_insured = None
        self._product_plan_id = None
        self._quote_id = None
        self._recommend = None
        self._refer_discount_rate = None
        self._refer_premium_rate = None

    @property
    def current_selected(self):
        return self._current_selected

    @current_selected.setter
    def current_selected(self, value):
        self._current_selected = value
    @property
    def ins_period(self):
        return self._ins_period

    @ins_period.setter
    def ins_period(self, value):
        if isinstance(value, InsPeriodDTO):
            self._ins_period = value
        else:
            self._ins_period = InsPeriodDTO.from_alipay_dict(value)
    @property
    def insure_plan_name(self):
        return self._insure_plan_name

    @insure_plan_name.setter
    def insure_plan_name(self, value):
        self._insure_plan_name = value
    @property
    def original_refer_premium(self):
        return self._original_refer_premium

    @original_refer_premium.setter
    def original_refer_premium(self, value):
        self._original_refer_premium = value
    @property
    def per_refer_premium(self):
        return self._per_refer_premium

    @per_refer_premium.setter
    def per_refer_premium(self, value):
        self._per_refer_premium = value
    @property
    def per_refer_sum_insured(self):
        return self._per_refer_sum_insured

    @per_refer_sum_insured.setter
    def per_refer_sum_insured(self, value):
        self._per_refer_sum_insured = value
    @property
    def product_plan_id(self):
        return self._product_plan_id

    @product_plan_id.setter
    def product_plan_id(self, value):
        self._product_plan_id = value
    @property
    def quote_id(self):
        return self._quote_id

    @quote_id.setter
    def quote_id(self, value):
        self._quote_id = value
    @property
    def recommend(self):
        return self._recommend

    @recommend.setter
    def recommend(self, value):
        self._recommend = value
    @property
    def refer_discount_rate(self):
        return self._refer_discount_rate

    @refer_discount_rate.setter
    def refer_discount_rate(self, value):
        self._refer_discount_rate = value
    @property
    def refer_premium_rate(self):
        return self._refer_premium_rate

    @refer_premium_rate.setter
    def refer_premium_rate(self, value):
        self._refer_premium_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_selected:
            if hasattr(self.current_selected, 'to_alipay_dict'):
                params['current_selected'] = self.current_selected.to_alipay_dict()
            else:
                params['current_selected'] = self.current_selected
        if self.ins_period:
            if hasattr(self.ins_period, 'to_alipay_dict'):
                params['ins_period'] = self.ins_period.to_alipay_dict()
            else:
                params['ins_period'] = self.ins_period
        if self.insure_plan_name:
            if hasattr(self.insure_plan_name, 'to_alipay_dict'):
                params['insure_plan_name'] = self.insure_plan_name.to_alipay_dict()
            else:
                params['insure_plan_name'] = self.insure_plan_name
        if self.original_refer_premium:
            if hasattr(self.original_refer_premium, 'to_alipay_dict'):
                params['original_refer_premium'] = self.original_refer_premium.to_alipay_dict()
            else:
                params['original_refer_premium'] = self.original_refer_premium
        if self.per_refer_premium:
            if hasattr(self.per_refer_premium, 'to_alipay_dict'):
                params['per_refer_premium'] = self.per_refer_premium.to_alipay_dict()
            else:
                params['per_refer_premium'] = self.per_refer_premium
        if self.per_refer_sum_insured:
            if hasattr(self.per_refer_sum_insured, 'to_alipay_dict'):
                params['per_refer_sum_insured'] = self.per_refer_sum_insured.to_alipay_dict()
            else:
                params['per_refer_sum_insured'] = self.per_refer_sum_insured
        if self.product_plan_id:
            if hasattr(self.product_plan_id, 'to_alipay_dict'):
                params['product_plan_id'] = self.product_plan_id.to_alipay_dict()
            else:
                params['product_plan_id'] = self.product_plan_id
        if self.quote_id:
            if hasattr(self.quote_id, 'to_alipay_dict'):
                params['quote_id'] = self.quote_id.to_alipay_dict()
            else:
                params['quote_id'] = self.quote_id
        if self.recommend:
            if hasattr(self.recommend, 'to_alipay_dict'):
                params['recommend'] = self.recommend.to_alipay_dict()
            else:
                params['recommend'] = self.recommend
        if self.refer_discount_rate:
            if hasattr(self.refer_discount_rate, 'to_alipay_dict'):
                params['refer_discount_rate'] = self.refer_discount_rate.to_alipay_dict()
            else:
                params['refer_discount_rate'] = self.refer_discount_rate
        if self.refer_premium_rate:
            if hasattr(self.refer_premium_rate, 'to_alipay_dict'):
                params['refer_premium_rate'] = self.refer_premium_rate.to_alipay_dict()
            else:
                params['refer_premium_rate'] = self.refer_premium_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PurchaseInsurePlanDTO()
        if 'current_selected' in d:
            o.current_selected = d['current_selected']
        if 'ins_period' in d:
            o.ins_period = d['ins_period']
        if 'insure_plan_name' in d:
            o.insure_plan_name = d['insure_plan_name']
        if 'original_refer_premium' in d:
            o.original_refer_premium = d['original_refer_premium']
        if 'per_refer_premium' in d:
            o.per_refer_premium = d['per_refer_premium']
        if 'per_refer_sum_insured' in d:
            o.per_refer_sum_insured = d['per_refer_sum_insured']
        if 'product_plan_id' in d:
            o.product_plan_id = d['product_plan_id']
        if 'quote_id' in d:
            o.quote_id = d['quote_id']
        if 'recommend' in d:
            o.recommend = d['recommend']
        if 'refer_discount_rate' in d:
            o.refer_discount_rate = d['refer_discount_rate']
        if 'refer_premium_rate' in d:
            o.refer_premium_rate = d['refer_premium_rate']
        return o


