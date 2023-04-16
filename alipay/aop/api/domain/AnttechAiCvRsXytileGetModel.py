#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechAiCvRsXytileGetModel(object):

    def __init__(self):
        self._biz_name = None
        self._crow_type = None
        self._date = None
        self._index = None
        self._object_type = None
        self._query_params = None
        self._x = None
        self._y = None
        self._z = None

    @property
    def biz_name(self):
        return self._biz_name

    @biz_name.setter
    def biz_name(self, value):
        self._biz_name = value
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
    def object_type(self):
        return self._object_type

    @object_type.setter
    def object_type(self, value):
        self._object_type = value
    @property
    def query_params(self):
        return self._query_params

    @query_params.setter
    def query_params(self, value):
        self._query_params = value
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
        if self.biz_name:
            if hasattr(self.biz_name, 'to_alipay_dict'):
                params['biz_name'] = self.biz_name.to_alipay_dict()
            else:
                params['biz_name'] = self.biz_name
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
        if self.object_type:
            if hasattr(self.object_type, 'to_alipay_dict'):
                params['object_type'] = self.object_type.to_alipay_dict()
            else:
                params['object_type'] = self.object_type
        if self.query_params:
            if hasattr(self.query_params, 'to_alipay_dict'):
                params['query_params'] = self.query_params.to_alipay_dict()
            else:
                params['query_params'] = self.query_params
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
        if 'biz_name' in d:
            o.biz_name = d['biz_name']
        if 'crow_type' in d:
            o.crow_type = d['crow_type']
        if 'date' in d:
            o.date = d['date']
        if 'index' in d:
            o.index = d['index']
        if 'object_type' in d:
            o.object_type = d['object_type']
        if 'query_params' in d:
            o.query_params = d['query_params']
        if 'x' in d:
            o.x = d['x']
        if 'y' in d:
            o.y = d['y']
        if 'z' in d:
            o.z = d['z']
        return o


