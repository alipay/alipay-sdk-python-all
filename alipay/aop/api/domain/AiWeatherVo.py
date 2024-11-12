#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AiWeatherVo(object):

    def __init__(self):
        self._aqi_quality = None
        self._aqi_score = None
        self._city_name = None
        self._humidity = None
        self._temperature = None
        self._today_highest_temperature = None
        self._today_lowest_temperature = None
        self._weather = None
        self._wind_direction = None
        self._wind_evel = None

    @property
    def aqi_quality(self):
        return self._aqi_quality

    @aqi_quality.setter
    def aqi_quality(self, value):
        self._aqi_quality = value
    @property
    def aqi_score(self):
        return self._aqi_score

    @aqi_score.setter
    def aqi_score(self, value):
        self._aqi_score = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, value):
        self._humidity = value
    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value
    @property
    def today_highest_temperature(self):
        return self._today_highest_temperature

    @today_highest_temperature.setter
    def today_highest_temperature(self, value):
        self._today_highest_temperature = value
    @property
    def today_lowest_temperature(self):
        return self._today_lowest_temperature

    @today_lowest_temperature.setter
    def today_lowest_temperature(self, value):
        self._today_lowest_temperature = value
    @property
    def weather(self):
        return self._weather

    @weather.setter
    def weather(self, value):
        self._weather = value
    @property
    def wind_direction(self):
        return self._wind_direction

    @wind_direction.setter
    def wind_direction(self, value):
        self._wind_direction = value
    @property
    def wind_evel(self):
        return self._wind_evel

    @wind_evel.setter
    def wind_evel(self, value):
        self._wind_evel = value


    def to_alipay_dict(self):
        params = dict()
        if self.aqi_quality:
            if hasattr(self.aqi_quality, 'to_alipay_dict'):
                params['aqi_quality'] = self.aqi_quality.to_alipay_dict()
            else:
                params['aqi_quality'] = self.aqi_quality
        if self.aqi_score:
            if hasattr(self.aqi_score, 'to_alipay_dict'):
                params['aqi_score'] = self.aqi_score.to_alipay_dict()
            else:
                params['aqi_score'] = self.aqi_score
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.humidity:
            if hasattr(self.humidity, 'to_alipay_dict'):
                params['humidity'] = self.humidity.to_alipay_dict()
            else:
                params['humidity'] = self.humidity
        if self.temperature:
            if hasattr(self.temperature, 'to_alipay_dict'):
                params['temperature'] = self.temperature.to_alipay_dict()
            else:
                params['temperature'] = self.temperature
        if self.today_highest_temperature:
            if hasattr(self.today_highest_temperature, 'to_alipay_dict'):
                params['today_highest_temperature'] = self.today_highest_temperature.to_alipay_dict()
            else:
                params['today_highest_temperature'] = self.today_highest_temperature
        if self.today_lowest_temperature:
            if hasattr(self.today_lowest_temperature, 'to_alipay_dict'):
                params['today_lowest_temperature'] = self.today_lowest_temperature.to_alipay_dict()
            else:
                params['today_lowest_temperature'] = self.today_lowest_temperature
        if self.weather:
            if hasattr(self.weather, 'to_alipay_dict'):
                params['weather'] = self.weather.to_alipay_dict()
            else:
                params['weather'] = self.weather
        if self.wind_direction:
            if hasattr(self.wind_direction, 'to_alipay_dict'):
                params['wind_direction'] = self.wind_direction.to_alipay_dict()
            else:
                params['wind_direction'] = self.wind_direction
        if self.wind_evel:
            if hasattr(self.wind_evel, 'to_alipay_dict'):
                params['wind_evel'] = self.wind_evel.to_alipay_dict()
            else:
                params['wind_evel'] = self.wind_evel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AiWeatherVo()
        if 'aqi_quality' in d:
            o.aqi_quality = d['aqi_quality']
        if 'aqi_score' in d:
            o.aqi_score = d['aqi_score']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'humidity' in d:
            o.humidity = d['humidity']
        if 'temperature' in d:
            o.temperature = d['temperature']
        if 'today_highest_temperature' in d:
            o.today_highest_temperature = d['today_highest_temperature']
        if 'today_lowest_temperature' in d:
            o.today_lowest_temperature = d['today_lowest_temperature']
        if 'weather' in d:
            o.weather = d['weather']
        if 'wind_direction' in d:
            o.wind_direction = d['wind_direction']
        if 'wind_evel' in d:
            o.wind_evel = d['wind_evel']
        return o


