#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbAdvertPercentageCommissionClause import KbAdvertPercentageCommissionClause
from alipay.aop.api.domain.KbAdvertPreserveCommissionClause import KbAdvertPreserveCommissionClause
from alipay.aop.api.domain.KbAdvertQuotaCommissionClause import KbAdvertQuotaCommissionClause


class KbAdvertCommissionClause(object):

    def __init__(self):
        self._clause_type = None
        self._percentage_clause = None
        self._preserve_clause = None
        self._quota_clause = None

    @property
    def clause_type(self):
        return self._clause_type

    @clause_type.setter
    def clause_type(self, value):
        self._clause_type = value
    @property
    def percentage_clause(self):
        return self._percentage_clause

    @percentage_clause.setter
    def percentage_clause(self, value):
        if isinstance(value, KbAdvertPercentageCommissionClause):
            self._percentage_clause = value
        else:
            self._percentage_clause = KbAdvertPercentageCommissionClause.from_alipay_dict(value)
    @property
    def preserve_clause(self):
        return self._preserve_clause

    @preserve_clause.setter
    def preserve_clause(self, value):
        if isinstance(value, KbAdvertPreserveCommissionClause):
            self._preserve_clause = value
        else:
            self._preserve_clause = KbAdvertPreserveCommissionClause.from_alipay_dict(value)
    @property
    def quota_clause(self):
        return self._quota_clause

    @quota_clause.setter
    def quota_clause(self, value):
        if isinstance(value, KbAdvertQuotaCommissionClause):
            self._quota_clause = value
        else:
            self._quota_clause = KbAdvertQuotaCommissionClause.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.clause_type:
            if hasattr(self.clause_type, 'to_alipay_dict'):
                params['clause_type'] = self.clause_type.to_alipay_dict()
            else:
                params['clause_type'] = self.clause_type
        if self.percentage_clause:
            if hasattr(self.percentage_clause, 'to_alipay_dict'):
                params['percentage_clause'] = self.percentage_clause.to_alipay_dict()
            else:
                params['percentage_clause'] = self.percentage_clause
        if self.preserve_clause:
            if hasattr(self.preserve_clause, 'to_alipay_dict'):
                params['preserve_clause'] = self.preserve_clause.to_alipay_dict()
            else:
                params['preserve_clause'] = self.preserve_clause
        if self.quota_clause:
            if hasattr(self.quota_clause, 'to_alipay_dict'):
                params['quota_clause'] = self.quota_clause.to_alipay_dict()
            else:
                params['quota_clause'] = self.quota_clause
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertCommissionClause()
        if 'clause_type' in d:
            o.clause_type = d['clause_type']
        if 'percentage_clause' in d:
            o.percentage_clause = d['percentage_clause']
        if 'preserve_clause' in d:
            o.preserve_clause = d['preserve_clause']
        if 'quota_clause' in d:
            o.quota_clause = d['quota_clause']
        return o


