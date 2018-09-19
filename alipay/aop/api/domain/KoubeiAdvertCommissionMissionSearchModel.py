#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbAdvertCommissionClausePercentage import KbAdvertCommissionClausePercentage
from alipay.aop.api.domain.KbAdvertCommissionClauseQuota import KbAdvertCommissionClauseQuota
from alipay.aop.api.domain.KbAdvertSubjectVoucher import KbAdvertSubjectVoucher


class KoubeiAdvertCommissionMissionSearchModel(object):

    def __init__(self):
        self._commission_clause_type = None
        self._page_index = None
        self._page_size = None
        self._percentage_clause = None
        self._quota_clause = None
        self._type = None
        self._voucher = None

    @property
    def commission_clause_type(self):
        return self._commission_clause_type

    @commission_clause_type.setter
    def commission_clause_type(self, value):
        self._commission_clause_type = value
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def percentage_clause(self):
        return self._percentage_clause

    @percentage_clause.setter
    def percentage_clause(self, value):
        if isinstance(value, KbAdvertCommissionClausePercentage):
            self._percentage_clause = value
        else:
            self._percentage_clause = KbAdvertCommissionClausePercentage.from_alipay_dict(value)
    @property
    def quota_clause(self):
        return self._quota_clause

    @quota_clause.setter
    def quota_clause(self, value):
        if isinstance(value, KbAdvertCommissionClauseQuota):
            self._quota_clause = value
        else:
            self._quota_clause = KbAdvertCommissionClauseQuota.from_alipay_dict(value)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def voucher(self):
        return self._voucher

    @voucher.setter
    def voucher(self, value):
        if isinstance(value, KbAdvertSubjectVoucher):
            self._voucher = value
        else:
            self._voucher = KbAdvertSubjectVoucher.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.commission_clause_type:
            if hasattr(self.commission_clause_type, 'to_alipay_dict'):
                params['commission_clause_type'] = self.commission_clause_type.to_alipay_dict()
            else:
                params['commission_clause_type'] = self.commission_clause_type
        if self.page_index:
            if hasattr(self.page_index, 'to_alipay_dict'):
                params['page_index'] = self.page_index.to_alipay_dict()
            else:
                params['page_index'] = self.page_index
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
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
        if self.voucher:
            if hasattr(self.voucher, 'to_alipay_dict'):
                params['voucher'] = self.voucher.to_alipay_dict()
            else:
                params['voucher'] = self.voucher
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiAdvertCommissionMissionSearchModel()
        if 'commission_clause_type' in d:
            o.commission_clause_type = d['commission_clause_type']
        if 'page_index' in d:
            o.page_index = d['page_index']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'percentage_clause' in d:
            o.percentage_clause = d['percentage_clause']
        if 'quota_clause' in d:
            o.quota_clause = d['quota_clause']
        if 'type' in d:
            o.type = d['type']
        if 'voucher' in d:
            o.voucher = d['voucher']
        return o


