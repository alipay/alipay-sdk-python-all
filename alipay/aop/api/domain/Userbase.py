#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Userbase(object):

    def __init__(self):
        self._birthday = None
        self._gender = None
        self._height = None
        self._insurance_type = None
        self._live_area_name = None
        self._name = None
        self._weight = None

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def insurance_type(self):
        return self._insurance_type

    @insurance_type.setter
    def insurance_type(self, value):
        self._insurance_type = value
    @property
    def live_area_name(self):
        return self._live_area_name

    @live_area_name.setter
    def live_area_name(self, value):
        self._live_area_name = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value


    def to_alipay_dict(self):
        params = dict()
        if self.birthday:
            if hasattr(self.birthday, 'to_alipay_dict'):
                params['birthday'] = self.birthday.to_alipay_dict()
            else:
                params['birthday'] = self.birthday
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
        if self.insurance_type:
            if hasattr(self.insurance_type, 'to_alipay_dict'):
                params['insurance_type'] = self.insurance_type.to_alipay_dict()
            else:
                params['insurance_type'] = self.insurance_type
        if self.live_area_name:
            if hasattr(self.live_area_name, 'to_alipay_dict'):
                params['live_area_name'] = self.live_area_name.to_alipay_dict()
            else:
                params['live_area_name'] = self.live_area_name
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
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
        o = Userbase()
        if 'birthday' in d:
            o.birthday = d['birthday']
        if 'gender' in d:
            o.gender = d['gender']
        if 'height' in d:
            o.height = d['height']
        if 'insurance_type' in d:
            o.insurance_type = d['insurance_type']
        if 'live_area_name' in d:
            o.live_area_name = d['live_area_name']
        if 'name' in d:
            o.name = d['name']
        if 'weight' in d:
            o.weight = d['weight']
        return o


