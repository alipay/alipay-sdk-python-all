#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AgWeatherForecastInfo(object):

    def __init__(self):
        self._actual_date = None
        self._addition_info = None
        self._avg_temperature = None
        self._forecast_date = None
        self._precipitation = None
        self._radiation = None
        self._wind_speed = None

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
    def avg_temperature(self):
        return self._avg_temperature

    @avg_temperature.setter
    def avg_temperature(self, value):
        self._avg_temperature = value
    @property
    def forecast_date(self):
        return self._forecast_date

    @forecast_date.setter
    def forecast_date(self, value):
        self._forecast_date = value
    @property
    def precipitation(self):
        return self._precipitation

    @precipitation.setter
    def precipitation(self, value):
        self._precipitation = value
    @property
    def radiation(self):
        return self._radiation

    @radiation.setter
    def radiation(self, value):
        self._radiation = value
    @property
    def wind_speed(self):
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, value):
        self._wind_speed = value


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
        if self.avg_temperature:
            if hasattr(self.avg_temperature, 'to_alipay_dict'):
                params['avg_temperature'] = self.avg_temperature.to_alipay_dict()
            else:
                params['avg_temperature'] = self.avg_temperature
        if self.forecast_date:
            if hasattr(self.forecast_date, 'to_alipay_dict'):
                params['forecast_date'] = self.forecast_date.to_alipay_dict()
            else:
                params['forecast_date'] = self.forecast_date
        if self.precipitation:
            if hasattr(self.precipitation, 'to_alipay_dict'):
                params['precipitation'] = self.precipitation.to_alipay_dict()
            else:
                params['precipitation'] = self.precipitation
        if self.radiation:
            if hasattr(self.radiation, 'to_alipay_dict'):
                params['radiation'] = self.radiation.to_alipay_dict()
            else:
                params['radiation'] = self.radiation
        if self.wind_speed:
            if hasattr(self.wind_speed, 'to_alipay_dict'):
                params['wind_speed'] = self.wind_speed.to_alipay_dict()
            else:
                params['wind_speed'] = self.wind_speed
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AgWeatherForecastInfo()
        if 'actual_date' in d:
            o.actual_date = d['actual_date']
        if 'addition_info' in d:
            o.addition_info = d['addition_info']
        if 'avg_temperature' in d:
            o.avg_temperature = d['avg_temperature']
        if 'forecast_date' in d:
            o.forecast_date = d['forecast_date']
        if 'precipitation' in d:
            o.precipitation = d['precipitation']
        if 'radiation' in d:
            o.radiation = d['radiation']
        if 'wind_speed' in d:
            o.wind_speed = d['wind_speed']
        return o


