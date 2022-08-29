#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsPeriodDTO import InsPeriodDTO


class InsQuoteDTO(object):

    def __init__(self):
        self._discount_rate = None
        self._ins_period = None
        self._inst_id = None
        self._original_premium = None
        self._premium = None
        self._premium_rate = None
        self._product_code = None
        self._product_name = None
        self._product_plan_id = None
        self._quote_id = None
        self._recommend_flow_id = None
        self._sum_insured = None

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
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def original_premium(self):
        return self._original_premium

    @original_premium.setter
    def original_premium(self, value):
        self._original_premium = value
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
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
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
    def recommend_flow_id(self):
        return self._recommend_flow_id

    @recommend_flow_id.setter
    def recommend_flow_id(self, value):
        self._recommend_flow_id = value
    @property
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        self._sum_insured = value


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
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.original_premium:
            if hasattr(self.original_premium, 'to_alipay_dict'):
                params['original_premium'] = self.original_premium.to_alipay_dict()
            else:
                params['original_premium'] = self.original_premium
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
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
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
        if self.recommend_flow_id:
            if hasattr(self.recommend_flow_id, 'to_alipay_dict'):
                params['recommend_flow_id'] = self.recommend_flow_id.to_alipay_dict()
            else:
                params['recommend_flow_id'] = self.recommend_flow_id
        if self.sum_insured:
            if hasattr(self.sum_insured, 'to_alipay_dict'):
                params['sum_insured'] = self.sum_insured.to_alipay_dict()
            else:
                params['sum_insured'] = self.sum_insured
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsQuoteDTO()
        if 'discount_rate' in d:
            o.discount_rate = d['discount_rate']
        if 'ins_period' in d:
            o.ins_period = d['ins_period']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'original_premium' in d:
            o.original_premium = d['original_premium']
        if 'premium' in d:
            o.premium = d['premium']
        if 'premium_rate' in d:
            o.premium_rate = d['premium_rate']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'product_plan_id' in d:
            o.product_plan_id = d['product_plan_id']
        if 'quote_id' in d:
            o.quote_id = d['quote_id']
        if 'recommend_flow_id' in d:
            o.recommend_flow_id = d['recommend_flow_id']
        if 'sum_insured' in d:
            o.sum_insured = d['sum_insured']
        return o


