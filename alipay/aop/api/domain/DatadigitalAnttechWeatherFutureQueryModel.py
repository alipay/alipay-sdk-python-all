#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WeatherVariablesMark import WeatherVariablesMark


class DatadigitalAnttechWeatherFutureQueryModel(object):

    def __init__(self):
        self._agreement_code = None
        self._forecast_days = None
        self._latitude = None
        self._longitude = None
        self._past_days = None
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
    def past_days(self):
        return self._past_days

    @past_days.setter
    def past_days(self, value):
        self._past_days = value
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
        if self.past_days:
            if hasattr(self.past_days, 'to_alipay_dict'):
                params['past_days'] = self.past_days.to_alipay_dict()
            else:
                params['past_days'] = self.past_days
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
        o = DatadigitalAnttechWeatherFutureQueryModel()
        if 'agreement_code' in d:
            o.agreement_code = d['agreement_code']
        if 'forecast_days' in d:
            o.forecast_days = d['forecast_days']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'past_days' in d:
            o.past_days = d['past_days']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'timezone' in d:
            o.timezone = d['timezone']
        if 'weather_variables_mark' in d:
            o.weather_variables_mark = d['weather_variables_mark']
        return o


