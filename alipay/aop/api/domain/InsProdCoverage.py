#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsLiability import InsLiability
from alipay.aop.api.domain.InsSumInsured import InsSumInsured


class InsProdCoverage(object):

    def __init__(self):
        self._coverage_desc = None
        self._coverage_name = None
        self._coverage_no = None
        self._is_fixed_period = None
        self._liabilities = None
        self._periods = None
        self._sum_insured = None

    @property
    def coverage_desc(self):
        return self._coverage_desc

    @coverage_desc.setter
    def coverage_desc(self, value):
        self._coverage_desc = value
    @property
    def coverage_name(self):
        return self._coverage_name

    @coverage_name.setter
    def coverage_name(self, value):
        self._coverage_name = value
    @property
    def coverage_no(self):
        return self._coverage_no

    @coverage_no.setter
    def coverage_no(self, value):
        self._coverage_no = value
    @property
    def is_fixed_period(self):
        return self._is_fixed_period

    @is_fixed_period.setter
    def is_fixed_period(self, value):
        self._is_fixed_period = value
    @property
    def liabilities(self):
        return self._liabilities

    @liabilities.setter
    def liabilities(self, value):
        if isinstance(value, list):
            self._liabilities = list()
            for i in value:
                if isinstance(i, InsLiability):
                    self._liabilities.append(i)
                else:
                    self._liabilities.append(InsLiability.from_alipay_dict(i))
    @property
    def periods(self):
        return self._periods

    @periods.setter
    def periods(self, value):
        if isinstance(value, list):
            self._periods = list()
            for i in value:
                self._periods.append(i)
    @property
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        if isinstance(value, InsSumInsured):
            self._sum_insured = value
        else:
            self._sum_insured = InsSumInsured.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.coverage_desc:
            if hasattr(self.coverage_desc, 'to_alipay_dict'):
                params['coverage_desc'] = self.coverage_desc.to_alipay_dict()
            else:
                params['coverage_desc'] = self.coverage_desc
        if self.coverage_name:
            if hasattr(self.coverage_name, 'to_alipay_dict'):
                params['coverage_name'] = self.coverage_name.to_alipay_dict()
            else:
                params['coverage_name'] = self.coverage_name
        if self.coverage_no:
            if hasattr(self.coverage_no, 'to_alipay_dict'):
                params['coverage_no'] = self.coverage_no.to_alipay_dict()
            else:
                params['coverage_no'] = self.coverage_no
        if self.is_fixed_period:
            if hasattr(self.is_fixed_period, 'to_alipay_dict'):
                params['is_fixed_period'] = self.is_fixed_period.to_alipay_dict()
            else:
                params['is_fixed_period'] = self.is_fixed_period
        if self.liabilities:
            if isinstance(self.liabilities, list):
                for i in range(0, len(self.liabilities)):
                    element = self.liabilities[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.liabilities[i] = element.to_alipay_dict()
            if hasattr(self.liabilities, 'to_alipay_dict'):
                params['liabilities'] = self.liabilities.to_alipay_dict()
            else:
                params['liabilities'] = self.liabilities
        if self.periods:
            if isinstance(self.periods, list):
                for i in range(0, len(self.periods)):
                    element = self.periods[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.periods[i] = element.to_alipay_dict()
            if hasattr(self.periods, 'to_alipay_dict'):
                params['periods'] = self.periods.to_alipay_dict()
            else:
                params['periods'] = self.periods
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
        o = InsProdCoverage()
        if 'coverage_desc' in d:
            o.coverage_desc = d['coverage_desc']
        if 'coverage_name' in d:
            o.coverage_name = d['coverage_name']
        if 'coverage_no' in d:
            o.coverage_no = d['coverage_no']
        if 'is_fixed_period' in d:
            o.is_fixed_period = d['is_fixed_period']
        if 'liabilities' in d:
            o.liabilities = d['liabilities']
        if 'periods' in d:
            o.periods = d['periods']
        if 'sum_insured' in d:
            o.sum_insured = d['sum_insured']
        return o


