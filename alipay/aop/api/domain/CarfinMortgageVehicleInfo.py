#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarfinMortgageVehicleInfo(object):

    def __init__(self):
        self._brand_name = None
        self._model_name = None
        self._series_name = None

    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def model_name(self):
        return self._model_name

    @model_name.setter
    def model_name(self, value):
        self._model_name = value
    @property
    def series_name(self):
        return self._series_name

    @series_name.setter
    def series_name(self, value):
        self._series_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.model_name:
            if hasattr(self.model_name, 'to_alipay_dict'):
                params['model_name'] = self.model_name.to_alipay_dict()
            else:
                params['model_name'] = self.model_name
        if self.series_name:
            if hasattr(self.series_name, 'to_alipay_dict'):
                params['series_name'] = self.series_name.to_alipay_dict()
            else:
                params['series_name'] = self.series_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarfinMortgageVehicleInfo()
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'model_name' in d:
            o.model_name = d['model_name']
        if 'series_name' in d:
            o.series_name = d['series_name']
        return o


