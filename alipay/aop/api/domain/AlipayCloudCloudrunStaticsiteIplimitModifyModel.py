#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudrunStaticsiteIplimitModifyModel(object):

    def __init__(self):
        self._assume_token = None
        self._enable = None
        self._env = None
        self._ip_list = None
        self._limit_type = None

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
    @property
    def ip_list(self):
        return self._ip_list

    @ip_list.setter
    def ip_list(self, value):
        if isinstance(value, list):
            self._ip_list = list()
            for i in value:
                self._ip_list.append(i)
    @property
    def limit_type(self):
        return self._limit_type

    @limit_type.setter
    def limit_type(self, value):
        self._limit_type = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.ip_list:
            if isinstance(self.ip_list, list):
                for i in range(0, len(self.ip_list)):
                    element = self.ip_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ip_list[i] = element.to_alipay_dict()
            if hasattr(self.ip_list, 'to_alipay_dict'):
                params['ip_list'] = self.ip_list.to_alipay_dict()
            else:
                params['ip_list'] = self.ip_list
        if self.limit_type:
            if hasattr(self.limit_type, 'to_alipay_dict'):
                params['limit_type'] = self.limit_type.to_alipay_dict()
            else:
                params['limit_type'] = self.limit_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudrunStaticsiteIplimitModifyModel()
        if 'assume_token' in d:
            o.assume_token = d['assume_token']
        if 'enable' in d:
            o.enable = d['enable']
        if 'env' in d:
            o.env = d['env']
        if 'ip_list' in d:
            o.ip_list = d['ip_list']
        if 'limit_type' in d:
            o.limit_type = d['limit_type']
        return o


