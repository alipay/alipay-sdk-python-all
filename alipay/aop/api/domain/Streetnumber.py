#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Streetnumber(object):

    def __init__(self):
        self._direction = None
        self._distance = None
        self._location = None
        self._number = None
        self._street = None

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value
    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, value):
        self._street = value


    def to_alipay_dict(self):
        params = dict()
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        if self.location:
            if hasattr(self.location, 'to_alipay_dict'):
                params['location'] = self.location.to_alipay_dict()
            else:
                params['location'] = self.location
        if self.number:
            if hasattr(self.number, 'to_alipay_dict'):
                params['number'] = self.number.to_alipay_dict()
            else:
                params['number'] = self.number
        if self.street:
            if hasattr(self.street, 'to_alipay_dict'):
                params['street'] = self.street.to_alipay_dict()
            else:
                params['street'] = self.street
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Streetnumber()
        if 'direction' in d:
            o.direction = d['direction']
        if 'distance' in d:
            o.distance = d['distance']
        if 'location' in d:
            o.location = d['location']
        if 'number' in d:
            o.number = d['number']
        if 'street' in d:
            o.street = d['street']
        return o


