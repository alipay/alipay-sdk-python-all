#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StationVO(object):

    def __init__(self):
        self._global_station_code = None
        self._name = None
        self._order = None
        self._station_code = None

    @property
    def global_station_code(self):
        return self._global_station_code

    @global_station_code.setter
    def global_station_code(self, value):
        self._global_station_code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        self._order = value
    @property
    def station_code(self):
        return self._station_code

    @station_code.setter
    def station_code(self, value):
        self._station_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.global_station_code:
            if hasattr(self.global_station_code, 'to_alipay_dict'):
                params['global_station_code'] = self.global_station_code.to_alipay_dict()
            else:
                params['global_station_code'] = self.global_station_code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.order:
            if hasattr(self.order, 'to_alipay_dict'):
                params['order'] = self.order.to_alipay_dict()
            else:
                params['order'] = self.order
        if self.station_code:
            if hasattr(self.station_code, 'to_alipay_dict'):
                params['station_code'] = self.station_code.to_alipay_dict()
            else:
                params['station_code'] = self.station_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StationVO()
        if 'global_station_code' in d:
            o.global_station_code = d['global_station_code']
        if 'name' in d:
            o.name = d['name']
        if 'order' in d:
            o.order = d['order']
        if 'station_code' in d:
            o.station_code = d['station_code']
        return o


