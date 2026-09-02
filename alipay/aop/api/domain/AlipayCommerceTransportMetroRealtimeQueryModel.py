#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportMetroRealtimeQueryModel(object):

    def __init__(self):
        self._city_code = None
        self._line_code = None
        self._station_name = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def line_code(self):
        return self._line_code

    @line_code.setter
    def line_code(self, value):
        self._line_code = value
    @property
    def station_name(self):
        return self._station_name

    @station_name.setter
    def station_name(self, value):
        self._station_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.line_code:
            if hasattr(self.line_code, 'to_alipay_dict'):
                params['line_code'] = self.line_code.to_alipay_dict()
            else:
                params['line_code'] = self.line_code
        if self.station_name:
            if hasattr(self.station_name, 'to_alipay_dict'):
                params['station_name'] = self.station_name.to_alipay_dict()
            else:
                params['station_name'] = self.station_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportMetroRealtimeQueryModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'line_code' in d:
            o.line_code = d['line_code']
        if 'station_name' in d:
            o.station_name = d['station_name']
        return o


