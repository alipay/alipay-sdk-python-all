#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseExtensionRedisApplyModel(object):

    def __init__(self):
        self._architecture_type = None
        self._biz_app_id = None
        self._biz_env_id = None
        self._instance_name = None
        self._instance_spec = None
        self._node_type = None
        self._password = None
        self._redis_version = None
        self._region = None
        self._shard_number = None

    @property
    def architecture_type(self):
        return self._architecture_type

    @architecture_type.setter
    def architecture_type(self, value):
        self._architecture_type = value
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
    def instance_name(self):
        return self._instance_name

    @instance_name.setter
    def instance_name(self, value):
        self._instance_name = value
    @property
    def instance_spec(self):
        return self._instance_spec

    @instance_spec.setter
    def instance_spec(self, value):
        self._instance_spec = value
    @property
    def node_type(self):
        return self._node_type

    @node_type.setter
    def node_type(self, value):
        self._node_type = value
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
    @property
    def redis_version(self):
        return self._redis_version

    @redis_version.setter
    def redis_version(self, value):
        self._redis_version = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value
    @property
    def shard_number(self):
        return self._shard_number

    @shard_number.setter
    def shard_number(self, value):
        self._shard_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.architecture_type:
            if hasattr(self.architecture_type, 'to_alipay_dict'):
                params['architecture_type'] = self.architecture_type.to_alipay_dict()
            else:
                params['architecture_type'] = self.architecture_type
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
        if self.instance_name:
            if hasattr(self.instance_name, 'to_alipay_dict'):
                params['instance_name'] = self.instance_name.to_alipay_dict()
            else:
                params['instance_name'] = self.instance_name
        if self.instance_spec:
            if hasattr(self.instance_spec, 'to_alipay_dict'):
                params['instance_spec'] = self.instance_spec.to_alipay_dict()
            else:
                params['instance_spec'] = self.instance_spec
        if self.node_type:
            if hasattr(self.node_type, 'to_alipay_dict'):
                params['node_type'] = self.node_type.to_alipay_dict()
            else:
                params['node_type'] = self.node_type
        if self.password:
            if hasattr(self.password, 'to_alipay_dict'):
                params['password'] = self.password.to_alipay_dict()
            else:
                params['password'] = self.password
        if self.redis_version:
            if hasattr(self.redis_version, 'to_alipay_dict'):
                params['redis_version'] = self.redis_version.to_alipay_dict()
            else:
                params['redis_version'] = self.redis_version
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        if self.shard_number:
            if hasattr(self.shard_number, 'to_alipay_dict'):
                params['shard_number'] = self.shard_number.to_alipay_dict()
            else:
                params['shard_number'] = self.shard_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseExtensionRedisApplyModel()
        if 'architecture_type' in d:
            o.architecture_type = d['architecture_type']
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'instance_name' in d:
            o.instance_name = d['instance_name']
        if 'instance_spec' in d:
            o.instance_spec = d['instance_spec']
        if 'node_type' in d:
            o.node_type = d['node_type']
        if 'password' in d:
            o.password = d['password']
        if 'redis_version' in d:
            o.redis_version = d['redis_version']
        if 'region' in d:
            o.region = d['region']
        if 'shard_number' in d:
            o.shard_number = d['shard_number']
        return o


