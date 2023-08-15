#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudrunStaticsiteRefererModifyModel(object):

    def __init__(self):
        self._assume_token = None
        self._enable = None
        self._env = None
        self._limit_type = None
        self._no_refer_access = None
        self._refer_list = None

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
    def limit_type(self):
        return self._limit_type

    @limit_type.setter
    def limit_type(self, value):
        self._limit_type = value
    @property
    def no_refer_access(self):
        return self._no_refer_access

    @no_refer_access.setter
    def no_refer_access(self, value):
        self._no_refer_access = value
    @property
    def refer_list(self):
        return self._refer_list

    @refer_list.setter
    def refer_list(self, value):
        if isinstance(value, list):
            self._refer_list = list()
            for i in value:
                self._refer_list.append(i)


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
        if self.limit_type:
            if hasattr(self.limit_type, 'to_alipay_dict'):
                params['limit_type'] = self.limit_type.to_alipay_dict()
            else:
                params['limit_type'] = self.limit_type
        if self.no_refer_access:
            if hasattr(self.no_refer_access, 'to_alipay_dict'):
                params['no_refer_access'] = self.no_refer_access.to_alipay_dict()
            else:
                params['no_refer_access'] = self.no_refer_access
        if self.refer_list:
            if isinstance(self.refer_list, list):
                for i in range(0, len(self.refer_list)):
                    element = self.refer_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refer_list[i] = element.to_alipay_dict()
            if hasattr(self.refer_list, 'to_alipay_dict'):
                params['refer_list'] = self.refer_list.to_alipay_dict()
            else:
                params['refer_list'] = self.refer_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudrunStaticsiteRefererModifyModel()
        if 'assume_token' in d:
            o.assume_token = d['assume_token']
        if 'enable' in d:
            o.enable = d['enable']
        if 'env' in d:
            o.env = d['env']
        if 'limit_type' in d:
            o.limit_type = d['limit_type']
        if 'no_refer_access' in d:
            o.no_refer_access = d['no_refer_access']
        if 'refer_list' in d:
            o.refer_list = d['refer_list']
        return o


