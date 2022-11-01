#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CropsYieldForecastInfo(object):

    def __init__(self):
        self._actual_date = None
        self._actual_year = None
        self._addition_info = None
        self._crop_code = None
        self._per_unit_yield = None
        self._total_yield = None

    @property
    def actual_date(self):
        return self._actual_date

    @actual_date.setter
    def actual_date(self, value):
        self._actual_date = value
    @property
    def actual_year(self):
        return self._actual_year

    @actual_year.setter
    def actual_year(self, value):
        self._actual_year = value
    @property
    def addition_info(self):
        return self._addition_info

    @addition_info.setter
    def addition_info(self, value):
        self._addition_info = value
    @property
    def crop_code(self):
        return self._crop_code

    @crop_code.setter
    def crop_code(self, value):
        self._crop_code = value
    @property
    def per_unit_yield(self):
        return self._per_unit_yield

    @per_unit_yield.setter
    def per_unit_yield(self, value):
        self._per_unit_yield = value
    @property
    def total_yield(self):
        return self._total_yield

    @total_yield.setter
    def total_yield(self, value):
        self._total_yield = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_date:
            if hasattr(self.actual_date, 'to_alipay_dict'):
                params['actual_date'] = self.actual_date.to_alipay_dict()
            else:
                params['actual_date'] = self.actual_date
        if self.actual_year:
            if hasattr(self.actual_year, 'to_alipay_dict'):
                params['actual_year'] = self.actual_year.to_alipay_dict()
            else:
                params['actual_year'] = self.actual_year
        if self.addition_info:
            if hasattr(self.addition_info, 'to_alipay_dict'):
                params['addition_info'] = self.addition_info.to_alipay_dict()
            else:
                params['addition_info'] = self.addition_info
        if self.crop_code:
            if hasattr(self.crop_code, 'to_alipay_dict'):
                params['crop_code'] = self.crop_code.to_alipay_dict()
            else:
                params['crop_code'] = self.crop_code
        if self.per_unit_yield:
            if hasattr(self.per_unit_yield, 'to_alipay_dict'):
                params['per_unit_yield'] = self.per_unit_yield.to_alipay_dict()
            else:
                params['per_unit_yield'] = self.per_unit_yield
        if self.total_yield:
            if hasattr(self.total_yield, 'to_alipay_dict'):
                params['total_yield'] = self.total_yield.to_alipay_dict()
            else:
                params['total_yield'] = self.total_yield
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CropsYieldForecastInfo()
        if 'actual_date' in d:
            o.actual_date = d['actual_date']
        if 'actual_year' in d:
            o.actual_year = d['actual_year']
        if 'addition_info' in d:
            o.addition_info = d['addition_info']
        if 'crop_code' in d:
            o.crop_code = d['crop_code']
        if 'per_unit_yield' in d:
            o.per_unit_yield = d['per_unit_yield']
        if 'total_yield' in d:
            o.total_yield = d['total_yield']
        return o


