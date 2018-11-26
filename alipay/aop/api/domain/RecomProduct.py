#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecomPlan import RecomPlan


class RecomProduct(object):

    def __init__(self):
        self._max_quan = None
        self._name = None
        self._plans = None
        self._premium = None
        self._prod_no = None
        self._type = None

    @property
    def max_quan(self):
        return self._max_quan

    @max_quan.setter
    def max_quan(self, value):
        self._max_quan = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def plans(self):
        return self._plans

    @plans.setter
    def plans(self, value):
        if isinstance(value, RecomPlan):
            self._plans = value
        else:
            self._plans = RecomPlan.from_alipay_dict(value)
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def prod_no(self):
        return self._prod_no

    @prod_no.setter
    def prod_no(self, value):
        self._prod_no = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.max_quan:
            if hasattr(self.max_quan, 'to_alipay_dict'):
                params['max_quan'] = self.max_quan.to_alipay_dict()
            else:
                params['max_quan'] = self.max_quan
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.plans:
            if hasattr(self.plans, 'to_alipay_dict'):
                params['plans'] = self.plans.to_alipay_dict()
            else:
                params['plans'] = self.plans
        if self.premium:
            if hasattr(self.premium, 'to_alipay_dict'):
                params['premium'] = self.premium.to_alipay_dict()
            else:
                params['premium'] = self.premium
        if self.prod_no:
            if hasattr(self.prod_no, 'to_alipay_dict'):
                params['prod_no'] = self.prod_no.to_alipay_dict()
            else:
                params['prod_no'] = self.prod_no
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecomProduct()
        if 'max_quan' in d:
            o.max_quan = d['max_quan']
        if 'name' in d:
            o.name = d['name']
        if 'plans' in d:
            o.plans = d['plans']
        if 'premium' in d:
            o.premium = d['premium']
        if 'prod_no' in d:
            o.prod_no = d['prod_no']
        if 'type' in d:
            o.type = d['type']
        return o


