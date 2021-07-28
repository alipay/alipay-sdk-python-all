#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialAntsportsCurrentpathQueryModel(object):

    def __init__(self):
        self._day = None
        self._path_scene = None
        self._path_station_code = None
        self._path_station_name = None
        self._time_zone = None
        self._user_id = None

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self._day = value
    @property
    def path_scene(self):
        return self._path_scene

    @path_scene.setter
    def path_scene(self, value):
        self._path_scene = value
    @property
    def path_station_code(self):
        return self._path_station_code

    @path_station_code.setter
    def path_station_code(self, value):
        self._path_station_code = value
    @property
    def path_station_name(self):
        return self._path_station_name

    @path_station_name.setter
    def path_station_name(self, value):
        self._path_station_name = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.day:
            if hasattr(self.day, 'to_alipay_dict'):
                params['day'] = self.day.to_alipay_dict()
            else:
                params['day'] = self.day
        if self.path_scene:
            if hasattr(self.path_scene, 'to_alipay_dict'):
                params['path_scene'] = self.path_scene.to_alipay_dict()
            else:
                params['path_scene'] = self.path_scene
        if self.path_station_code:
            if hasattr(self.path_station_code, 'to_alipay_dict'):
                params['path_station_code'] = self.path_station_code.to_alipay_dict()
            else:
                params['path_station_code'] = self.path_station_code
        if self.path_station_name:
            if hasattr(self.path_station_name, 'to_alipay_dict'):
                params['path_station_name'] = self.path_station_name.to_alipay_dict()
            else:
                params['path_station_name'] = self.path_station_name
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialAntsportsCurrentpathQueryModel()
        if 'day' in d:
            o.day = d['day']
        if 'path_scene' in d:
            o.path_scene = d['path_scene']
        if 'path_station_code' in d:
            o.path_station_code = d['path_station_code']
        if 'path_station_name' in d:
            o.path_station_name = d['path_station_name']
        if 'time_zone' in d:
            o.time_zone = d['time_zone']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


