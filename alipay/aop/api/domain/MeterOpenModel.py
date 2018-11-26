#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MeterOpenModel(object):

    def __init__(self):
        self._avg_speed = None
        self._calorie = None
        self._distance = None
        self._duration = None
        self._rep = None
        self._set = None
        self._type = None

    @property
    def avg_speed(self):
        return self._avg_speed

    @avg_speed.setter
    def avg_speed(self, value):
        self._avg_speed = value
    @property
    def calorie(self):
        return self._calorie

    @calorie.setter
    def calorie(self, value):
        self._calorie = value
    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def rep(self):
        return self._rep

    @rep.setter
    def rep(self, value):
        self._rep = value
    @property
    def set(self):
        return self._set

    @set.setter
    def set(self, value):
        self._set = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.avg_speed:
            if hasattr(self.avg_speed, 'to_alipay_dict'):
                params['avg_speed'] = self.avg_speed.to_alipay_dict()
            else:
                params['avg_speed'] = self.avg_speed
        if self.calorie:
            if hasattr(self.calorie, 'to_alipay_dict'):
                params['calorie'] = self.calorie.to_alipay_dict()
            else:
                params['calorie'] = self.calorie
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.rep:
            if hasattr(self.rep, 'to_alipay_dict'):
                params['rep'] = self.rep.to_alipay_dict()
            else:
                params['rep'] = self.rep
        if self.set:
            if hasattr(self.set, 'to_alipay_dict'):
                params['set'] = self.set.to_alipay_dict()
            else:
                params['set'] = self.set
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MeterOpenModel()
        if 'avg_speed' in d:
            o.avg_speed = d['avg_speed']
        if 'calorie' in d:
            o.calorie = d['calorie']
        if 'distance' in d:
            o.distance = d['distance']
        if 'duration' in d:
            o.duration = d['duration']
        if 'rep' in d:
            o.rep = d['rep']
        if 'set' in d:
            o.set = d['set']
        if 'type' in d:
            o.type = d['type']
        return o


