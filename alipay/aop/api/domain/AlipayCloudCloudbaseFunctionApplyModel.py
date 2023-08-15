#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseFunctionApplyModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._biz_env_id = None
        self._function_name = None
        self._params = None
        self._snapshot_name = None

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
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value
    @property
    def snapshot_name(self):
        return self._snapshot_name

    @snapshot_name.setter
    def snapshot_name(self, value):
        self._snapshot_name = value


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
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        if self.snapshot_name:
            if hasattr(self.snapshot_name, 'to_alipay_dict'):
                params['snapshot_name'] = self.snapshot_name.to_alipay_dict()
            else:
                params['snapshot_name'] = self.snapshot_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseFunctionApplyModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'function_name' in d:
            o.function_name = d['function_name']
        if 'params' in d:
            o.params = d['params']
        if 'snapshot_name' in d:
            o.snapshot_name = d['snapshot_name']
        return o


