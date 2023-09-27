#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcEnterpriseConfigModifyModel(object):

    def __init__(self):
        self._config_key = None
        self._config_value = None
        self._enterprise_id = None

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
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value


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
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcEnterpriseConfigModifyModel()
        if 'config_key' in d:
            o.config_key = d['config_key']
        if 'config_value' in d:
            o.config_value = d['config_value']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        return o


