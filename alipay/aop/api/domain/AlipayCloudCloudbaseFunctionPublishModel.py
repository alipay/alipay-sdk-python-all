#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseFunctionPublishModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._biz_env_id = None
        self._function_name = None
        self._need_dependency = None
        self._upload_id = None

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
    def need_dependency(self):
        return self._need_dependency

    @need_dependency.setter
    def need_dependency(self, value):
        self._need_dependency = value
    @property
    def upload_id(self):
        return self._upload_id

    @upload_id.setter
    def upload_id(self, value):
        self._upload_id = value


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
        if self.need_dependency:
            if hasattr(self.need_dependency, 'to_alipay_dict'):
                params['need_dependency'] = self.need_dependency.to_alipay_dict()
            else:
                params['need_dependency'] = self.need_dependency
        if self.upload_id:
            if hasattr(self.upload_id, 'to_alipay_dict'):
                params['upload_id'] = self.upload_id.to_alipay_dict()
            else:
                params['upload_id'] = self.upload_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseFunctionPublishModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'function_name' in d:
            o.function_name = d['function_name']
        if 'need_dependency' in d:
            o.need_dependency = d['need_dependency']
        if 'upload_id' in d:
            o.upload_id = d['upload_id']
        return o


