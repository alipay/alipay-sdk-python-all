#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditPayChargePricingVO import CreditPayChargePricingVO
from alipay.aop.api.domain.CreditPayClauseVO import CreditPayClauseVO
from alipay.aop.api.domain.CreditPayIntPricingVO import CreditPayIntPricingVO


class CreditPayCompensateDetailVO(object):

    def __init__(self):
        self._charge_pricing_list = None
        self._clauses = None
        self._instal_itrv = None
        self._instal_type = None
        self._int_pricing = None

    @property
    def charge_pricing_list(self):
        return self._charge_pricing_list

    @charge_pricing_list.setter
    def charge_pricing_list(self, value):
        if isinstance(value, list):
            self._charge_pricing_list = list()
            for i in value:
                if isinstance(i, CreditPayChargePricingVO):
                    self._charge_pricing_list.append(i)
                else:
                    self._charge_pricing_list.append(CreditPayChargePricingVO.from_alipay_dict(i))
    @property
    def clauses(self):
        return self._clauses

    @clauses.setter
    def clauses(self, value):
        if isinstance(value, list):
            self._clauses = list()
            for i in value:
                if isinstance(i, CreditPayClauseVO):
                    self._clauses.append(i)
                else:
                    self._clauses.append(CreditPayClauseVO.from_alipay_dict(i))
    @property
    def instal_itrv(self):
        return self._instal_itrv

    @instal_itrv.setter
    def instal_itrv(self, value):
        self._instal_itrv = value
    @property
    def instal_type(self):
        return self._instal_type

    @instal_type.setter
    def instal_type(self, value):
        self._instal_type = value
    @property
    def int_pricing(self):
        return self._int_pricing

    @int_pricing.setter
    def int_pricing(self, value):
        if isinstance(value, CreditPayIntPricingVO):
            self._int_pricing = value
        else:
            self._int_pricing = CreditPayIntPricingVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.charge_pricing_list:
            if isinstance(self.charge_pricing_list, list):
                for i in range(0, len(self.charge_pricing_list)):
                    element = self.charge_pricing_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.charge_pricing_list[i] = element.to_alipay_dict()
            if hasattr(self.charge_pricing_list, 'to_alipay_dict'):
                params['charge_pricing_list'] = self.charge_pricing_list.to_alipay_dict()
            else:
                params['charge_pricing_list'] = self.charge_pricing_list
        if self.clauses:
            if isinstance(self.clauses, list):
                for i in range(0, len(self.clauses)):
                    element = self.clauses[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.clauses[i] = element.to_alipay_dict()
            if hasattr(self.clauses, 'to_alipay_dict'):
                params['clauses'] = self.clauses.to_alipay_dict()
            else:
                params['clauses'] = self.clauses
        if self.instal_itrv:
            if hasattr(self.instal_itrv, 'to_alipay_dict'):
                params['instal_itrv'] = self.instal_itrv.to_alipay_dict()
            else:
                params['instal_itrv'] = self.instal_itrv
        if self.instal_type:
            if hasattr(self.instal_type, 'to_alipay_dict'):
                params['instal_type'] = self.instal_type.to_alipay_dict()
            else:
                params['instal_type'] = self.instal_type
        if self.int_pricing:
            if hasattr(self.int_pricing, 'to_alipay_dict'):
                params['int_pricing'] = self.int_pricing.to_alipay_dict()
            else:
                params['int_pricing'] = self.int_pricing
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditPayCompensateDetailVO()
        if 'charge_pricing_list' in d:
            o.charge_pricing_list = d['charge_pricing_list']
        if 'clauses' in d:
            o.clauses = d['clauses']
        if 'instal_itrv' in d:
            o.instal_itrv = d['instal_itrv']
        if 'instal_type' in d:
            o.instal_type = d['instal_type']
        if 'int_pricing' in d:
            o.int_pricing = d['int_pricing']
        return o


