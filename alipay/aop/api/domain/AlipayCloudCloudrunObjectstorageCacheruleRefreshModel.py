#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudrunObjectstorageCacheruleRefreshModel(object):

    def __init__(self):
        self._data = None
        self._env = None
        self._id_app = None
        self._type = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value
    @property
    def id_app(self):
        return self._id_app

    @id_app.setter
    def id_app(self, value):
        self._id_app = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
        if self.id_app:
            if hasattr(self.id_app, 'to_alipay_dict'):
                params['id_app'] = self.id_app.to_alipay_dict()
            else:
                params['id_app'] = self.id_app
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
        o = AlipayCloudCloudrunObjectstorageCacheruleRefreshModel()
        if 'data' in d:
            o.data = d['data']
        if 'env' in d:
            o.env = d['env']
        if 'id_app' in d:
            o.id_app = d['id_app']
        if 'type' in d:
            o.type = d['type']
        return o


