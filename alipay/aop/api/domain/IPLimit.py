#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IPLimit(object):

    def __init__(self):
        self._enabled = None
        self._ip_list = None
        self._limit_type = None

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value
    @property
    def ip_list(self):
        return self._ip_list

    @ip_list.setter
    def ip_list(self, value):
        if isinstance(value, list):
            self._ip_list = list()
            for i in value:
                self._ip_list.append(i)
    @property
    def limit_type(self):
        return self._limit_type

    @limit_type.setter
    def limit_type(self, value):
        self._limit_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.enabled:
            if hasattr(self.enabled, 'to_alipay_dict'):
                params['enabled'] = self.enabled.to_alipay_dict()
            else:
                params['enabled'] = self.enabled
        if self.ip_list:
            if isinstance(self.ip_list, list):
                for i in range(0, len(self.ip_list)):
                    element = self.ip_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ip_list[i] = element.to_alipay_dict()
            if hasattr(self.ip_list, 'to_alipay_dict'):
                params['ip_list'] = self.ip_list.to_alipay_dict()
            else:
                params['ip_list'] = self.ip_list
        if self.limit_type:
            if hasattr(self.limit_type, 'to_alipay_dict'):
                params['limit_type'] = self.limit_type.to_alipay_dict()
            else:
                params['limit_type'] = self.limit_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IPLimit()
        if 'enabled' in d:
            o.enabled = d['enabled']
        if 'ip_list' in d:
            o.ip_list = d['ip_list']
        if 'limit_type' in d:
            o.limit_type = d['limit_type']
        return o


