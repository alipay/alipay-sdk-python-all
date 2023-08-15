#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RefererSetting(object):

    def __init__(self):
        self._enabled = None
        self._no_refer_access = None
        self._refer_list = None
        self._refer_type = None

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value
    @property
    def no_refer_access(self):
        return self._no_refer_access

    @no_refer_access.setter
    def no_refer_access(self, value):
        self._no_refer_access = value
    @property
    def refer_list(self):
        return self._refer_list

    @refer_list.setter
    def refer_list(self, value):
        if isinstance(value, list):
            self._refer_list = list()
            for i in value:
                self._refer_list.append(i)
    @property
    def refer_type(self):
        return self._refer_type

    @refer_type.setter
    def refer_type(self, value):
        self._refer_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.enabled:
            if hasattr(self.enabled, 'to_alipay_dict'):
                params['enabled'] = self.enabled.to_alipay_dict()
            else:
                params['enabled'] = self.enabled
        if self.no_refer_access:
            if hasattr(self.no_refer_access, 'to_alipay_dict'):
                params['no_refer_access'] = self.no_refer_access.to_alipay_dict()
            else:
                params['no_refer_access'] = self.no_refer_access
        if self.refer_list:
            if isinstance(self.refer_list, list):
                for i in range(0, len(self.refer_list)):
                    element = self.refer_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refer_list[i] = element.to_alipay_dict()
            if hasattr(self.refer_list, 'to_alipay_dict'):
                params['refer_list'] = self.refer_list.to_alipay_dict()
            else:
                params['refer_list'] = self.refer_list
        if self.refer_type:
            if hasattr(self.refer_type, 'to_alipay_dict'):
                params['refer_type'] = self.refer_type.to_alipay_dict()
            else:
                params['refer_type'] = self.refer_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RefererSetting()
        if 'enabled' in d:
            o.enabled = d['enabled']
        if 'no_refer_access' in d:
            o.no_refer_access = d['no_refer_access']
        if 'refer_list' in d:
            o.refer_list = d['refer_list']
        if 'refer_type' in d:
            o.refer_type = d['refer_type']
        return o


