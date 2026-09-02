#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtcTollfeeQueryModel(object):

    def __init__(self):
        self._caller_id = None
        self._end_latitude = None
        self._end_longitude = None
        self._end_station_name = None
        self._start_latitude = None
        self._start_longitude = None
        self._start_station_name = None

    @property
    def caller_id(self):
        return self._caller_id

    @caller_id.setter
    def caller_id(self, value):
        self._caller_id = value
    @property
    def end_latitude(self):
        return self._end_latitude

    @end_latitude.setter
    def end_latitude(self, value):
        self._end_latitude = value
    @property
    def end_longitude(self):
        return self._end_longitude

    @end_longitude.setter
    def end_longitude(self, value):
        self._end_longitude = value
    @property
    def end_station_name(self):
        return self._end_station_name

    @end_station_name.setter
    def end_station_name(self, value):
        self._end_station_name = value
    @property
    def start_latitude(self):
        return self._start_latitude

    @start_latitude.setter
    def start_latitude(self, value):
        self._start_latitude = value
    @property
    def start_longitude(self):
        return self._start_longitude

    @start_longitude.setter
    def start_longitude(self, value):
        self._start_longitude = value
    @property
    def start_station_name(self):
        return self._start_station_name

    @start_station_name.setter
    def start_station_name(self, value):
        self._start_station_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.caller_id:
            if hasattr(self.caller_id, 'to_alipay_dict'):
                params['caller_id'] = self.caller_id.to_alipay_dict()
            else:
                params['caller_id'] = self.caller_id
        if self.end_latitude:
            if hasattr(self.end_latitude, 'to_alipay_dict'):
                params['end_latitude'] = self.end_latitude.to_alipay_dict()
            else:
                params['end_latitude'] = self.end_latitude
        if self.end_longitude:
            if hasattr(self.end_longitude, 'to_alipay_dict'):
                params['end_longitude'] = self.end_longitude.to_alipay_dict()
            else:
                params['end_longitude'] = self.end_longitude
        if self.end_station_name:
            if hasattr(self.end_station_name, 'to_alipay_dict'):
                params['end_station_name'] = self.end_station_name.to_alipay_dict()
            else:
                params['end_station_name'] = self.end_station_name
        if self.start_latitude:
            if hasattr(self.start_latitude, 'to_alipay_dict'):
                params['start_latitude'] = self.start_latitude.to_alipay_dict()
            else:
                params['start_latitude'] = self.start_latitude
        if self.start_longitude:
            if hasattr(self.start_longitude, 'to_alipay_dict'):
                params['start_longitude'] = self.start_longitude.to_alipay_dict()
            else:
                params['start_longitude'] = self.start_longitude
        if self.start_station_name:
            if hasattr(self.start_station_name, 'to_alipay_dict'):
                params['start_station_name'] = self.start_station_name.to_alipay_dict()
            else:
                params['start_station_name'] = self.start_station_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcTollfeeQueryModel()
        if 'caller_id' in d:
            o.caller_id = d['caller_id']
        if 'end_latitude' in d:
            o.end_latitude = d['end_latitude']
        if 'end_longitude' in d:
            o.end_longitude = d['end_longitude']
        if 'end_station_name' in d:
            o.end_station_name = d['end_station_name']
        if 'start_latitude' in d:
            o.start_latitude = d['start_latitude']
        if 'start_longitude' in d:
            o.start_longitude = d['start_longitude']
        if 'start_station_name' in d:
            o.start_station_name = d['start_station_name']
        return o


