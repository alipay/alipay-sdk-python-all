#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AcmeKeyConfig import AcmeKeyConfig


class AlipayCloudCloudbaseHttpscerthostingCreateModel(object):

    def __init__(self):
        self._acme_key_configs = None
        self._biz_app_id = None
        self._biz_env_id = None
        self._description = None
        self._domain = None
        self._domain_provider = None
        self._domain_type = None
        self._name = None
        self._open = None

    @property
    def acme_key_configs(self):
        return self._acme_key_configs

    @acme_key_configs.setter
    def acme_key_configs(self, value):
        if isinstance(value, list):
            self._acme_key_configs = list()
            for i in value:
                if isinstance(i, AcmeKeyConfig):
                    self._acme_key_configs.append(i)
                else:
                    self._acme_key_configs.append(AcmeKeyConfig.from_alipay_dict(i))
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
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, value):
        self._domain = value
    @property
    def domain_provider(self):
        return self._domain_provider

    @domain_provider.setter
    def domain_provider(self, value):
        self._domain_provider = value
    @property
    def domain_type(self):
        return self._domain_type

    @domain_type.setter
    def domain_type(self, value):
        self._domain_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def open(self):
        return self._open

    @open.setter
    def open(self, value):
        self._open = value


    def to_alipay_dict(self):
        params = dict()
        if self.acme_key_configs:
            if isinstance(self.acme_key_configs, list):
                for i in range(0, len(self.acme_key_configs)):
                    element = self.acme_key_configs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.acme_key_configs[i] = element.to_alipay_dict()
            if hasattr(self.acme_key_configs, 'to_alipay_dict'):
                params['acme_key_configs'] = self.acme_key_configs.to_alipay_dict()
            else:
                params['acme_key_configs'] = self.acme_key_configs
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
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.domain:
            if hasattr(self.domain, 'to_alipay_dict'):
                params['domain'] = self.domain.to_alipay_dict()
            else:
                params['domain'] = self.domain
        if self.domain_provider:
            if hasattr(self.domain_provider, 'to_alipay_dict'):
                params['domain_provider'] = self.domain_provider.to_alipay_dict()
            else:
                params['domain_provider'] = self.domain_provider
        if self.domain_type:
            if hasattr(self.domain_type, 'to_alipay_dict'):
                params['domain_type'] = self.domain_type.to_alipay_dict()
            else:
                params['domain_type'] = self.domain_type
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.open:
            if hasattr(self.open, 'to_alipay_dict'):
                params['open'] = self.open.to_alipay_dict()
            else:
                params['open'] = self.open
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseHttpscerthostingCreateModel()
        if 'acme_key_configs' in d:
            o.acme_key_configs = d['acme_key_configs']
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'description' in d:
            o.description = d['description']
        if 'domain' in d:
            o.domain = d['domain']
        if 'domain_provider' in d:
            o.domain_provider = d['domain_provider']
        if 'domain_type' in d:
            o.domain_type = d['domain_type']
        if 'name' in d:
            o.name = d['name']
        if 'open' in d:
            o.open = d['open']
        return o


