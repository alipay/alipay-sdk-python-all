#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EnvVar import EnvVar


class AlipayCloudCloudbaseFunctionEnvvarsSetModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._biz_env_id = None
        self._env_vars = None
        self._function_name = None

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
    def env_vars(self):
        return self._env_vars

    @env_vars.setter
    def env_vars(self, value):
        if isinstance(value, list):
            self._env_vars = list()
            for i in value:
                if isinstance(i, EnvVar):
                    self._env_vars.append(i)
                else:
                    self._env_vars.append(EnvVar.from_alipay_dict(i))
    @property
    def function_name(self):
        return self._function_name

    @function_name.setter
    def function_name(self, value):
        self._function_name = value


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
        if self.env_vars:
            if isinstance(self.env_vars, list):
                for i in range(0, len(self.env_vars)):
                    element = self.env_vars[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.env_vars[i] = element.to_alipay_dict()
            if hasattr(self.env_vars, 'to_alipay_dict'):
                params['env_vars'] = self.env_vars.to_alipay_dict()
            else:
                params['env_vars'] = self.env_vars
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
        o = AlipayCloudCloudbaseFunctionEnvvarsSetModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'env_vars' in d:
            o.env_vars = d['env_vars']
        if 'function_name' in d:
            o.function_name = d['function_name']
        return o


