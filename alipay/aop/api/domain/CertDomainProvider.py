#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AcmeKeyConfig import AcmeKeyConfig


class CertDomainProvider(object):

    def __init__(self):
        self._acme_key_configs = None
        self._display_name = None
        self._name = None

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
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        self._display_name = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


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
        if self.display_name:
            if hasattr(self.display_name, 'to_alipay_dict'):
                params['display_name'] = self.display_name.to_alipay_dict()
            else:
                params['display_name'] = self.display_name
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertDomainProvider()
        if 'acme_key_configs' in d:
            o.acme_key_configs = d['acme_key_configs']
        if 'display_name' in d:
            o.display_name = d['display_name']
        if 'name' in d:
            o.name = d['name']
        return o


