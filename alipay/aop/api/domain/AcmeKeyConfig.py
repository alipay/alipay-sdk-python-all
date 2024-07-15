#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AcmeKeyConfig(object):

    def __init__(self):
        self._key_description = None
        self._key_name = None
        self._key_value = None

    @property
    def key_description(self):
        return self._key_description

    @key_description.setter
    def key_description(self, value):
        self._key_description = value
    @property
    def key_name(self):
        return self._key_name

    @key_name.setter
    def key_name(self, value):
        self._key_name = value
    @property
    def key_value(self):
        return self._key_value

    @key_value.setter
    def key_value(self, value):
        self._key_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.key_description:
            if hasattr(self.key_description, 'to_alipay_dict'):
                params['key_description'] = self.key_description.to_alipay_dict()
            else:
                params['key_description'] = self.key_description
        if self.key_name:
            if hasattr(self.key_name, 'to_alipay_dict'):
                params['key_name'] = self.key_name.to_alipay_dict()
            else:
                params['key_name'] = self.key_name
        if self.key_value:
            if hasattr(self.key_value, 'to_alipay_dict'):
                params['key_value'] = self.key_value.to_alipay_dict()
            else:
                params['key_value'] = self.key_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AcmeKeyConfig()
        if 'key_description' in d:
            o.key_description = d['key_description']
        if 'key_name' in d:
            o.key_name = d['key_name']
        if 'key_value' in d:
            o.key_value = d['key_value']
        return o


