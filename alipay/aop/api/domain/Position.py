#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Position(object):

    def __init__(self):
        self._city_code = None
        self._device_id = None
        self._device_type = None
        self._scene = None
        self._station_code = None
        self._station_level = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def station_code(self):
        return self._station_code

    @station_code.setter
    def station_code(self, value):
        self._station_code = value
    @property
    def station_level(self):
        return self._station_level

    @station_level.setter
    def station_level(self, value):
        self._station_level = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.station_code:
            if hasattr(self.station_code, 'to_alipay_dict'):
                params['station_code'] = self.station_code.to_alipay_dict()
            else:
                params['station_code'] = self.station_code
        if self.station_level:
            if hasattr(self.station_level, 'to_alipay_dict'):
                params['station_level'] = self.station_level.to_alipay_dict()
            else:
                params['station_level'] = self.station_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Position()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'scene' in d:
            o.scene = d['scene']
        if 'station_code' in d:
            o.station_code = d['station_code']
        if 'station_level' in d:
            o.station_level = d['station_level']
        return o


