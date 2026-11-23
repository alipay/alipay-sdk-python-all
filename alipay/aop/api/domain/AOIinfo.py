#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AOIinfo(object):

    def __init__(self):
        self._adcode = None
        self._area = None
        self._distance = None
        self._id = None
        self._location = None
        self._name = None

    @property
    def adcode(self):
        return self._adcode

    @adcode.setter
    def adcode(self, value):
        self._adcode = value
    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.adcode:
            if hasattr(self.adcode, 'to_alipay_dict'):
                params['adcode'] = self.adcode.to_alipay_dict()
            else:
                params['adcode'] = self.adcode
        if self.area:
            if hasattr(self.area, 'to_alipay_dict'):
                params['area'] = self.area.to_alipay_dict()
            else:
                params['area'] = self.area
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.location:
            if hasattr(self.location, 'to_alipay_dict'):
                params['location'] = self.location.to_alipay_dict()
            else:
                params['location'] = self.location
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AOIinfo()
        if 'adcode' in d:
            o.adcode = d['adcode']
        if 'area' in d:
            o.area = d['area']
        if 'distance' in d:
            o.distance = d['distance']
        if 'id' in d:
            o.id = d['id']
        if 'location' in d:
            o.location = d['location']
        if 'name' in d:
            o.name = d['name']
        return o


