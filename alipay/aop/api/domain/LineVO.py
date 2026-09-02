#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StationVO import StationVO


class LineVO(object):

    def __init__(self):
        self._color = None
        self._icon = None
        self._line_code = None
        self._name = None
        self._next_stations = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def line_code(self):
        return self._line_code

    @line_code.setter
    def line_code(self, value):
        self._line_code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def next_stations(self):
        return self._next_stations

    @next_stations.setter
    def next_stations(self, value):
        if isinstance(value, list):
            self._next_stations = list()
            for i in value:
                if isinstance(i, StationVO):
                    self._next_stations.append(i)
                else:
                    self._next_stations.append(StationVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.color:
            if hasattr(self.color, 'to_alipay_dict'):
                params['color'] = self.color.to_alipay_dict()
            else:
                params['color'] = self.color
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.line_code:
            if hasattr(self.line_code, 'to_alipay_dict'):
                params['line_code'] = self.line_code.to_alipay_dict()
            else:
                params['line_code'] = self.line_code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.next_stations:
            if isinstance(self.next_stations, list):
                for i in range(0, len(self.next_stations)):
                    element = self.next_stations[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.next_stations[i] = element.to_alipay_dict()
            if hasattr(self.next_stations, 'to_alipay_dict'):
                params['next_stations'] = self.next_stations.to_alipay_dict()
            else:
                params['next_stations'] = self.next_stations
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LineVO()
        if 'color' in d:
            o.color = d['color']
        if 'icon' in d:
            o.icon = d['icon']
        if 'line_code' in d:
            o.line_code = d['line_code']
        if 'name' in d:
            o.name = d['name']
        if 'next_stations' in d:
            o.next_stations = d['next_stations']
        return o


