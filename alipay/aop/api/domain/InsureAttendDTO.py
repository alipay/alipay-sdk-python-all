#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsureAttendDTO(object):

    def __init__(self):
        self._attend_time = None
        self._attend_type = None
        self._back_url = None
        self._coordinates = None
        self._distance = None

    @property
    def attend_time(self):
        return self._attend_time

    @attend_time.setter
    def attend_time(self, value):
        self._attend_time = value
    @property
    def attend_type(self):
        return self._attend_type

    @attend_type.setter
    def attend_type(self, value):
        self._attend_type = value
    @property
    def back_url(self):
        return self._back_url

    @back_url.setter
    def back_url(self, value):
        self._back_url = value
    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, value):
        self._coordinates = value
    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value


    def to_alipay_dict(self):
        params = dict()
        if self.attend_time:
            if hasattr(self.attend_time, 'to_alipay_dict'):
                params['attend_time'] = self.attend_time.to_alipay_dict()
            else:
                params['attend_time'] = self.attend_time
        if self.attend_type:
            if hasattr(self.attend_type, 'to_alipay_dict'):
                params['attend_type'] = self.attend_type.to_alipay_dict()
            else:
                params['attend_type'] = self.attend_type
        if self.back_url:
            if hasattr(self.back_url, 'to_alipay_dict'):
                params['back_url'] = self.back_url.to_alipay_dict()
            else:
                params['back_url'] = self.back_url
        if self.coordinates:
            if hasattr(self.coordinates, 'to_alipay_dict'):
                params['coordinates'] = self.coordinates.to_alipay_dict()
            else:
                params['coordinates'] = self.coordinates
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsureAttendDTO()
        if 'attend_time' in d:
            o.attend_time = d['attend_time']
        if 'attend_type' in d:
            o.attend_type = d['attend_type']
        if 'back_url' in d:
            o.back_url = d['back_url']
        if 'coordinates' in d:
            o.coordinates = d['coordinates']
        if 'distance' in d:
            o.distance = d['distance']
        return o


