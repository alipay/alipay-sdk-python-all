#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CoverageLiability import CoverageLiability


class Coverage(object):

    def __init__(self):
        self._coverage_liability_list = None
        self._coverage_name = None
        self._coverage_no = None
        self._effect_end_time = None
        self._effect_start_time = None
        self._main_coverage = None
        self._premium = None
        self._status = None
        self._sum_insured = None

    @property
    def coverage_liability_list(self):
        return self._coverage_liability_list

    @coverage_liability_list.setter
    def coverage_liability_list(self, value):
        if isinstance(value, list):
            self._coverage_liability_list = list()
            for i in value:
                if isinstance(i, CoverageLiability):
                    self._coverage_liability_list.append(i)
                else:
                    self._coverage_liability_list.append(CoverageLiability.from_alipay_dict(i))
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
    def effect_end_time(self):
        return self._effect_end_time

    @effect_end_time.setter
    def effect_end_time(self, value):
        self._effect_end_time = value
    @property
    def effect_start_time(self):
        return self._effect_start_time

    @effect_start_time.setter
    def effect_start_time(self, value):
        self._effect_start_time = value
    @property
    def main_coverage(self):
        return self._main_coverage

    @main_coverage.setter
    def main_coverage(self, value):
        self._main_coverage = value
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        self._sum_insured = value


    def to_alipay_dict(self):
        params = dict()
        if self.coverage_liability_list:
            if isinstance(self.coverage_liability_list, list):
                for i in range(0, len(self.coverage_liability_list)):
                    element = self.coverage_liability_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.coverage_liability_list[i] = element.to_alipay_dict()
            if hasattr(self.coverage_liability_list, 'to_alipay_dict'):
                params['coverage_liability_list'] = self.coverage_liability_list.to_alipay_dict()
            else:
                params['coverage_liability_list'] = self.coverage_liability_list
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
        if self.effect_end_time:
            if hasattr(self.effect_end_time, 'to_alipay_dict'):
                params['effect_end_time'] = self.effect_end_time.to_alipay_dict()
            else:
                params['effect_end_time'] = self.effect_end_time
        if self.effect_start_time:
            if hasattr(self.effect_start_time, 'to_alipay_dict'):
                params['effect_start_time'] = self.effect_start_time.to_alipay_dict()
            else:
                params['effect_start_time'] = self.effect_start_time
        if self.main_coverage:
            if hasattr(self.main_coverage, 'to_alipay_dict'):
                params['main_coverage'] = self.main_coverage.to_alipay_dict()
            else:
                params['main_coverage'] = self.main_coverage
        if self.premium:
            if hasattr(self.premium, 'to_alipay_dict'):
                params['premium'] = self.premium.to_alipay_dict()
            else:
                params['premium'] = self.premium
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = Coverage()
        if 'coverage_liability_list' in d:
            o.coverage_liability_list = d['coverage_liability_list']
        if 'coverage_name' in d:
            o.coverage_name = d['coverage_name']
        if 'coverage_no' in d:
            o.coverage_no = d['coverage_no']
        if 'effect_end_time' in d:
            o.effect_end_time = d['effect_end_time']
        if 'effect_start_time' in d:
            o.effect_start_time = d['effect_start_time']
        if 'main_coverage' in d:
            o.main_coverage = d['main_coverage']
        if 'premium' in d:
            o.premium = d['premium']
        if 'status' in d:
            o.status = d['status']
        if 'sum_insured' in d:
            o.sum_insured = d['sum_insured']
        return o


