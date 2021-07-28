#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataAiserviceCloudbusResourceUploadModel(object):

    def __init__(self):
        self._data = None
        self._res_name = None
        self._type = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def res_name(self):
        return self._res_name

    @res_name.setter
    def res_name(self, value):
        self._res_name = value
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
        if self.res_name:
            if hasattr(self.res_name, 'to_alipay_dict'):
                params['res_name'] = self.res_name.to_alipay_dict()
            else:
                params['res_name'] = self.res_name
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
        o = AlipayDataAiserviceCloudbusResourceUploadModel()
        if 'data' in d:
            o.data = d['data']
        if 'res_name' in d:
            o.res_name = d['res_name']
        if 'type' in d:
            o.type = d['type']
        return o


