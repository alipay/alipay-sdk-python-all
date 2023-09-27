#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AosDataItem import AosDataItem


class AlipayOpenMiniCloudAosbizdataSyncModel(object):

    def __init__(self):
        self._app_token = None
        self._data = None
        self._id_type = None
        self._ops = None
        self._ops_timestamp = None
        self._type = None

    @property
    def app_token(self):
        return self._app_token

    @app_token.setter
    def app_token(self, value):
        self._app_token = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, AosDataItem):
                    self._data.append(i)
                else:
                    self._data.append(AosDataItem.from_alipay_dict(i))
    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        self._id_type = value
    @property
    def ops(self):
        return self._ops

    @ops.setter
    def ops(self, value):
        self._ops = value
    @property
    def ops_timestamp(self):
        return self._ops_timestamp

    @ops_timestamp.setter
    def ops_timestamp(self, value):
        self._ops_timestamp = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_token:
            if hasattr(self.app_token, 'to_alipay_dict'):
                params['app_token'] = self.app_token.to_alipay_dict()
            else:
                params['app_token'] = self.app_token
        if self.data:
            if isinstance(self.data, list):
                for i in range(0, len(self.data)):
                    element = self.data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data[i] = element.to_alipay_dict()
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.id_type:
            if hasattr(self.id_type, 'to_alipay_dict'):
                params['id_type'] = self.id_type.to_alipay_dict()
            else:
                params['id_type'] = self.id_type
        if self.ops:
            if hasattr(self.ops, 'to_alipay_dict'):
                params['ops'] = self.ops.to_alipay_dict()
            else:
                params['ops'] = self.ops
        if self.ops_timestamp:
            if hasattr(self.ops_timestamp, 'to_alipay_dict'):
                params['ops_timestamp'] = self.ops_timestamp.to_alipay_dict()
            else:
                params['ops_timestamp'] = self.ops_timestamp
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
        o = AlipayOpenMiniCloudAosbizdataSyncModel()
        if 'app_token' in d:
            o.app_token = d['app_token']
        if 'data' in d:
            o.data = d['data']
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'ops' in d:
            o.ops = d['ops']
        if 'ops_timestamp' in d:
            o.ops_timestamp = d['ops_timestamp']
        if 'type' in d:
            o.type = d['type']
        return o


