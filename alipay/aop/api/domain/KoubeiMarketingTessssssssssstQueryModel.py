#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SpiInputObject import SpiInputObject
from alipay.aop.api.domain.AccessParams import AccessParams


class KoubeiMarketingTessssssssssstQueryModel(object):

    def __init__(self):
        self._age = None
        self._height = None
        self._object = None
        self._params = None
        self._x_name = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def object(self):
        return self._object

    @object.setter
    def object(self, value):
        if isinstance(value, SpiInputObject):
            self._object = value
        else:
            self._object = SpiInputObject.from_alipay_dict(value)
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        if isinstance(value, AccessParams):
            self._params = value
        else:
            self._params = AccessParams.from_alipay_dict(value)
    @property
    def x_name(self):
        return self._x_name

    @x_name.setter
    def x_name(self, value):
        self._x_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
        if self.object:
            if hasattr(self.object, 'to_alipay_dict'):
                params['object'] = self.object.to_alipay_dict()
            else:
                params['object'] = self.object
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        if self.x_name:
            if hasattr(self.x_name, 'to_alipay_dict'):
                params['x_name'] = self.x_name.to_alipay_dict()
            else:
                params['x_name'] = self.x_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingTessssssssssstQueryModel()
        if 'age' in d:
            o.age = d['age']
        if 'height' in d:
            o.height = d['height']
        if 'object' in d:
            o.object = d['object']
        if 'params' in d:
            o.params = d['params']
        if 'x_name' in d:
            o.x_name = d['x_name']
        return o


