#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseFunctionLayerBindModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._biz_env_id = None
        self._function_name = None
        self._layer_name = None
        self._layer_version_name = None

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
    @property
    def layer_name(self):
        return self._layer_name

    @layer_name.setter
    def layer_name(self, value):
        self._layer_name = value
    @property
    def layer_version_name(self):
        return self._layer_version_name

    @layer_version_name.setter
    def layer_version_name(self, value):
        self._layer_version_name = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.layer_name:
            if hasattr(self.layer_name, 'to_alipay_dict'):
                params['layer_name'] = self.layer_name.to_alipay_dict()
            else:
                params['layer_name'] = self.layer_name
        if self.layer_version_name:
            if hasattr(self.layer_version_name, 'to_alipay_dict'):
                params['layer_version_name'] = self.layer_version_name.to_alipay_dict()
            else:
                params['layer_version_name'] = self.layer_version_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseFunctionLayerBindModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'function_name' in d:
            o.function_name = d['function_name']
        if 'layer_name' in d:
            o.layer_name = d['layer_name']
        if 'layer_version_name' in d:
            o.layer_version_name = d['layer_version_name']
        return o


