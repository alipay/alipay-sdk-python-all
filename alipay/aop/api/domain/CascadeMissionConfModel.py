#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbAdvertCommissionClause import KbAdvertCommissionClause


class CascadeMissionConfModel(object):

    def __init__(self):
        self._commission_clause = None
        self._commission_user_type = None

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
    def commission_user_type(self):
        return self._commission_user_type

    @commission_user_type.setter
    def commission_user_type(self, value):
        self._commission_user_type = value


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
        if self.commission_user_type:
            if hasattr(self.commission_user_type, 'to_alipay_dict'):
                params['commission_user_type'] = self.commission_user_type.to_alipay_dict()
            else:
                params['commission_user_type'] = self.commission_user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CascadeMissionConfModel()
        if 'commission_clause' in d:
            o.commission_clause = d['commission_clause']
        if 'commission_user_type' in d:
            o.commission_user_type = d['commission_user_type']
        return o


