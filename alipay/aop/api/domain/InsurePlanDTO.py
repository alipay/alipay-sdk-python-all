#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsPeriodDTO import InsPeriodDTO


class InsurePlanDTO(object):

    def __init__(self):
        self._discount_rate = None
        self._ins_period = None
        self._insure_plan_name = None
        self._original_premium = None
        self._original_premium_yuan = None
        self._premium = None
        self._premium_rate = None
        self._premium_yuan = None
        self._product_plan_id = None
        self._quote_id = None
        self._recommend = None
        self._sum_insured = None
        self._sum_insured_yuan = None

    @property
    def discount_rate(self):
        return self._discount_rate

    @discount_rate.setter
    def discount_rate(self, value):
        self._discount_rate = value
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
    def original_premium(self):
        return self._original_premium

    @original_premium.setter
    def original_premium(self, value):
        self._original_premium = value
    @property
    def original_premium_yuan(self):
        return self._original_premium_yuan

    @original_premium_yuan.setter
    def original_premium_yuan(self, value):
        self._original_premium_yuan = value
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def premium_rate(self):
        return self._premium_rate

    @premium_rate.setter
    def premium_rate(self, value):
        self._premium_rate = value
    @property
    def premium_yuan(self):
        return self._premium_yuan

    @premium_yuan.setter
    def premium_yuan(self, value):
        self._premium_yuan = value
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
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        self._sum_insured = value
    @property
    def sum_insured_yuan(self):
        return self._sum_insured_yuan

    @sum_insured_yuan.setter
    def sum_insured_yuan(self, value):
        self._sum_insured_yuan = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_rate:
            if hasattr(self.discount_rate, 'to_alipay_dict'):
                params['discount_rate'] = self.discount_rate.to_alipay_dict()
            else:
                params['discount_rate'] = self.discount_rate
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
        if self.original_premium:
            if hasattr(self.original_premium, 'to_alipay_dict'):
                params['original_premium'] = self.original_premium.to_alipay_dict()
            else:
                params['original_premium'] = self.original_premium
        if self.original_premium_yuan:
            if hasattr(self.original_premium_yuan, 'to_alipay_dict'):
                params['original_premium_yuan'] = self.original_premium_yuan.to_alipay_dict()
            else:
                params['original_premium_yuan'] = self.original_premium_yuan
        if self.premium:
            if hasattr(self.premium, 'to_alipay_dict'):
                params['premium'] = self.premium.to_alipay_dict()
            else:
                params['premium'] = self.premium
        if self.premium_rate:
            if hasattr(self.premium_rate, 'to_alipay_dict'):
                params['premium_rate'] = self.premium_rate.to_alipay_dict()
            else:
                params['premium_rate'] = self.premium_rate
        if self.premium_yuan:
            if hasattr(self.premium_yuan, 'to_alipay_dict'):
                params['premium_yuan'] = self.premium_yuan.to_alipay_dict()
            else:
                params['premium_yuan'] = self.premium_yuan
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
        if self.sum_insured:
            if hasattr(self.sum_insured, 'to_alipay_dict'):
                params['sum_insured'] = self.sum_insured.to_alipay_dict()
            else:
                params['sum_insured'] = self.sum_insured
        if self.sum_insured_yuan:
            if hasattr(self.sum_insured_yuan, 'to_alipay_dict'):
                params['sum_insured_yuan'] = self.sum_insured_yuan.to_alipay_dict()
            else:
                params['sum_insured_yuan'] = self.sum_insured_yuan
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsurePlanDTO()
        if 'discount_rate' in d:
            o.discount_rate = d['discount_rate']
        if 'ins_period' in d:
            o.ins_period = d['ins_period']
        if 'insure_plan_name' in d:
            o.insure_plan_name = d['insure_plan_name']
        if 'original_premium' in d:
            o.original_premium = d['original_premium']
        if 'original_premium_yuan' in d:
            o.original_premium_yuan = d['original_premium_yuan']
        if 'premium' in d:
            o.premium = d['premium']
        if 'premium_rate' in d:
            o.premium_rate = d['premium_rate']
        if 'premium_yuan' in d:
            o.premium_yuan = d['premium_yuan']
        if 'product_plan_id' in d:
            o.product_plan_id = d['product_plan_id']
        if 'quote_id' in d:
            o.quote_id = d['quote_id']
        if 'recommend' in d:
            o.recommend = d['recommend']
        if 'sum_insured' in d:
            o.sum_insured = d['sum_insured']
        if 'sum_insured_yuan' in d:
            o.sum_insured_yuan = d['sum_insured_yuan']
        return o


