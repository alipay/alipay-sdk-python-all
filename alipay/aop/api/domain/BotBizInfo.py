#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BotBizInfo(object):

    def __init__(self):
        self._actual_city_code = None
        self._actual_city_name = None
        self._city_code = None
        self._city_name = None
        self._scene = None

    @property
    def actual_city_code(self):
        return self._actual_city_code

    @actual_city_code.setter
    def actual_city_code(self, value):
        self._actual_city_code = value
    @property
    def actual_city_name(self):
        return self._actual_city_name

    @actual_city_name.setter
    def actual_city_name(self, value):
        self._actual_city_name = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_city_code:
            if hasattr(self.actual_city_code, 'to_alipay_dict'):
                params['actual_city_code'] = self.actual_city_code.to_alipay_dict()
            else:
                params['actual_city_code'] = self.actual_city_code
        if self.actual_city_name:
            if hasattr(self.actual_city_name, 'to_alipay_dict'):
                params['actual_city_name'] = self.actual_city_name.to_alipay_dict()
            else:
                params['actual_city_name'] = self.actual_city_name
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BotBizInfo()
        if 'actual_city_code' in d:
            o.actual_city_code = d['actual_city_code']
        if 'actual_city_name' in d:
            o.actual_city_name = d['actual_city_name']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'scene' in d:
            o.scene = d['scene']
        return o


