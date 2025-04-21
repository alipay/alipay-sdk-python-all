#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseRedisOperationQueryModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._biz_env_id = None
        self._filter_content = None
        self._filter_type = None
        self._instance_name = None
        self._region = None
        self._zone = None

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
    def filter_content(self):
        return self._filter_content

    @filter_content.setter
    def filter_content(self, value):
        self._filter_content = value
    @property
    def filter_type(self):
        return self._filter_type

    @filter_type.setter
    def filter_type(self, value):
        self._filter_type = value
    @property
    def instance_name(self):
        return self._instance_name

    @instance_name.setter
    def instance_name(self, value):
        self._instance_name = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value
    @property
    def zone(self):
        return self._zone

    @zone.setter
    def zone(self, value):
        self._zone = value


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
        if self.filter_content:
            if hasattr(self.filter_content, 'to_alipay_dict'):
                params['filter_content'] = self.filter_content.to_alipay_dict()
            else:
                params['filter_content'] = self.filter_content
        if self.filter_type:
            if hasattr(self.filter_type, 'to_alipay_dict'):
                params['filter_type'] = self.filter_type.to_alipay_dict()
            else:
                params['filter_type'] = self.filter_type
        if self.instance_name:
            if hasattr(self.instance_name, 'to_alipay_dict'):
                params['instance_name'] = self.instance_name.to_alipay_dict()
            else:
                params['instance_name'] = self.instance_name
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        if self.zone:
            if hasattr(self.zone, 'to_alipay_dict'):
                params['zone'] = self.zone.to_alipay_dict()
            else:
                params['zone'] = self.zone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseRedisOperationQueryModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'filter_content' in d:
            o.filter_content = d['filter_content']
        if 'filter_type' in d:
            o.filter_type = d['filter_type']
        if 'instance_name' in d:
            o.instance_name = d['instance_name']
        if 'region' in d:
            o.region = d['region']
        if 'zone' in d:
            o.zone = d['zone']
        return o


