#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseHttpaccessDomainCreateModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._biz_env_id = None
        self._name = None
        self._ssl_cert = None
        self._ssl_key = None

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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def ssl_cert(self):
        return self._ssl_cert

    @ssl_cert.setter
    def ssl_cert(self, value):
        self._ssl_cert = value
    @property
    def ssl_key(self):
        return self._ssl_key

    @ssl_key.setter
    def ssl_key(self, value):
        self._ssl_key = value


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
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.ssl_cert:
            if hasattr(self.ssl_cert, 'to_alipay_dict'):
                params['ssl_cert'] = self.ssl_cert.to_alipay_dict()
            else:
                params['ssl_cert'] = self.ssl_cert
        if self.ssl_key:
            if hasattr(self.ssl_key, 'to_alipay_dict'):
                params['ssl_key'] = self.ssl_key.to_alipay_dict()
            else:
                params['ssl_key'] = self.ssl_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseHttpaccessDomainCreateModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'name' in d:
            o.name = d['name']
        if 'ssl_cert' in d:
            o.ssl_cert = d['ssl_cert']
        if 'ssl_key' in d:
            o.ssl_key = d['ssl_key']
        return o


