#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GPSLocationInfo(object):

    def __init__(self):
        self._accuracy = None
        self._direction = None
        self._height = None
        self._latitude = None
        self._longitude = None
        self._speed = None

    @property
    def accuracy(self):
        return self._accuracy

    @accuracy.setter
    def accuracy(self, value):
        self._accuracy = value
    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
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
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value


    def to_alipay_dict(self):
        params = dict()
        if self.accuracy:
            if hasattr(self.accuracy, 'to_alipay_dict'):
                params['accuracy'] = self.accuracy.to_alipay_dict()
            else:
                params['accuracy'] = self.accuracy
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
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
        if self.speed:
            if hasattr(self.speed, 'to_alipay_dict'):
                params['speed'] = self.speed.to_alipay_dict()
            else:
                params['speed'] = self.speed
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GPSLocationInfo()
        if 'accuracy' in d:
            o.accuracy = d['accuracy']
        if 'direction' in d:
            o.direction = d['direction']
        if 'height' in d:
            o.height = d['height']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'speed' in d:
            o.speed = d['speed']
        return o


