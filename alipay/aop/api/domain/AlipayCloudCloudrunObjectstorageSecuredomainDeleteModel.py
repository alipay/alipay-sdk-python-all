#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudrunObjectstorageSecuredomainDeleteModel(object):

    def __init__(self):
        self._assume_token = None
        self._env = None
        self._secure_domain = None

    @property
    def assume_token(self):
        return self._assume_token

    @assume_token.setter
    def assume_token(self, value):
        self._assume_token = value
    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value
    @property
    def secure_domain(self):
        return self._secure_domain

    @secure_domain.setter
    def secure_domain(self, value):
        self._secure_domain = value


    def to_alipay_dict(self):
        params = dict()
        if self.assume_token:
            if hasattr(self.assume_token, 'to_alipay_dict'):
                params['assume_token'] = self.assume_token.to_alipay_dict()
            else:
                params['assume_token'] = self.assume_token
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
        if self.secure_domain:
            if hasattr(self.secure_domain, 'to_alipay_dict'):
                params['secure_domain'] = self.secure_domain.to_alipay_dict()
            else:
                params['secure_domain'] = self.secure_domain
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudrunObjectstorageSecuredomainDeleteModel()
        if 'assume_token' in d:
            o.assume_token = d['assume_token']
        if 'env' in d:
            o.env = d['env']
        if 'secure_domain' in d:
            o.secure_domain = d['secure_domain']
        return o


