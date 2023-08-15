#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CorsSetting(object):

    def __init__(self):
        self._access_control_allow_origins = None
        self._access_control_max_age = None
        self._enabled = None

    @property
    def access_control_allow_origins(self):
        return self._access_control_allow_origins

    @access_control_allow_origins.setter
    def access_control_allow_origins(self, value):
        if isinstance(value, list):
            self._access_control_allow_origins = list()
            for i in value:
                self._access_control_allow_origins.append(i)
    @property
    def access_control_max_age(self):
        return self._access_control_max_age

    @access_control_max_age.setter
    def access_control_max_age(self, value):
        self._access_control_max_age = value
    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_control_allow_origins:
            if isinstance(self.access_control_allow_origins, list):
                for i in range(0, len(self.access_control_allow_origins)):
                    element = self.access_control_allow_origins[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.access_control_allow_origins[i] = element.to_alipay_dict()
            if hasattr(self.access_control_allow_origins, 'to_alipay_dict'):
                params['access_control_allow_origins'] = self.access_control_allow_origins.to_alipay_dict()
            else:
                params['access_control_allow_origins'] = self.access_control_allow_origins
        if self.access_control_max_age:
            if hasattr(self.access_control_max_age, 'to_alipay_dict'):
                params['access_control_max_age'] = self.access_control_max_age.to_alipay_dict()
            else:
                params['access_control_max_age'] = self.access_control_max_age
        if self.enabled:
            if hasattr(self.enabled, 'to_alipay_dict'):
                params['enabled'] = self.enabled.to_alipay_dict()
            else:
                params['enabled'] = self.enabled
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CorsSetting()
        if 'access_control_allow_origins' in d:
            o.access_control_allow_origins = d['access_control_allow_origins']
        if 'access_control_max_age' in d:
            o.access_control_max_age = d['access_control_max_age']
        if 'enabled' in d:
            o.enabled = d['enabled']
        return o


