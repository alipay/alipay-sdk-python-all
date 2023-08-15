#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseEnvResourcepackageBuyModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._biz_env_id = None
        self._region = None
        self._resource_spec_code = None

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
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value
    @property
    def resource_spec_code(self):
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, value):
        self._resource_spec_code = value


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
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        if self.resource_spec_code:
            if hasattr(self.resource_spec_code, 'to_alipay_dict'):
                params['resource_spec_code'] = self.resource_spec_code.to_alipay_dict()
            else:
                params['resource_spec_code'] = self.resource_spec_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseEnvResourcepackageBuyModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'region' in d:
            o.region = d['region']
        if 'resource_spec_code' in d:
            o.resource_spec_code = d['resource_spec_code']
        return o


