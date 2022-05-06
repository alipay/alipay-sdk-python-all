#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NotifyTriggerExt(object):

    def __init__(self):
        self._default_value = None
        self._desc = None
        self._name = None

    @property
    def default_value(self):
        return self._default_value

    @default_value.setter
    def default_value(self, value):
        self._default_value = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.default_value:
            if hasattr(self.default_value, 'to_alipay_dict'):
                params['default_value'] = self.default_value.to_alipay_dict()
            else:
                params['default_value'] = self.default_value
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
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
        o = NotifyTriggerExt()
        if 'default_value' in d:
            o.default_value = d['default_value']
        if 'desc' in d:
            o.desc = d['desc']
        if 'name' in d:
            o.name = d['name']
        return o


