#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudrunObjectstorageCacheruleAddModel(object):

    def __init__(self):
        self._assume_token = None
        self._cache_key = None
        self._cache_priority = None
        self._cache_timeout = None
        self._cache_type = None
        self._env = None

    @property
    def assume_token(self):
        return self._assume_token

    @assume_token.setter
    def assume_token(self, value):
        self._assume_token = value
    @property
    def cache_key(self):
        return self._cache_key

    @cache_key.setter
    def cache_key(self, value):
        self._cache_key = value
    @property
    def cache_priority(self):
        return self._cache_priority

    @cache_priority.setter
    def cache_priority(self, value):
        self._cache_priority = value
    @property
    def cache_timeout(self):
        return self._cache_timeout

    @cache_timeout.setter
    def cache_timeout(self, value):
        self._cache_timeout = value
    @property
    def cache_type(self):
        return self._cache_type

    @cache_type.setter
    def cache_type(self, value):
        self._cache_type = value
    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value


    def to_alipay_dict(self):
        params = dict()
        if self.assume_token:
            if hasattr(self.assume_token, 'to_alipay_dict'):
                params['assume_token'] = self.assume_token.to_alipay_dict()
            else:
                params['assume_token'] = self.assume_token
        if self.cache_key:
            if hasattr(self.cache_key, 'to_alipay_dict'):
                params['cache_key'] = self.cache_key.to_alipay_dict()
            else:
                params['cache_key'] = self.cache_key
        if self.cache_priority:
            if hasattr(self.cache_priority, 'to_alipay_dict'):
                params['cache_priority'] = self.cache_priority.to_alipay_dict()
            else:
                params['cache_priority'] = self.cache_priority
        if self.cache_timeout:
            if hasattr(self.cache_timeout, 'to_alipay_dict'):
                params['cache_timeout'] = self.cache_timeout.to_alipay_dict()
            else:
                params['cache_timeout'] = self.cache_timeout
        if self.cache_type:
            if hasattr(self.cache_type, 'to_alipay_dict'):
                params['cache_type'] = self.cache_type.to_alipay_dict()
            else:
                params['cache_type'] = self.cache_type
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudrunObjectstorageCacheruleAddModel()
        if 'assume_token' in d:
            o.assume_token = d['assume_token']
        if 'cache_key' in d:
            o.cache_key = d['cache_key']
        if 'cache_priority' in d:
            o.cache_priority = d['cache_priority']
        if 'cache_timeout' in d:
            o.cache_timeout = d['cache_timeout']
        if 'cache_type' in d:
            o.cache_type = d['cache_type']
        if 'env' in d:
            o.env = d['env']
        return o


