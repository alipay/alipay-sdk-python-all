#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CropsHarvestForecastInfo(object):

    def __init__(self):
        self._actual_date = None
        self._addition_info = None
        self._create_date = None
        self._crop_code = None
        self._estimate_harvest_time = None
        self._is_harvest_time = None
        self._maturity = None

    @property
    def actual_date(self):
        return self._actual_date

    @actual_date.setter
    def actual_date(self, value):
        self._actual_date = value
    @property
    def addition_info(self):
        return self._addition_info

    @addition_info.setter
    def addition_info(self, value):
        self._addition_info = value
    @property
    def create_date(self):
        return self._create_date

    @create_date.setter
    def create_date(self, value):
        self._create_date = value
    @property
    def crop_code(self):
        return self._crop_code

    @crop_code.setter
    def crop_code(self, value):
        self._crop_code = value
    @property
    def estimate_harvest_time(self):
        return self._estimate_harvest_time

    @estimate_harvest_time.setter
    def estimate_harvest_time(self, value):
        self._estimate_harvest_time = value
    @property
    def is_harvest_time(self):
        return self._is_harvest_time

    @is_harvest_time.setter
    def is_harvest_time(self, value):
        self._is_harvest_time = value
    @property
    def maturity(self):
        return self._maturity

    @maturity.setter
    def maturity(self, value):
        self._maturity = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_date:
            if hasattr(self.actual_date, 'to_alipay_dict'):
                params['actual_date'] = self.actual_date.to_alipay_dict()
            else:
                params['actual_date'] = self.actual_date
        if self.addition_info:
            if hasattr(self.addition_info, 'to_alipay_dict'):
                params['addition_info'] = self.addition_info.to_alipay_dict()
            else:
                params['addition_info'] = self.addition_info
        if self.create_date:
            if hasattr(self.create_date, 'to_alipay_dict'):
                params['create_date'] = self.create_date.to_alipay_dict()
            else:
                params['create_date'] = self.create_date
        if self.crop_code:
            if hasattr(self.crop_code, 'to_alipay_dict'):
                params['crop_code'] = self.crop_code.to_alipay_dict()
            else:
                params['crop_code'] = self.crop_code
        if self.estimate_harvest_time:
            if hasattr(self.estimate_harvest_time, 'to_alipay_dict'):
                params['estimate_harvest_time'] = self.estimate_harvest_time.to_alipay_dict()
            else:
                params['estimate_harvest_time'] = self.estimate_harvest_time
        if self.is_harvest_time:
            if hasattr(self.is_harvest_time, 'to_alipay_dict'):
                params['is_harvest_time'] = self.is_harvest_time.to_alipay_dict()
            else:
                params['is_harvest_time'] = self.is_harvest_time
        if self.maturity:
            if hasattr(self.maturity, 'to_alipay_dict'):
                params['maturity'] = self.maturity.to_alipay_dict()
            else:
                params['maturity'] = self.maturity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CropsHarvestForecastInfo()
        if 'actual_date' in d:
            o.actual_date = d['actual_date']
        if 'addition_info' in d:
            o.addition_info = d['addition_info']
        if 'create_date' in d:
            o.create_date = d['create_date']
        if 'crop_code' in d:
            o.crop_code = d['crop_code']
        if 'estimate_harvest_time' in d:
            o.estimate_harvest_time = d['estimate_harvest_time']
        if 'is_harvest_time' in d:
            o.is_harvest_time = d['is_harvest_time']
        if 'maturity' in d:
            o.maturity = d['maturity']
        return o


