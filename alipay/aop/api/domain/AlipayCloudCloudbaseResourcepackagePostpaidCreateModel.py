#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseResourcepackagePostpaidCreateModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._env_description = None
        self._env_name = None
        self._region = None

    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def env_description(self):
        return self._env_description

    @env_description.setter
    def env_description(self, value):
        self._env_description = value
    @property
    def env_name(self):
        return self._env_name

    @env_name.setter
    def env_name(self, value):
        self._env_name = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.env_description:
            if hasattr(self.env_description, 'to_alipay_dict'):
                params['env_description'] = self.env_description.to_alipay_dict()
            else:
                params['env_description'] = self.env_description
        if self.env_name:
            if hasattr(self.env_name, 'to_alipay_dict'):
                params['env_name'] = self.env_name.to_alipay_dict()
            else:
                params['env_name'] = self.env_name
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseResourcepackagePostpaidCreateModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'env_description' in d:
            o.env_description = d['env_description']
        if 'env_name' in d:
            o.env_name = d['env_name']
        if 'region' in d:
            o.region = d['region']
        return o


