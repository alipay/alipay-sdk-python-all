#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Roadinter(object):

    def __init__(self):
        self._direction = None
        self._distance = None
        self._first_id = None
        self._first_name = None
        self._location = None
        self._second_id = None
        self._second_name = None

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
    def first_id(self):
        return self._first_id

    @first_id.setter
    def first_id(self, value):
        self._first_id = value
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
    @property
    def second_id(self):
        return self._second_id

    @second_id.setter
    def second_id(self, value):
        self._second_id = value
    @property
    def second_name(self):
        return self._second_name

    @second_name.setter
    def second_name(self, value):
        self._second_name = value


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
        if self.first_id:
            if hasattr(self.first_id, 'to_alipay_dict'):
                params['first_id'] = self.first_id.to_alipay_dict()
            else:
                params['first_id'] = self.first_id
        if self.first_name:
            if hasattr(self.first_name, 'to_alipay_dict'):
                params['first_name'] = self.first_name.to_alipay_dict()
            else:
                params['first_name'] = self.first_name
        if self.location:
            if hasattr(self.location, 'to_alipay_dict'):
                params['location'] = self.location.to_alipay_dict()
            else:
                params['location'] = self.location
        if self.second_id:
            if hasattr(self.second_id, 'to_alipay_dict'):
                params['second_id'] = self.second_id.to_alipay_dict()
            else:
                params['second_id'] = self.second_id
        if self.second_name:
            if hasattr(self.second_name, 'to_alipay_dict'):
                params['second_name'] = self.second_name.to_alipay_dict()
            else:
                params['second_name'] = self.second_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Roadinter()
        if 'direction' in d:
            o.direction = d['direction']
        if 'distance' in d:
            o.distance = d['distance']
        if 'first_id' in d:
            o.first_id = d['first_id']
        if 'first_name' in d:
            o.first_name = d['first_name']
        if 'location' in d:
            o.location = d['location']
        if 'second_id' in d:
            o.second_id = d['second_id']
        if 'second_name' in d:
            o.second_name = d['second_name']
        return o


