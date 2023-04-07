#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenCloudAppPermissionSyncModel(object):

    def __init__(self):
        self._cloud_id = None
        self._env_id = None
        self._invoke_app_id = None
        self._permission_api_list = None

    @property
    def cloud_id(self):
        return self._cloud_id

    @cloud_id.setter
    def cloud_id(self, value):
        self._cloud_id = value
    @property
    def env_id(self):
        return self._env_id

    @env_id.setter
    def env_id(self, value):
        self._env_id = value
    @property
    def invoke_app_id(self):
        return self._invoke_app_id

    @invoke_app_id.setter
    def invoke_app_id(self, value):
        self._invoke_app_id = value
    @property
    def permission_api_list(self):
        return self._permission_api_list

    @permission_api_list.setter
    def permission_api_list(self, value):
        if isinstance(value, list):
            self._permission_api_list = list()
            for i in value:
                self._permission_api_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.cloud_id:
            if hasattr(self.cloud_id, 'to_alipay_dict'):
                params['cloud_id'] = self.cloud_id.to_alipay_dict()
            else:
                params['cloud_id'] = self.cloud_id
        if self.env_id:
            if hasattr(self.env_id, 'to_alipay_dict'):
                params['env_id'] = self.env_id.to_alipay_dict()
            else:
                params['env_id'] = self.env_id
        if self.invoke_app_id:
            if hasattr(self.invoke_app_id, 'to_alipay_dict'):
                params['invoke_app_id'] = self.invoke_app_id.to_alipay_dict()
            else:
                params['invoke_app_id'] = self.invoke_app_id
        if self.permission_api_list:
            if isinstance(self.permission_api_list, list):
                for i in range(0, len(self.permission_api_list)):
                    element = self.permission_api_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.permission_api_list[i] = element.to_alipay_dict()
            if hasattr(self.permission_api_list, 'to_alipay_dict'):
                params['permission_api_list'] = self.permission_api_list.to_alipay_dict()
            else:
                params['permission_api_list'] = self.permission_api_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenCloudAppPermissionSyncModel()
        if 'cloud_id' in d:
            o.cloud_id = d['cloud_id']
        if 'env_id' in d:
            o.env_id = d['env_id']
        if 'invoke_app_id' in d:
            o.invoke_app_id = d['invoke_app_id']
        if 'permission_api_list' in d:
            o.permission_api_list = d['permission_api_list']
        return o


