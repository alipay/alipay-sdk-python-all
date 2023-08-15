#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseFunctionCreateModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._biz_env_id = None
        self._description = None
        self._function_name = None
        self._image_name = None
        self._quota_name = None

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
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def function_name(self):
        return self._function_name

    @function_name.setter
    def function_name(self, value):
        self._function_name = value
    @property
    def image_name(self):
        return self._image_name

    @image_name.setter
    def image_name(self, value):
        self._image_name = value
    @property
    def quota_name(self):
        return self._quota_name

    @quota_name.setter
    def quota_name(self, value):
        self._quota_name = value


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
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.function_name:
            if hasattr(self.function_name, 'to_alipay_dict'):
                params['function_name'] = self.function_name.to_alipay_dict()
            else:
                params['function_name'] = self.function_name
        if self.image_name:
            if hasattr(self.image_name, 'to_alipay_dict'):
                params['image_name'] = self.image_name.to_alipay_dict()
            else:
                params['image_name'] = self.image_name
        if self.quota_name:
            if hasattr(self.quota_name, 'to_alipay_dict'):
                params['quota_name'] = self.quota_name.to_alipay_dict()
            else:
                params['quota_name'] = self.quota_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseFunctionCreateModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'description' in d:
            o.description = d['description']
        if 'function_name' in d:
            o.function_name = d['function_name']
        if 'image_name' in d:
            o.image_name = d['image_name']
        if 'quota_name' in d:
            o.quota_name = d['quota_name']
        return o


