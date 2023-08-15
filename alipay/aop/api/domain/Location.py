#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TipInfo import TipInfo


class Location(object):

    def __init__(self):
        self._angle = None
        self._lat = None
        self._lon = None
        self._name = None
        self._tips = None

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = value
    @property
    def lat(self):
        return self._lat

    @lat.setter
    def lat(self, value):
        self._lat = value
    @property
    def lon(self):
        return self._lon

    @lon.setter
    def lon(self, value):
        self._lon = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def tips(self):
        return self._tips

    @tips.setter
    def tips(self, value):
        if isinstance(value, TipInfo):
            self._tips = value
        else:
            self._tips = TipInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.angle:
            if hasattr(self.angle, 'to_alipay_dict'):
                params['angle'] = self.angle.to_alipay_dict()
            else:
                params['angle'] = self.angle
        if self.lat:
            if hasattr(self.lat, 'to_alipay_dict'):
                params['lat'] = self.lat.to_alipay_dict()
            else:
                params['lat'] = self.lat
        if self.lon:
            if hasattr(self.lon, 'to_alipay_dict'):
                params['lon'] = self.lon.to_alipay_dict()
            else:
                params['lon'] = self.lon
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.tips:
            if hasattr(self.tips, 'to_alipay_dict'):
                params['tips'] = self.tips.to_alipay_dict()
            else:
                params['tips'] = self.tips
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Location()
        if 'angle' in d:
            o.angle = d['angle']
        if 'lat' in d:
            o.lat = d['lat']
        if 'lon' in d:
            o.lon = d['lon']
        if 'name' in d:
            o.name = d['name']
        if 'tips' in d:
            o.tips = d['tips']
        return o


