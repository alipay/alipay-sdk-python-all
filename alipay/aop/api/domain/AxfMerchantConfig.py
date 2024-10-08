#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AxfMerchantConfig(object):

    def __init__(self):
        self._config_key = None
        self._config_value = None

    @property
    def config_key(self):
        return self._config_key

    @config_key.setter
    def config_key(self, value):
        self._config_key = value
    @property
    def config_value(self):
        return self._config_value

    @config_value.setter
    def config_value(self, value):
        self._config_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.config_key:
            if hasattr(self.config_key, 'to_alipay_dict'):
                params['config_key'] = self.config_key.to_alipay_dict()
            else:
                params['config_key'] = self.config_key
        if self.config_value:
            if hasattr(self.config_value, 'to_alipay_dict'):
                params['config_value'] = self.config_value.to_alipay_dict()
            else:
                params['config_value'] = self.config_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AxfMerchantConfig()
        if 'config_key' in d:
            o.config_key = d['config_key']
        if 'config_value' in d:
            o.config_value = d['config_value']
        return o


