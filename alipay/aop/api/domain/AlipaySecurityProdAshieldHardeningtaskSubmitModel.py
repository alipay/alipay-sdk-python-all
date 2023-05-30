#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ClassMethodConfig import ClassMethodConfig
from alipay.aop.api.domain.RuntimeProtectConfig import RuntimeProtectConfig


class AlipaySecurityProdAshieldHardeningtaskSubmitModel(object):

    def __init__(self):
        self._assets_protect = None
        self._assets_protect_config = None
        self._enable_life_func = None
        self._file_url = None
        self._javatoc_jni_config = None
        self._runtime_protect_config = None
        self._so_protect = None
        self._so_protect_config = None

    @property
    def assets_protect(self):
        return self._assets_protect

    @assets_protect.setter
    def assets_protect(self, value):
        self._assets_protect = value
    @property
    def assets_protect_config(self):
        return self._assets_protect_config

    @assets_protect_config.setter
    def assets_protect_config(self, value):
        self._assets_protect_config = value
    @property
    def enable_life_func(self):
        return self._enable_life_func

    @enable_life_func.setter
    def enable_life_func(self, value):
        self._enable_life_func = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def javatoc_jni_config(self):
        return self._javatoc_jni_config

    @javatoc_jni_config.setter
    def javatoc_jni_config(self, value):
        if isinstance(value, list):
            self._javatoc_jni_config = list()
            for i in value:
                if isinstance(i, ClassMethodConfig):
                    self._javatoc_jni_config.append(i)
                else:
                    self._javatoc_jni_config.append(ClassMethodConfig.from_alipay_dict(i))
    @property
    def runtime_protect_config(self):
        return self._runtime_protect_config

    @runtime_protect_config.setter
    def runtime_protect_config(self, value):
        if isinstance(value, RuntimeProtectConfig):
            self._runtime_protect_config = value
        else:
            self._runtime_protect_config = RuntimeProtectConfig.from_alipay_dict(value)
    @property
    def so_protect(self):
        return self._so_protect

    @so_protect.setter
    def so_protect(self, value):
        self._so_protect = value
    @property
    def so_protect_config(self):
        return self._so_protect_config

    @so_protect_config.setter
    def so_protect_config(self, value):
        self._so_protect_config = value


    def to_alipay_dict(self):
        params = dict()
        if self.assets_protect:
            if hasattr(self.assets_protect, 'to_alipay_dict'):
                params['assets_protect'] = self.assets_protect.to_alipay_dict()
            else:
                params['assets_protect'] = self.assets_protect
        if self.assets_protect_config:
            if hasattr(self.assets_protect_config, 'to_alipay_dict'):
                params['assets_protect_config'] = self.assets_protect_config.to_alipay_dict()
            else:
                params['assets_protect_config'] = self.assets_protect_config
        if self.enable_life_func:
            if hasattr(self.enable_life_func, 'to_alipay_dict'):
                params['enable_life_func'] = self.enable_life_func.to_alipay_dict()
            else:
                params['enable_life_func'] = self.enable_life_func
        if self.file_url:
            if hasattr(self.file_url, 'to_alipay_dict'):
                params['file_url'] = self.file_url.to_alipay_dict()
            else:
                params['file_url'] = self.file_url
        if self.javatoc_jni_config:
            if isinstance(self.javatoc_jni_config, list):
                for i in range(0, len(self.javatoc_jni_config)):
                    element = self.javatoc_jni_config[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.javatoc_jni_config[i] = element.to_alipay_dict()
            if hasattr(self.javatoc_jni_config, 'to_alipay_dict'):
                params['javatoc_jni_config'] = self.javatoc_jni_config.to_alipay_dict()
            else:
                params['javatoc_jni_config'] = self.javatoc_jni_config
        if self.runtime_protect_config:
            if hasattr(self.runtime_protect_config, 'to_alipay_dict'):
                params['runtime_protect_config'] = self.runtime_protect_config.to_alipay_dict()
            else:
                params['runtime_protect_config'] = self.runtime_protect_config
        if self.so_protect:
            if hasattr(self.so_protect, 'to_alipay_dict'):
                params['so_protect'] = self.so_protect.to_alipay_dict()
            else:
                params['so_protect'] = self.so_protect
        if self.so_protect_config:
            if hasattr(self.so_protect_config, 'to_alipay_dict'):
                params['so_protect_config'] = self.so_protect_config.to_alipay_dict()
            else:
                params['so_protect_config'] = self.so_protect_config
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdAshieldHardeningtaskSubmitModel()
        if 'assets_protect' in d:
            o.assets_protect = d['assets_protect']
        if 'assets_protect_config' in d:
            o.assets_protect_config = d['assets_protect_config']
        if 'enable_life_func' in d:
            o.enable_life_func = d['enable_life_func']
        if 'file_url' in d:
            o.file_url = d['file_url']
        if 'javatoc_jni_config' in d:
            o.javatoc_jni_config = d['javatoc_jni_config']
        if 'runtime_protect_config' in d:
            o.runtime_protect_config = d['runtime_protect_config']
        if 'so_protect' in d:
            o.so_protect = d['so_protect']
        if 'so_protect_config' in d:
            o.so_protect_config = d['so_protect_config']
        return o


