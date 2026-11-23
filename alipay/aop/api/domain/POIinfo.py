#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class POIinfo(object):

    def __init__(self):
        self._address = None
        self._businessarea = None
        self._direction = None
        self._distance = None
        self._id = None
        self._location = None
        self._name = None
        self._tel = None
        self._type = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def businessarea(self):
        return self._businessarea

    @businessarea.setter
    def businessarea(self, value):
        self._businessarea = value
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
    @property
    def tel(self):
        return self._tel

    @tel.setter
    def tel(self, value):
        self._tel = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.businessarea:
            if hasattr(self.businessarea, 'to_alipay_dict'):
                params['businessarea'] = self.businessarea.to_alipay_dict()
            else:
                params['businessarea'] = self.businessarea
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
        if self.tel:
            if hasattr(self.tel, 'to_alipay_dict'):
                params['tel'] = self.tel.to_alipay_dict()
            else:
                params['tel'] = self.tel
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
        o = POIinfo()
        if 'address' in d:
            o.address = d['address']
        if 'businessarea' in d:
            o.businessarea = d['businessarea']
        if 'direction' in d:
            o.direction = d['direction']
        if 'distance' in d:
            o.distance = d['distance']
        if 'id' in d:
            o.id = d['id']
        if 'location' in d:
            o.location = d['location']
        if 'name' in d:
            o.name = d['name']
        if 'tel' in d:
            o.tel = d['tel']
        if 'type' in d:
            o.type = d['type']
        return o


