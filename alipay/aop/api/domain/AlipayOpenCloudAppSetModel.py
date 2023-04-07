#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenCloudAppSetModel(object):

    def __init__(self):
        self._cloud_call_status = None
        self._cloud_id = None
        self._env_id = None
        self._invoke_app_id = None

    @property
    def cloud_call_status(self):
        return self._cloud_call_status

    @cloud_call_status.setter
    def cloud_call_status(self, value):
        self._cloud_call_status = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.cloud_call_status:
            if hasattr(self.cloud_call_status, 'to_alipay_dict'):
                params['cloud_call_status'] = self.cloud_call_status.to_alipay_dict()
            else:
                params['cloud_call_status'] = self.cloud_call_status
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenCloudAppSetModel()
        if 'cloud_call_status' in d:
            o.cloud_call_status = d['cloud_call_status']
        if 'cloud_id' in d:
            o.cloud_id = d['cloud_id']
        if 'env_id' in d:
            o.env_id = d['env_id']
        if 'invoke_app_id' in d:
            o.invoke_app_id = d['invoke_app_id']
        return o


