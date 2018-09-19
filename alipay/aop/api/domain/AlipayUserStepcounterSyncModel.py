#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserStepcounterSyncModel(object):

    def __init__(self):
        self._age = None
        self._calorie = None
        self._count = None
        self._data_provider = None
        self._distance = None
        self._height = None
        self._latitude = None
        self._longitude = None
        self._out_user_id = None
        self._time = None
        self._time_zone = None
        self._user_id = None
        self._weight = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def calorie(self):
        return self._calorie

    @calorie.setter
    def calorie(self, value):
        self._calorie = value
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def data_provider(self):
        return self._data_provider

    @data_provider.setter
    def data_provider(self, value):
        self._data_provider = value
    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
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
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value
    @property
    def time_zone(self):
        return self._time_zone

    @time_zone.setter
    def time_zone(self, value):
        self._time_zone = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.calorie:
            if hasattr(self.calorie, 'to_alipay_dict'):
                params['calorie'] = self.calorie.to_alipay_dict()
            else:
                params['calorie'] = self.calorie
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.data_provider:
            if hasattr(self.data_provider, 'to_alipay_dict'):
                params['data_provider'] = self.data_provider.to_alipay_dict()
            else:
                params['data_provider'] = self.data_provider
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
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
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        if self.time_zone:
            if hasattr(self.time_zone, 'to_alipay_dict'):
                params['time_zone'] = self.time_zone.to_alipay_dict()
            else:
                params['time_zone'] = self.time_zone
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.weight:
            if hasattr(self.weight, 'to_alipay_dict'):
                params['weight'] = self.weight.to_alipay_dict()
            else:
                params['weight'] = self.weight
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserStepcounterSyncModel()
        if 'age' in d:
            o.age = d['age']
        if 'calorie' in d:
            o.calorie = d['calorie']
        if 'count' in d:
            o.count = d['count']
        if 'data_provider' in d:
            o.data_provider = d['data_provider']
        if 'distance' in d:
            o.distance = d['distance']
        if 'height' in d:
            o.height = d['height']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'time' in d:
            o.time = d['time']
        if 'time_zone' in d:
            o.time_zone = d['time_zone']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'weight' in d:
            o.weight = d['weight']
        return o


