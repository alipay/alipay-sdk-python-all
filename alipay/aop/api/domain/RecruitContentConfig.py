#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecruitContentConfig(object):

    def __init__(self):
        self._config_code = None
        self._config_value = None

    @property
    def config_code(self):
        return self._config_code

    @config_code.setter
    def config_code(self, value):
        self._config_code = value
    @property
    def config_value(self):
        return self._config_value

    @config_value.setter
    def config_value(self, value):
        self._config_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.config_code:
            if hasattr(self.config_code, 'to_alipay_dict'):
                params['config_code'] = self.config_code.to_alipay_dict()
            else:
                params['config_code'] = self.config_code
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
        o = RecruitContentConfig()
        if 'config_code' in d:
            o.config_code = d['config_code']
        if 'config_value' in d:
            o.config_value = d['config_value']
        return o


