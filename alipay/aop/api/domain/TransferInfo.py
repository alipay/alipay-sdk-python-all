#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TransferInfo(object):

    def __init__(self):
        self._transfer_airport = None
        self._transfer_airport_name = None
        self._transfer_city = None
        self._transfer_city_name = None
        self._transfer_time = None

    @property
    def transfer_airport(self):
        return self._transfer_airport

    @transfer_airport.setter
    def transfer_airport(self, value):
        self._transfer_airport = value
    @property
    def transfer_airport_name(self):
        return self._transfer_airport_name

    @transfer_airport_name.setter
    def transfer_airport_name(self, value):
        self._transfer_airport_name = value
    @property
    def transfer_city(self):
        return self._transfer_city

    @transfer_city.setter
    def transfer_city(self, value):
        self._transfer_city = value
    @property
    def transfer_city_name(self):
        return self._transfer_city_name

    @transfer_city_name.setter
    def transfer_city_name(self, value):
        self._transfer_city_name = value
    @property
    def transfer_time(self):
        return self._transfer_time

    @transfer_time.setter
    def transfer_time(self, value):
        self._transfer_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.transfer_airport:
            if hasattr(self.transfer_airport, 'to_alipay_dict'):
                params['transfer_airport'] = self.transfer_airport.to_alipay_dict()
            else:
                params['transfer_airport'] = self.transfer_airport
        if self.transfer_airport_name:
            if hasattr(self.transfer_airport_name, 'to_alipay_dict'):
                params['transfer_airport_name'] = self.transfer_airport_name.to_alipay_dict()
            else:
                params['transfer_airport_name'] = self.transfer_airport_name
        if self.transfer_city:
            if hasattr(self.transfer_city, 'to_alipay_dict'):
                params['transfer_city'] = self.transfer_city.to_alipay_dict()
            else:
                params['transfer_city'] = self.transfer_city
        if self.transfer_city_name:
            if hasattr(self.transfer_city_name, 'to_alipay_dict'):
                params['transfer_city_name'] = self.transfer_city_name.to_alipay_dict()
            else:
                params['transfer_city_name'] = self.transfer_city_name
        if self.transfer_time:
            if hasattr(self.transfer_time, 'to_alipay_dict'):
                params['transfer_time'] = self.transfer_time.to_alipay_dict()
            else:
                params['transfer_time'] = self.transfer_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TransferInfo()
        if 'transfer_airport' in d:
            o.transfer_airport = d['transfer_airport']
        if 'transfer_airport_name' in d:
            o.transfer_airport_name = d['transfer_airport_name']
        if 'transfer_city' in d:
            o.transfer_city = d['transfer_city']
        if 'transfer_city_name' in d:
            o.transfer_city_name = d['transfer_city_name']
        if 'transfer_time' in d:
            o.transfer_time = d['transfer_time']
        return o


