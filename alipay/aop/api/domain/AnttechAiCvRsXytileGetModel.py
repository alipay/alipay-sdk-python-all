#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechAiCvRsXytileGetModel(object):

    def __init__(self):
        self._crow_type = None
        self._date = None
        self._index = None
        self._x = None
        self._y = None
        self._z = None

    @property
    def crow_type(self):
        return self._crow_type

    @crow_type.setter
    def crow_type(self, value):
        self._crow_type = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value


    def to_alipay_dict(self):
        params = dict()
        if self.crow_type:
            if hasattr(self.crow_type, 'to_alipay_dict'):
                params['crow_type'] = self.crow_type.to_alipay_dict()
            else:
                params['crow_type'] = self.crow_type
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.index:
            if hasattr(self.index, 'to_alipay_dict'):
                params['index'] = self.index.to_alipay_dict()
            else:
                params['index'] = self.index
        if self.x:
            if hasattr(self.x, 'to_alipay_dict'):
                params['x'] = self.x.to_alipay_dict()
            else:
                params['x'] = self.x
        if self.y:
            if hasattr(self.y, 'to_alipay_dict'):
                params['y'] = self.y.to_alipay_dict()
            else:
                params['y'] = self.y
        if self.z:
            if hasattr(self.z, 'to_alipay_dict'):
                params['z'] = self.z.to_alipay_dict()
            else:
                params['z'] = self.z
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechAiCvRsXytileGetModel()
        if 'crow_type' in d:
            o.crow_type = d['crow_type']
        if 'date' in d:
            o.date = d['date']
        if 'index' in d:
            o.index = d['index']
        if 'x' in d:
            o.x = d['x']
        if 'y' in d:
            o.y = d['y']
        if 'z' in d:
            o.z = d['z']
        return o


