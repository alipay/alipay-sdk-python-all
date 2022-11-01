#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CropsSoilMoistureInfo(object):

    def __init__(self):
        self._actual_date = None
        self._addition_info = None
        self._crop_code = None
        self._forecast_date = None
        self._risk_index = None
        self._risk_level = None

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
    def crop_code(self):
        return self._crop_code

    @crop_code.setter
    def crop_code(self, value):
        self._crop_code = value
    @property
    def forecast_date(self):
        return self._forecast_date

    @forecast_date.setter
    def forecast_date(self, value):
        self._forecast_date = value
    @property
    def risk_index(self):
        return self._risk_index

    @risk_index.setter
    def risk_index(self, value):
        self._risk_index = value
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value


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
        if self.crop_code:
            if hasattr(self.crop_code, 'to_alipay_dict'):
                params['crop_code'] = self.crop_code.to_alipay_dict()
            else:
                params['crop_code'] = self.crop_code
        if self.forecast_date:
            if hasattr(self.forecast_date, 'to_alipay_dict'):
                params['forecast_date'] = self.forecast_date.to_alipay_dict()
            else:
                params['forecast_date'] = self.forecast_date
        if self.risk_index:
            if hasattr(self.risk_index, 'to_alipay_dict'):
                params['risk_index'] = self.risk_index.to_alipay_dict()
            else:
                params['risk_index'] = self.risk_index
        if self.risk_level:
            if hasattr(self.risk_level, 'to_alipay_dict'):
                params['risk_level'] = self.risk_level.to_alipay_dict()
            else:
                params['risk_level'] = self.risk_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CropsSoilMoistureInfo()
        if 'actual_date' in d:
            o.actual_date = d['actual_date']
        if 'addition_info' in d:
            o.addition_info = d['addition_info']
        if 'crop_code' in d:
            o.crop_code = d['crop_code']
        if 'forecast_date' in d:
            o.forecast_date = d['forecast_date']
        if 'risk_index' in d:
            o.risk_index = d['risk_index']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        return o


