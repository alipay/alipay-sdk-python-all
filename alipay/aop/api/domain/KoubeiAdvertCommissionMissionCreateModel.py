#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbAdvertCommissionClause import KbAdvertCommissionClause
from alipay.aop.api.domain.KbadvertSmartPromoRequest import KbadvertSmartPromoRequest


class KoubeiAdvertCommissionMissionCreateModel(object):

    def __init__(self):
        self._commission_clause = None
        self._identify = None
        self._identify_type = None
        self._name = None
        self._operator_id = None
        self._operator_type = None
        self._smart_promo = None

    @property
    def commission_clause(self):
        return self._commission_clause

    @commission_clause.setter
    def commission_clause(self, value):
        if isinstance(value, list):
            self._commission_clause = list()
            for i in value:
                if isinstance(i, KbAdvertCommissionClause):
                    self._commission_clause.append(i)
                else:
                    self._commission_clause.append(KbAdvertCommissionClause.from_alipay_dict(i))
    @property
    def identify(self):
        return self._identify

    @identify.setter
    def identify(self, value):
        self._identify = value
    @property
    def identify_type(self):
        return self._identify_type

    @identify_type.setter
    def identify_type(self, value):
        self._identify_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def smart_promo(self):
        return self._smart_promo

    @smart_promo.setter
    def smart_promo(self, value):
        if isinstance(value, KbadvertSmartPromoRequest):
            self._smart_promo = value
        else:
            self._smart_promo = KbadvertSmartPromoRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.commission_clause:
            if isinstance(self.commission_clause, list):
                for i in range(0, len(self.commission_clause)):
                    element = self.commission_clause[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.commission_clause[i] = element.to_alipay_dict()
            if hasattr(self.commission_clause, 'to_alipay_dict'):
                params['commission_clause'] = self.commission_clause.to_alipay_dict()
            else:
                params['commission_clause'] = self.commission_clause
        if self.identify:
            if hasattr(self.identify, 'to_alipay_dict'):
                params['identify'] = self.identify.to_alipay_dict()
            else:
                params['identify'] = self.identify
        if self.identify_type:
            if hasattr(self.identify_type, 'to_alipay_dict'):
                params['identify_type'] = self.identify_type.to_alipay_dict()
            else:
                params['identify_type'] = self.identify_type
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        if self.smart_promo:
            if hasattr(self.smart_promo, 'to_alipay_dict'):
                params['smart_promo'] = self.smart_promo.to_alipay_dict()
            else:
                params['smart_promo'] = self.smart_promo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiAdvertCommissionMissionCreateModel()
        if 'commission_clause' in d:
            o.commission_clause = d['commission_clause']
        if 'identify' in d:
            o.identify = d['identify']
        if 'identify_type' in d:
            o.identify_type = d['identify_type']
        if 'name' in d:
            o.name = d['name']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'smart_promo' in d:
            o.smart_promo = d['smart_promo']
        return o


