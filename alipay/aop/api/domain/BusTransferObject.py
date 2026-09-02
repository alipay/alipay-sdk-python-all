#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusTransferObject(object):

    def __init__(self):
        self._bus_transfer_platform = None
        self._entrance_exit_code = None
        self._entrance_exit_name = None
        self._metro_station_code = None
        self._metro_station_name = None
        self._park_route_count = None
        self._park_route_detail = None
        self._station_index = None

    @property
    def bus_transfer_platform(self):
        return self._bus_transfer_platform

    @bus_transfer_platform.setter
    def bus_transfer_platform(self, value):
        self._bus_transfer_platform = value
    @property
    def entrance_exit_code(self):
        return self._entrance_exit_code

    @entrance_exit_code.setter
    def entrance_exit_code(self, value):
        self._entrance_exit_code = value
    @property
    def entrance_exit_name(self):
        return self._entrance_exit_name

    @entrance_exit_name.setter
    def entrance_exit_name(self, value):
        self._entrance_exit_name = value
    @property
    def metro_station_code(self):
        return self._metro_station_code

    @metro_station_code.setter
    def metro_station_code(self, value):
        self._metro_station_code = value
    @property
    def metro_station_name(self):
        return self._metro_station_name

    @metro_station_name.setter
    def metro_station_name(self, value):
        self._metro_station_name = value
    @property
    def park_route_count(self):
        return self._park_route_count

    @park_route_count.setter
    def park_route_count(self, value):
        self._park_route_count = value
    @property
    def park_route_detail(self):
        return self._park_route_detail

    @park_route_detail.setter
    def park_route_detail(self, value):
        self._park_route_detail = value
    @property
    def station_index(self):
        return self._station_index

    @station_index.setter
    def station_index(self, value):
        self._station_index = value


    def to_alipay_dict(self):
        params = dict()
        if self.bus_transfer_platform:
            if hasattr(self.bus_transfer_platform, 'to_alipay_dict'):
                params['bus_transfer_platform'] = self.bus_transfer_platform.to_alipay_dict()
            else:
                params['bus_transfer_platform'] = self.bus_transfer_platform
        if self.entrance_exit_code:
            if hasattr(self.entrance_exit_code, 'to_alipay_dict'):
                params['entrance_exit_code'] = self.entrance_exit_code.to_alipay_dict()
            else:
                params['entrance_exit_code'] = self.entrance_exit_code
        if self.entrance_exit_name:
            if hasattr(self.entrance_exit_name, 'to_alipay_dict'):
                params['entrance_exit_name'] = self.entrance_exit_name.to_alipay_dict()
            else:
                params['entrance_exit_name'] = self.entrance_exit_name
        if self.metro_station_code:
            if hasattr(self.metro_station_code, 'to_alipay_dict'):
                params['metro_station_code'] = self.metro_station_code.to_alipay_dict()
            else:
                params['metro_station_code'] = self.metro_station_code
        if self.metro_station_name:
            if hasattr(self.metro_station_name, 'to_alipay_dict'):
                params['metro_station_name'] = self.metro_station_name.to_alipay_dict()
            else:
                params['metro_station_name'] = self.metro_station_name
        if self.park_route_count:
            if hasattr(self.park_route_count, 'to_alipay_dict'):
                params['park_route_count'] = self.park_route_count.to_alipay_dict()
            else:
                params['park_route_count'] = self.park_route_count
        if self.park_route_detail:
            if hasattr(self.park_route_detail, 'to_alipay_dict'):
                params['park_route_detail'] = self.park_route_detail.to_alipay_dict()
            else:
                params['park_route_detail'] = self.park_route_detail
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
        o = BusTransferObject()
        if 'bus_transfer_platform' in d:
            o.bus_transfer_platform = d['bus_transfer_platform']
        if 'entrance_exit_code' in d:
            o.entrance_exit_code = d['entrance_exit_code']
        if 'entrance_exit_name' in d:
            o.entrance_exit_name = d['entrance_exit_name']
        if 'metro_station_code' in d:
            o.metro_station_code = d['metro_station_code']
        if 'metro_station_name' in d:
            o.metro_station_name = d['metro_station_name']
        if 'park_route_count' in d:
            o.park_route_count = d['park_route_count']
        if 'park_route_detail' in d:
            o.park_route_detail = d['park_route_detail']
        if 'station_index' in d:
            o.station_index = d['station_index']
        return o


