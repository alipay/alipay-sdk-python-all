#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScenicExtInfo import ScenicExtInfo


class TrafficProductInfo(object):

    def __init__(self):
        self._departure = None
        self._departure_gate = None
        self._destination = None
        self._ext_info = None
        self._latitude = None
        self._longitude = None
        self._route_name = None
        self._route_no = None
        self._seat_type = None
        self._traffic_no = None
        self._traffic_type = None

    @property
    def departure(self):
        return self._departure

    @departure.setter
    def departure(self, value):
        self._departure = value
    @property
    def departure_gate(self):
        return self._departure_gate

    @departure_gate.setter
    def departure_gate(self, value):
        self._departure_gate = value
    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        self._destination = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, ScenicExtInfo):
            self._ext_info = value
        else:
            self._ext_info = ScenicExtInfo.from_alipay_dict(value)
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
    def route_name(self):
        return self._route_name

    @route_name.setter
    def route_name(self, value):
        self._route_name = value
    @property
    def route_no(self):
        return self._route_no

    @route_no.setter
    def route_no(self, value):
        self._route_no = value
    @property
    def seat_type(self):
        return self._seat_type

    @seat_type.setter
    def seat_type(self, value):
        self._seat_type = value
    @property
    def traffic_no(self):
        return self._traffic_no

    @traffic_no.setter
    def traffic_no(self, value):
        self._traffic_no = value
    @property
    def traffic_type(self):
        return self._traffic_type

    @traffic_type.setter
    def traffic_type(self, value):
        self._traffic_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.departure:
            if hasattr(self.departure, 'to_alipay_dict'):
                params['departure'] = self.departure.to_alipay_dict()
            else:
                params['departure'] = self.departure
        if self.departure_gate:
            if hasattr(self.departure_gate, 'to_alipay_dict'):
                params['departure_gate'] = self.departure_gate.to_alipay_dict()
            else:
                params['departure_gate'] = self.departure_gate
        if self.destination:
            if hasattr(self.destination, 'to_alipay_dict'):
                params['destination'] = self.destination.to_alipay_dict()
            else:
                params['destination'] = self.destination
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
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
        if self.route_name:
            if hasattr(self.route_name, 'to_alipay_dict'):
                params['route_name'] = self.route_name.to_alipay_dict()
            else:
                params['route_name'] = self.route_name
        if self.route_no:
            if hasattr(self.route_no, 'to_alipay_dict'):
                params['route_no'] = self.route_no.to_alipay_dict()
            else:
                params['route_no'] = self.route_no
        if self.seat_type:
            if hasattr(self.seat_type, 'to_alipay_dict'):
                params['seat_type'] = self.seat_type.to_alipay_dict()
            else:
                params['seat_type'] = self.seat_type
        if self.traffic_no:
            if hasattr(self.traffic_no, 'to_alipay_dict'):
                params['traffic_no'] = self.traffic_no.to_alipay_dict()
            else:
                params['traffic_no'] = self.traffic_no
        if self.traffic_type:
            if hasattr(self.traffic_type, 'to_alipay_dict'):
                params['traffic_type'] = self.traffic_type.to_alipay_dict()
            else:
                params['traffic_type'] = self.traffic_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TrafficProductInfo()
        if 'departure' in d:
            o.departure = d['departure']
        if 'departure_gate' in d:
            o.departure_gate = d['departure_gate']
        if 'destination' in d:
            o.destination = d['destination']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'route_name' in d:
            o.route_name = d['route_name']
        if 'route_no' in d:
            o.route_no = d['route_no']
        if 'seat_type' in d:
            o.seat_type = d['seat_type']
        if 'traffic_no' in d:
            o.traffic_no = d['traffic_no']
        if 'traffic_type' in d:
            o.traffic_type = d['traffic_type']
        return o


