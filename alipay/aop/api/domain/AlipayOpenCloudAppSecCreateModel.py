#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenCloudAppSecCreateModel(object):

    def __init__(self):
        self._cloud_id = None
        self._env_id = None
        self._invoke_app_id = None
        self._req_sign_type = None
        self._sec_content = None
        self._sec_type = None

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
    def req_sign_type(self):
        return self._req_sign_type

    @req_sign_type.setter
    def req_sign_type(self, value):
        self._req_sign_type = value
    @property
    def sec_content(self):
        return self._sec_content

    @sec_content.setter
    def sec_content(self, value):
        self._sec_content = value
    @property
    def sec_type(self):
        return self._sec_type

    @sec_type.setter
    def sec_type(self, value):
        self._sec_type = value


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
        if self.req_sign_type:
            if hasattr(self.req_sign_type, 'to_alipay_dict'):
                params['req_sign_type'] = self.req_sign_type.to_alipay_dict()
            else:
                params['req_sign_type'] = self.req_sign_type
        if self.sec_content:
            if hasattr(self.sec_content, 'to_alipay_dict'):
                params['sec_content'] = self.sec_content.to_alipay_dict()
            else:
                params['sec_content'] = self.sec_content
        if self.sec_type:
            if hasattr(self.sec_type, 'to_alipay_dict'):
                params['sec_type'] = self.sec_type.to_alipay_dict()
            else:
                params['sec_type'] = self.sec_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenCloudAppSecCreateModel()
        if 'cloud_id' in d:
            o.cloud_id = d['cloud_id']
        if 'env_id' in d:
            o.env_id = d['env_id']
        if 'invoke_app_id' in d:
            o.invoke_app_id = d['invoke_app_id']
        if 'req_sign_type' in d:
            o.req_sign_type = d['req_sign_type']
        if 'sec_content' in d:
            o.sec_content = d['sec_content']
        if 'sec_type' in d:
            o.sec_type = d['sec_type']
        return o


