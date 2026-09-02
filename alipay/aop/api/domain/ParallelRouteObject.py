#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ParallelRouteObject(object):

    def __init__(self):
        self._bus_route_name = None
        self._repeat_station_count = None
        self._repeat_station_detail = None
        self._station_index = None

    @property
    def bus_route_name(self):
        return self._bus_route_name

    @bus_route_name.setter
    def bus_route_name(self, value):
        self._bus_route_name = value
    @property
    def repeat_station_count(self):
        return self._repeat_station_count

    @repeat_station_count.setter
    def repeat_station_count(self, value):
        self._repeat_station_count = value
    @property
    def repeat_station_detail(self):
        return self._repeat_station_detail

    @repeat_station_detail.setter
    def repeat_station_detail(self, value):
        self._repeat_station_detail = value
    @property
    def station_index(self):
        return self._station_index

    @station_index.setter
    def station_index(self, value):
        self._station_index = value


    def to_alipay_dict(self):
        params = dict()
        if self.bus_route_name:
            if hasattr(self.bus_route_name, 'to_alipay_dict'):
                params['bus_route_name'] = self.bus_route_name.to_alipay_dict()
            else:
                params['bus_route_name'] = self.bus_route_name
        if self.repeat_station_count:
            if hasattr(self.repeat_station_count, 'to_alipay_dict'):
                params['repeat_station_count'] = self.repeat_station_count.to_alipay_dict()
            else:
                params['repeat_station_count'] = self.repeat_station_count
        if self.repeat_station_detail:
            if hasattr(self.repeat_station_detail, 'to_alipay_dict'):
                params['repeat_station_detail'] = self.repeat_station_detail.to_alipay_dict()
            else:
                params['repeat_station_detail'] = self.repeat_station_detail
        if self.station_index:
            if hasattr(self.station_index, 'to_alipay_dict'):
                params['station_index'] = self.station_index.to_alipay_dict()
            else:
                params['station_index'] = self.station_index
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ParallelRouteObject()
        if 'bus_route_name' in d:
            o.bus_route_name = d['bus_route_name']
        if 'repeat_station_count' in d:
            o.repeat_station_count = d['repeat_station_count']
        if 'repeat_station_detail' in d:
            o.repeat_station_detail = d['repeat_station_detail']
        if 'station_index' in d:
            o.station_index = d['station_index']
        return o


