#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudrunStaticsiteDomaincertModifyModel(object):

    def __init__(self):
        self._assume_token = None
        self._cert_private_key = None
        self._certificate = None
        self._domain_name = None
        self._env = None

    @property
    def assume_token(self):
        return self._assume_token

    @assume_token.setter
    def assume_token(self, value):
        self._assume_token = value
    @property
    def cert_private_key(self):
        return self._cert_private_key

    @cert_private_key.setter
    def cert_private_key(self, value):
        self._cert_private_key = value
    @property
    def certificate(self):
        return self._certificate

    @certificate.setter
    def certificate(self, value):
        self._certificate = value
    @property
    def domain_name(self):
        return self._domain_name

    @domain_name.setter
    def domain_name(self, value):
        self._domain_name = value
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
        if self.cert_private_key:
            if hasattr(self.cert_private_key, 'to_alipay_dict'):
                params['cert_private_key'] = self.cert_private_key.to_alipay_dict()
            else:
                params['cert_private_key'] = self.cert_private_key
        if self.certificate:
            if hasattr(self.certificate, 'to_alipay_dict'):
                params['certificate'] = self.certificate.to_alipay_dict()
            else:
                params['certificate'] = self.certificate
        if self.domain_name:
            if hasattr(self.domain_name, 'to_alipay_dict'):
                params['domain_name'] = self.domain_name.to_alipay_dict()
            else:
                params['domain_name'] = self.domain_name
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
        o = AlipayCloudCloudrunStaticsiteDomaincertModifyModel()
        if 'assume_token' in d:
            o.assume_token = d['assume_token']
        if 'cert_private_key' in d:
            o.cert_private_key = d['cert_private_key']
        if 'certificate' in d:
            o.certificate = d['certificate']
        if 'domain_name' in d:
            o.domain_name = d['domain_name']
        if 'env' in d:
            o.env = d['env']
        return o


