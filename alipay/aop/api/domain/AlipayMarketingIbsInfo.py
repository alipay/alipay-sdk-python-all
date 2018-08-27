#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingIbsInfo(object):

    def __init__(self):
        self._accuracy = None
        self._altitude = None
        self._latitude = None
        self._longitude = None
        self._time = None

    @property
    def accuracy(self):
        return self._accuracy

    @accuracy.setter
    def accuracy(self, value):
        self._accuracy = value
    @property
    def altitude(self):
        return self._altitude

    @altitude.setter
    def altitude(self, value):
        self._altitude = value
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
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value


    def to_alipay_dict(self):
        params = dict()
        if self.accuracy:
            if hasattr(self.accuracy, 'to_alipay_dict'):
                params['accuracy'] = self.accuracy.to_alipay_dict()
            else:
                params['accuracy'] = self.accuracy
        if self.altitude:
            if hasattr(self.altitude, 'to_alipay_dict'):
                params['altitude'] = self.altitude.to_alipay_dict()
            else:
                params['altitude'] = self.altitude
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
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingIbsInfo()
        if 'accuracy' in d:
            o.accuracy = d['accuracy']
        if 'altitude' in d:
            o.altitude = d['altitude']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'time' in d:
            o.time = d['time']
        return o


