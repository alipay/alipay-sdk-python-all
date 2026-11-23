#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WeatherVariablesMark import WeatherVariablesMark


class DatadigitalAnttechWeatherHistoryQueryModel(object):

    def __init__(self):
        self._agreement_code = None
        self._city = None
        self._date_end = None
        self._date_start = None
        self._district = None
        self._latitude = None
        self._longitude = None
        self._province = None
        self._request_id = None
        self._timezone = None
        self._weather_variables_mark = None

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
    def date_end(self):
        return self._date_end

    @date_end.setter
    def date_end(self, value):
        self._date_end = value
    @property
    def date_start(self):
        return self._date_start

    @date_start.setter
    def date_start(self, value):
        self._date_start = value
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
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
    def timezone(self):
        return self._timezone

    @timezone.setter
    def timezone(self, value):
        self._timezone = value
    @property
    def weather_variables_mark(self):
        return self._weather_variables_mark

    @weather_variables_mark.setter
    def weather_variables_mark(self, value):
        if isinstance(value, WeatherVariablesMark):
            self._weather_variables_mark = value
        else:
            self._weather_variables_mark = WeatherVariablesMark.from_alipay_dict(value)


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
        if self.date_end:
            if hasattr(self.date_end, 'to_alipay_dict'):
                params['date_end'] = self.date_end.to_alipay_dict()
            else:
                params['date_end'] = self.date_end
        if self.date_start:
            if hasattr(self.date_start, 'to_alipay_dict'):
                params['date_start'] = self.date_start.to_alipay_dict()
            else:
                params['date_start'] = self.date_start
        if self.district:
            if hasattr(self.district, 'to_alipay_dict'):
                params['district'] = self.district.to_alipay_dict()
            else:
                params['district'] = self.district
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
        if self.timezone:
            if hasattr(self.timezone, 'to_alipay_dict'):
                params['timezone'] = self.timezone.to_alipay_dict()
            else:
                params['timezone'] = self.timezone
        if self.weather_variables_mark:
            if hasattr(self.weather_variables_mark, 'to_alipay_dict'):
                params['weather_variables_mark'] = self.weather_variables_mark.to_alipay_dict()
            else:
                params['weather_variables_mark'] = self.weather_variables_mark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalAnttechWeatherHistoryQueryModel()
        if 'agreement_code' in d:
            o.agreement_code = d['agreement_code']
        if 'city' in d:
            o.city = d['city']
        if 'date_end' in d:
            o.date_end = d['date_end']
        if 'date_start' in d:
            o.date_start = d['date_start']
        if 'district' in d:
            o.district = d['district']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'province' in d:
            o.province = d['province']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'timezone' in d:
            o.timezone = d['timezone']
        if 'weather_variables_mark' in d:
            o.weather_variables_mark = d['weather_variables_mark']
        return o


