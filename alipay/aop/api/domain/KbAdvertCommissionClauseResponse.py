#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbAdvertCommissionClausePercentageResponse import KbAdvertCommissionClausePercentageResponse
from alipay.aop.api.domain.KbAdvertCommissionClauseQuotaResponse import KbAdvertCommissionClauseQuotaResponse


class KbAdvertCommissionClauseResponse(object):

    def __init__(self):
        self._percentage_clause = None
        self._quota_clause = None
        self._type = None

    @property
    def percentage_clause(self):
        return self._percentage_clause

    @percentage_clause.setter
    def percentage_clause(self, value):
        if isinstance(value, KbAdvertCommissionClausePercentageResponse):
            self._percentage_clause = value
        else:
            self._percentage_clause = KbAdvertCommissionClausePercentageResponse.from_alipay_dict(value)
    @property
    def quota_clause(self):
        return self._quota_clause

    @quota_clause.setter
    def quota_clause(self, value):
        if isinstance(value, KbAdvertCommissionClauseQuotaResponse):
            self._quota_clause = value
        else:
            self._quota_clause = KbAdvertCommissionClauseQuotaResponse.from_alipay_dict(value)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.percentage_clause:
            if hasattr(self.percentage_clause, 'to_alipay_dict'):
                params['percentage_clause'] = self.percentage_clause.to_alipay_dict()
            else:
                params['percentage_clause'] = self.percentage_clause
        if self.quota_clause:
            if hasattr(self.quota_clause, 'to_alipay_dict'):
                params['quota_clause'] = self.quota_clause.to_alipay_dict()
            else:
                params['quota_clause'] = self.quota_clause
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
        o = KbAdvertCommissionClauseResponse()
        if 'percentage_clause' in d:
            o.percentage_clause = d['percentage_clause']
        if 'quota_clause' in d:
            o.quota_clause = d['quota_clause']
        if 'type' in d:
            o.type = d['type']
        return o


