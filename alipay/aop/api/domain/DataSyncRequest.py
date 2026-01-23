#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DataSyncRequest(object):

    def __init__(self):
        self._biz_key = None
        self._data_content = None
        self._data_type = None
        self._dt = None

    @property
    def biz_key(self):
        return self._biz_key

    @biz_key.setter
    def biz_key(self, value):
        self._biz_key = value
    @property
    def data_content(self):
        return self._data_content

    @data_content.setter
    def data_content(self, value):
        self._data_content = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def dt(self):
        return self._dt

    @dt.setter
    def dt(self, value):
        self._dt = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_key:
            if hasattr(self.biz_key, 'to_alipay_dict'):
                params['biz_key'] = self.biz_key.to_alipay_dict()
            else:
                params['biz_key'] = self.biz_key
        if self.data_content:
            if hasattr(self.data_content, 'to_alipay_dict'):
                params['data_content'] = self.data_content.to_alipay_dict()
            else:
                params['data_content'] = self.data_content
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.dt:
            if hasattr(self.dt, 'to_alipay_dict'):
                params['dt'] = self.dt.to_alipay_dict()
            else:
                params['dt'] = self.dt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DataSyncRequest()
        if 'biz_key' in d:
            o.biz_key = d['biz_key']
        if 'data_content' in d:
            o.data_content = d['data_content']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'dt' in d:
            o.dt = d['dt']
        return o


