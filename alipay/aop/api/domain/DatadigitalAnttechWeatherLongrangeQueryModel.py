#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAnttechWeatherLongrangeQueryModel(object):

    def __init__(self):
        self._agreement_code = None
        self._city = None
        self._district = None
        self._forecast_days = None
        self._latitude = None
        self._longitude = None
        self._province = None
        self._request_id = None
        self._weather_variables = None

    @property
    def agreement_code(self):
        return self._agreement_code

    @agreement_code.setter
    def agreement_code(self, value):
        self._agreement_code = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
    @property
    def forecast_days(self):
        return self._forecast_days

    @forecast_days.setter
    def forecast_days(self, value):
        self._forecast_days = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def weather_variables(self):
        return self._weather_variables

    @weather_variables.setter
    def weather_variables(self, value):
        if isinstance(value, list):
            self._weather_variables = list()
            for i in value:
                self._weather_variables.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_code:
            if hasattr(self.agreement_code, 'to_alipay_dict'):
                params['agreement_code'] = self.agreement_code.to_alipay_dict()
            else:
                params['agreement_code'] = self.agreement_code
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.district:
            if hasattr(self.district, 'to_alipay_dict'):
                params['district'] = self.district.to_alipay_dict()
            else:
                params['district'] = self.district
        if self.forecast_days:
            if hasattr(self.forecast_days, 'to_alipay_dict'):
                params['forecast_days'] = self.forecast_days.to_alipay_dict()
            else:
                params['forecast_days'] = self.forecast_days
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.weather_variables:
            if isinstance(self.weather_variables, list):
                for i in range(0, len(self.weather_variables)):
                    element = self.weather_variables[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.weather_variables[i] = element.to_alipay_dict()
            if hasattr(self.weather_variables, 'to_alipay_dict'):
                params['weather_variables'] = self.weather_variables.to_alipay_dict()
            else:
                params['weather_variables'] = self.weather_variables
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalAnttechWeatherLongrangeQueryModel()
        if 'agreement_code' in d:
            o.agreement_code = d['agreement_code']
        if 'city' in d:
            o.city = d['city']
        if 'district' in d:
            o.district = d['district']
        if 'forecast_days' in d:
            o.forecast_days = d['forecast_days']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'province' in d:
            o.province = d['province']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'weather_variables' in d:
            o.weather_variables = d['weather_variables']
        return o


