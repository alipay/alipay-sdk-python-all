#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KmsBakingSalesForecastDTO(object):

    def __init__(self):
        self._forecast_date = None
        self._forecast_level = None
        self._sku_id = None
        self._t_plus_one = None
        self._t_plus_three = None
        self._t_plus_two = None

    @property
    def forecast_date(self):
        return self._forecast_date

    @forecast_date.setter
    def forecast_date(self, value):
        self._forecast_date = value
    @property
    def forecast_level(self):
        return self._forecast_level

    @forecast_level.setter
    def forecast_level(self, value):
        self._forecast_level = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def t_plus_one(self):
        return self._t_plus_one

    @t_plus_one.setter
    def t_plus_one(self, value):
        self._t_plus_one = value
    @property
    def t_plus_three(self):
        return self._t_plus_three

    @t_plus_three.setter
    def t_plus_three(self, value):
        self._t_plus_three = value
    @property
    def t_plus_two(self):
        return self._t_plus_two

    @t_plus_two.setter
    def t_plus_two(self, value):
        self._t_plus_two = value


    def to_alipay_dict(self):
        params = dict()
        if self.forecast_date:
            if hasattr(self.forecast_date, 'to_alipay_dict'):
                params['forecast_date'] = self.forecast_date.to_alipay_dict()
            else:
                params['forecast_date'] = self.forecast_date
        if self.forecast_level:
            if hasattr(self.forecast_level, 'to_alipay_dict'):
                params['forecast_level'] = self.forecast_level.to_alipay_dict()
            else:
                params['forecast_level'] = self.forecast_level
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.t_plus_one:
            if hasattr(self.t_plus_one, 'to_alipay_dict'):
                params['t_plus_one'] = self.t_plus_one.to_alipay_dict()
            else:
                params['t_plus_one'] = self.t_plus_one
        if self.t_plus_three:
            if hasattr(self.t_plus_three, 'to_alipay_dict'):
                params['t_plus_three'] = self.t_plus_three.to_alipay_dict()
            else:
                params['t_plus_three'] = self.t_plus_three
        if self.t_plus_two:
            if hasattr(self.t_plus_two, 'to_alipay_dict'):
                params['t_plus_two'] = self.t_plus_two.to_alipay_dict()
            else:
                params['t_plus_two'] = self.t_plus_two
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KmsBakingSalesForecastDTO()
        if 'forecast_date' in d:
            o.forecast_date = d['forecast_date']
        if 'forecast_level' in d:
            o.forecast_level = d['forecast_level']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 't_plus_one' in d:
            o.t_plus_one = d['t_plus_one']
        if 't_plus_three' in d:
            o.t_plus_three = d['t_plus_three']
        if 't_plus_two' in d:
            o.t_plus_two = d['t_plus_two']
        return o


