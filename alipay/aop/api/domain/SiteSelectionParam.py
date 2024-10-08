#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LngAndLatParam import LngAndLatParam


class SiteSelectionParam(object):

    def __init__(self):
        self._city_code = None
        self._date_from = None
        self._date_to = None
        self._index_list = None
        self._lng_lat_list = None
        self._min_parking_period = None
        self._parking_days = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def date_from(self):
        return self._date_from

    @date_from.setter
    def date_from(self, value):
        self._date_from = value
    @property
    def date_to(self):
        return self._date_to

    @date_to.setter
    def date_to(self, value):
        self._date_to = value
    @property
    def index_list(self):
        return self._index_list

    @index_list.setter
    def index_list(self, value):
        if isinstance(value, list):
            self._index_list = list()
            for i in value:
                self._index_list.append(i)
    @property
    def lng_lat_list(self):
        return self._lng_lat_list

    @lng_lat_list.setter
    def lng_lat_list(self, value):
        if isinstance(value, list):
            self._lng_lat_list = list()
            for i in value:
                if isinstance(i, LngAndLatParam):
                    self._lng_lat_list.append(i)
                else:
                    self._lng_lat_list.append(LngAndLatParam.from_alipay_dict(i))
    @property
    def min_parking_period(self):
        return self._min_parking_period

    @min_parking_period.setter
    def min_parking_period(self, value):
        self._min_parking_period = value
    @property
    def parking_days(self):
        return self._parking_days

    @parking_days.setter
    def parking_days(self, value):
        self._parking_days = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.date_from:
            if hasattr(self.date_from, 'to_alipay_dict'):
                params['date_from'] = self.date_from.to_alipay_dict()
            else:
                params['date_from'] = self.date_from
        if self.date_to:
            if hasattr(self.date_to, 'to_alipay_dict'):
                params['date_to'] = self.date_to.to_alipay_dict()
            else:
                params['date_to'] = self.date_to
        if self.index_list:
            if isinstance(self.index_list, list):
                for i in range(0, len(self.index_list)):
                    element = self.index_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.index_list[i] = element.to_alipay_dict()
            if hasattr(self.index_list, 'to_alipay_dict'):
                params['index_list'] = self.index_list.to_alipay_dict()
            else:
                params['index_list'] = self.index_list
        if self.lng_lat_list:
            if isinstance(self.lng_lat_list, list):
                for i in range(0, len(self.lng_lat_list)):
                    element = self.lng_lat_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.lng_lat_list[i] = element.to_alipay_dict()
            if hasattr(self.lng_lat_list, 'to_alipay_dict'):
                params['lng_lat_list'] = self.lng_lat_list.to_alipay_dict()
            else:
                params['lng_lat_list'] = self.lng_lat_list
        if self.min_parking_period:
            if hasattr(self.min_parking_period, 'to_alipay_dict'):
                params['min_parking_period'] = self.min_parking_period.to_alipay_dict()
            else:
                params['min_parking_period'] = self.min_parking_period
        if self.parking_days:
            if hasattr(self.parking_days, 'to_alipay_dict'):
                params['parking_days'] = self.parking_days.to_alipay_dict()
            else:
                params['parking_days'] = self.parking_days
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SiteSelectionParam()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'date_from' in d:
            o.date_from = d['date_from']
        if 'date_to' in d:
            o.date_to = d['date_to']
        if 'index_list' in d:
            o.index_list = d['index_list']
        if 'lng_lat_list' in d:
            o.lng_lat_list = d['lng_lat_list']
        if 'min_parking_period' in d:
            o.min_parking_period = d['min_parking_period']
        if 'parking_days' in d:
            o.parking_days = d['parking_days']
        return o


