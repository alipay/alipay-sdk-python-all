#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudrunStaticsiteCorsModifyModel(object):

    def __init__(self):
        self._access_control_allow_origins = None
        self._access_control_max_age = None
        self._assume_token = None
        self._enable = None
        self._env = None

    @property
    def access_control_allow_origins(self):
        return self._access_control_allow_origins

    @access_control_allow_origins.setter
    def access_control_allow_origins(self, value):
        if isinstance(value, list):
            self._access_control_allow_origins = list()
            for i in value:
                self._access_control_allow_origins.append(i)
    @property
    def access_control_max_age(self):
        return self._access_control_max_age

    @access_control_max_age.setter
    def access_control_max_age(self, value):
        self._access_control_max_age = value
    @property
    def assume_token(self):
        return self._assume_token

    @assume_token.setter
    def assume_token(self, value):
        self._assume_token = value
    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value
    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_control_allow_origins:
            if isinstance(self.access_control_allow_origins, list):
                for i in range(0, len(self.access_control_allow_origins)):
                    element = self.access_control_allow_origins[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.access_control_allow_origins[i] = element.to_alipay_dict()
            if hasattr(self.access_control_allow_origins, 'to_alipay_dict'):
                params['access_control_allow_origins'] = self.access_control_allow_origins.to_alipay_dict()
            else:
                params['access_control_allow_origins'] = self.access_control_allow_origins
        if self.access_control_max_age:
            if hasattr(self.access_control_max_age, 'to_alipay_dict'):
                params['access_control_max_age'] = self.access_control_max_age.to_alipay_dict()
            else:
                params['access_control_max_age'] = self.access_control_max_age
        if self.assume_token:
            if hasattr(self.assume_token, 'to_alipay_dict'):
                params['assume_token'] = self.assume_token.to_alipay_dict()
            else:
                params['assume_token'] = self.assume_token
        if self.enable:
            if hasattr(self.enable, 'to_alipay_dict'):
                params['enable'] = self.enable.to_alipay_dict()
            else:
                params['enable'] = self.enable
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
        o = AlipayCloudCloudrunStaticsiteCorsModifyModel()
        if 'access_control_allow_origins' in d:
            o.access_control_allow_origins = d['access_control_allow_origins']
        if 'access_control_max_age' in d:
            o.access_control_max_age = d['access_control_max_age']
        if 'assume_token' in d:
            o.assume_token = d['assume_token']
        if 'enable' in d:
            o.enable = d['enable']
        if 'env' in d:
            o.env = d['env']
        return o


