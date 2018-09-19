#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsCoverage(object):

    def __init__(self):
        self._coverage_name = None
        self._coverage_no = None
        self._effect_end_time = None
        self._effect_start_time = None
        self._iop = None
        self._iop_premium = None
        self._premium = None
        self._sum_insured = None

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
    def iop(self):
        return self._iop

    @iop.setter
    def iop(self, value):
        self._iop = value
    @property
    def iop_premium(self):
        return self._iop_premium

    @iop_premium.setter
    def iop_premium(self, value):
        self._iop_premium = value
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        self._sum_insured = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.iop:
            if hasattr(self.iop, 'to_alipay_dict'):
                params['iop'] = self.iop.to_alipay_dict()
            else:
                params['iop'] = self.iop
        if self.iop_premium:
            if hasattr(self.iop_premium, 'to_alipay_dict'):
                params['iop_premium'] = self.iop_premium.to_alipay_dict()
            else:
                params['iop_premium'] = self.iop_premium
        if self.premium:
            if hasattr(self.premium, 'to_alipay_dict'):
                params['premium'] = self.premium.to_alipay_dict()
            else:
                params['premium'] = self.premium
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
        o = InsCoverage()
        if 'coverage_name' in d:
            o.coverage_name = d['coverage_name']
        if 'coverage_no' in d:
            o.coverage_no = d['coverage_no']
        if 'effect_end_time' in d:
            o.effect_end_time = d['effect_end_time']
        if 'effect_start_time' in d:
            o.effect_start_time = d['effect_start_time']
        if 'iop' in d:
            o.iop = d['iop']
        if 'iop_premium' in d:
            o.iop_premium = d['iop_premium']
        if 'premium' in d:
            o.premium = d['premium']
        if 'sum_insured' in d:
            o.sum_insured = d['sum_insured']
        return o


