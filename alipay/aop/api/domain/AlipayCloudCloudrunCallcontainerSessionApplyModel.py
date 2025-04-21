#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudrunCallcontainerSessionApplyModel(object):

    def __init__(self):
        self._custom_id = None
        self._env_id = None
        self._parent_app_id = None
        self._sp_app_id = None

    @property
    def custom_id(self):
        return self._custom_id

    @custom_id.setter
    def custom_id(self, value):
        self._custom_id = value
    @property
    def env_id(self):
        return self._env_id

    @env_id.setter
    def env_id(self, value):
        self._env_id = value
    @property
    def parent_app_id(self):
        return self._parent_app_id

    @parent_app_id.setter
    def parent_app_id(self, value):
        self._parent_app_id = value
    @property
    def sp_app_id(self):
        return self._sp_app_id

    @sp_app_id.setter
    def sp_app_id(self, value):
        self._sp_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.custom_id:
            if hasattr(self.custom_id, 'to_alipay_dict'):
                params['custom_id'] = self.custom_id.to_alipay_dict()
            else:
                params['custom_id'] = self.custom_id
        if self.env_id:
            if hasattr(self.env_id, 'to_alipay_dict'):
                params['env_id'] = self.env_id.to_alipay_dict()
            else:
                params['env_id'] = self.env_id
        if self.parent_app_id:
            if hasattr(self.parent_app_id, 'to_alipay_dict'):
                params['parent_app_id'] = self.parent_app_id.to_alipay_dict()
            else:
                params['parent_app_id'] = self.parent_app_id
        if self.sp_app_id:
            if hasattr(self.sp_app_id, 'to_alipay_dict'):
                params['sp_app_id'] = self.sp_app_id.to_alipay_dict()
            else:
                params['sp_app_id'] = self.sp_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudrunCallcontainerSessionApplyModel()
        if 'custom_id' in d:
            o.custom_id = d['custom_id']
        if 'env_id' in d:
            o.env_id = d['env_id']
        if 'parent_app_id' in d:
            o.parent_app_id = d['parent_app_id']
        if 'sp_app_id' in d:
            o.sp_app_id = d['sp_app_id']
        return o


