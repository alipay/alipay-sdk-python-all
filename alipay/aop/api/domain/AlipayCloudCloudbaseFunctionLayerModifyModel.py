#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LayerBinding import LayerBinding


class AlipayCloudCloudbaseFunctionLayerModifyModel(object):

    def __init__(self):
        self._bindings = None
        self._biz_app_id = None
        self._biz_env_id = None
        self._function_name = None

    @property
    def bindings(self):
        return self._bindings

    @bindings.setter
    def bindings(self, value):
        if isinstance(value, list):
            self._bindings = list()
            for i in value:
                if isinstance(i, LayerBinding):
                    self._bindings.append(i)
                else:
                    self._bindings.append(LayerBinding.from_alipay_dict(i))
    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def biz_env_id(self):
        return self._biz_env_id

    @biz_env_id.setter
    def biz_env_id(self, value):
        self._biz_env_id = value
    @property
    def function_name(self):
        return self._function_name

    @function_name.setter
    def function_name(self, value):
        self._function_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.bindings:
            if isinstance(self.bindings, list):
                for i in range(0, len(self.bindings)):
                    element = self.bindings[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bindings[i] = element.to_alipay_dict()
            if hasattr(self.bindings, 'to_alipay_dict'):
                params['bindings'] = self.bindings.to_alipay_dict()
            else:
                params['bindings'] = self.bindings
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.biz_env_id:
            if hasattr(self.biz_env_id, 'to_alipay_dict'):
                params['biz_env_id'] = self.biz_env_id.to_alipay_dict()
            else:
                params['biz_env_id'] = self.biz_env_id
        if self.function_name:
            if hasattr(self.function_name, 'to_alipay_dict'):
                params['function_name'] = self.function_name.to_alipay_dict()
            else:
                params['function_name'] = self.function_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseFunctionLayerModifyModel()
        if 'bindings' in d:
            o.bindings = d['bindings']
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'function_name' in d:
            o.function_name = d['function_name']
        return o


