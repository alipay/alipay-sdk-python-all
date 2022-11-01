#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AgWeatherMonthlyStats(object):

    def __init__(self):
        self._acc_precipitation_anomaly = None
        self._acc_precipitation_month = None
        self._acc_precipitation_year = None
        self._avg_temperature_anomaly = None
        self._avg_temperature_month = None
        self._avg_temperature_year = None
        self._create_date = None
        self._soil_moisture_anomaly = None
        self._soil_moisture_month = None
        self._soil_moisture_year = None
        self._update_date = None
        self._wind_speed_anomaly = None
        self._wind_speed_month = None
        self._wind_speed_year = None

    @property
    def acc_precipitation_anomaly(self):
        return self._acc_precipitation_anomaly

    @acc_precipitation_anomaly.setter
    def acc_precipitation_anomaly(self, value):
        self._acc_precipitation_anomaly = value
    @property
    def acc_precipitation_month(self):
        return self._acc_precipitation_month

    @acc_precipitation_month.setter
    def acc_precipitation_month(self, value):
        self._acc_precipitation_month = value
    @property
    def acc_precipitation_year(self):
        return self._acc_precipitation_year

    @acc_precipitation_year.setter
    def acc_precipitation_year(self, value):
        self._acc_precipitation_year = value
    @property
    def avg_temperature_anomaly(self):
        return self._avg_temperature_anomaly

    @avg_temperature_anomaly.setter
    def avg_temperature_anomaly(self, value):
        self._avg_temperature_anomaly = value
    @property
    def avg_temperature_month(self):
        return self._avg_temperature_month

    @avg_temperature_month.setter
    def avg_temperature_month(self, value):
        self._avg_temperature_month = value
    @property
    def avg_temperature_year(self):
        return self._avg_temperature_year

    @avg_temperature_year.setter
    def avg_temperature_year(self, value):
        self._avg_temperature_year = value
    @property
    def create_date(self):
        return self._create_date

    @create_date.setter
    def create_date(self, value):
        self._create_date = value
    @property
    def soil_moisture_anomaly(self):
        return self._soil_moisture_anomaly

    @soil_moisture_anomaly.setter
    def soil_moisture_anomaly(self, value):
        self._soil_moisture_anomaly = value
    @property
    def soil_moisture_month(self):
        return self._soil_moisture_month

    @soil_moisture_month.setter
    def soil_moisture_month(self, value):
        self._soil_moisture_month = value
    @property
    def soil_moisture_year(self):
        return self._soil_moisture_year

    @soil_moisture_year.setter
    def soil_moisture_year(self, value):
        self._soil_moisture_year = value
    @property
    def update_date(self):
        return self._update_date

    @update_date.setter
    def update_date(self, value):
        self._update_date = value
    @property
    def wind_speed_anomaly(self):
        return self._wind_speed_anomaly

    @wind_speed_anomaly.setter
    def wind_speed_anomaly(self, value):
        self._wind_speed_anomaly = value
    @property
    def wind_speed_month(self):
        return self._wind_speed_month

    @wind_speed_month.setter
    def wind_speed_month(self, value):
        self._wind_speed_month = value
    @property
    def wind_speed_year(self):
        return self._wind_speed_year

    @wind_speed_year.setter
    def wind_speed_year(self, value):
        self._wind_speed_year = value


    def to_alipay_dict(self):
        params = dict()
        if self.acc_precipitation_anomaly:
            if hasattr(self.acc_precipitation_anomaly, 'to_alipay_dict'):
                params['acc_precipitation_anomaly'] = self.acc_precipitation_anomaly.to_alipay_dict()
            else:
                params['acc_precipitation_anomaly'] = self.acc_precipitation_anomaly
        if self.acc_precipitation_month:
            if hasattr(self.acc_precipitation_month, 'to_alipay_dict'):
                params['acc_precipitation_month'] = self.acc_precipitation_month.to_alipay_dict()
            else:
                params['acc_precipitation_month'] = self.acc_precipitation_month
        if self.acc_precipitation_year:
            if hasattr(self.acc_precipitation_year, 'to_alipay_dict'):
                params['acc_precipitation_year'] = self.acc_precipitation_year.to_alipay_dict()
            else:
                params['acc_precipitation_year'] = self.acc_precipitation_year
        if self.avg_temperature_anomaly:
            if hasattr(self.avg_temperature_anomaly, 'to_alipay_dict'):
                params['avg_temperature_anomaly'] = self.avg_temperature_anomaly.to_alipay_dict()
            else:
                params['avg_temperature_anomaly'] = self.avg_temperature_anomaly
        if self.avg_temperature_month:
            if hasattr(self.avg_temperature_month, 'to_alipay_dict'):
                params['avg_temperature_month'] = self.avg_temperature_month.to_alipay_dict()
            else:
                params['avg_temperature_month'] = self.avg_temperature_month
        if self.avg_temperature_year:
            if hasattr(self.avg_temperature_year, 'to_alipay_dict'):
                params['avg_temperature_year'] = self.avg_temperature_year.to_alipay_dict()
            else:
                params['avg_temperature_year'] = self.avg_temperature_year
        if self.create_date:
            if hasattr(self.create_date, 'to_alipay_dict'):
                params['create_date'] = self.create_date.to_alipay_dict()
            else:
                params['create_date'] = self.create_date
        if self.soil_moisture_anomaly:
            if hasattr(self.soil_moisture_anomaly, 'to_alipay_dict'):
                params['soil_moisture_anomaly'] = self.soil_moisture_anomaly.to_alipay_dict()
            else:
                params['soil_moisture_anomaly'] = self.soil_moisture_anomaly
        if self.soil_moisture_month:
            if hasattr(self.soil_moisture_month, 'to_alipay_dict'):
                params['soil_moisture_month'] = self.soil_moisture_month.to_alipay_dict()
            else:
                params['soil_moisture_month'] = self.soil_moisture_month
        if self.soil_moisture_year:
            if hasattr(self.soil_moisture_year, 'to_alipay_dict'):
                params['soil_moisture_year'] = self.soil_moisture_year.to_alipay_dict()
            else:
                params['soil_moisture_year'] = self.soil_moisture_year
        if self.update_date:
            if hasattr(self.update_date, 'to_alipay_dict'):
                params['update_date'] = self.update_date.to_alipay_dict()
            else:
                params['update_date'] = self.update_date
        if self.wind_speed_anomaly:
            if hasattr(self.wind_speed_anomaly, 'to_alipay_dict'):
                params['wind_speed_anomaly'] = self.wind_speed_anomaly.to_alipay_dict()
            else:
                params['wind_speed_anomaly'] = self.wind_speed_anomaly
        if self.wind_speed_month:
            if hasattr(self.wind_speed_month, 'to_alipay_dict'):
                params['wind_speed_month'] = self.wind_speed_month.to_alipay_dict()
            else:
                params['wind_speed_month'] = self.wind_speed_month
        if self.wind_speed_year:
            if hasattr(self.wind_speed_year, 'to_alipay_dict'):
                params['wind_speed_year'] = self.wind_speed_year.to_alipay_dict()
            else:
                params['wind_speed_year'] = self.wind_speed_year
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AgWeatherMonthlyStats()
        if 'acc_precipitation_anomaly' in d:
            o.acc_precipitation_anomaly = d['acc_precipitation_anomaly']
        if 'acc_precipitation_month' in d:
            o.acc_precipitation_month = d['acc_precipitation_month']
        if 'acc_precipitation_year' in d:
            o.acc_precipitation_year = d['acc_precipitation_year']
        if 'avg_temperature_anomaly' in d:
            o.avg_temperature_anomaly = d['avg_temperature_anomaly']
        if 'avg_temperature_month' in d:
            o.avg_temperature_month = d['avg_temperature_month']
        if 'avg_temperature_year' in d:
            o.avg_temperature_year = d['avg_temperature_year']
        if 'create_date' in d:
            o.create_date = d['create_date']
        if 'soil_moisture_anomaly' in d:
            o.soil_moisture_anomaly = d['soil_moisture_anomaly']
        if 'soil_moisture_month' in d:
            o.soil_moisture_month = d['soil_moisture_month']
        if 'soil_moisture_year' in d:
            o.soil_moisture_year = d['soil_moisture_year']
        if 'update_date' in d:
            o.update_date = d['update_date']
        if 'wind_speed_anomaly' in d:
            o.wind_speed_anomaly = d['wind_speed_anomaly']
        if 'wind_speed_month' in d:
            o.wind_speed_month = d['wind_speed_month']
        if 'wind_speed_year' in d:
            o.wind_speed_year = d['wind_speed_year']
        return o


