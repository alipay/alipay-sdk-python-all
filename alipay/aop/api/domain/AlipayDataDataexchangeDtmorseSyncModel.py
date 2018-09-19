#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataexchangeDtmorseSyncModel(object):

    def __init__(self):
        self._data = None
        self._extent_info = None
        self._mid = None
        self._operate_type = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def extent_info(self):
        return self._extent_info

    @extent_info.setter
    def extent_info(self, value):
        self._extent_info = value
    @property
    def mid(self):
        return self._mid

    @mid.setter
    def mid(self, value):
        self._mid = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.extent_info:
            if hasattr(self.extent_info, 'to_alipay_dict'):
                params['extent_info'] = self.extent_info.to_alipay_dict()
            else:
                params['extent_info'] = self.extent_info
        if self.mid:
            if hasattr(self.mid, 'to_alipay_dict'):
                params['mid'] = self.mid.to_alipay_dict()
            else:
                params['mid'] = self.mid
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataexchangeDtmorseSyncModel()
        if 'data' in d:
            o.data = d['data']
        if 'extent_info' in d:
            o.extent_info = d['extent_info']
        if 'mid' in d:
            o.mid = d['mid']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        return o


