#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExtraInfo(object):

    def __init__(self):
        self._extra_info_key = None
        self._extra_info_value = None

    @property
    def extra_info_key(self):
        return self._extra_info_key

    @extra_info_key.setter
    def extra_info_key(self, value):
        self._extra_info_key = value
    @property
    def extra_info_value(self):
        return self._extra_info_value

    @extra_info_value.setter
    def extra_info_value(self, value):
        self._extra_info_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.extra_info_key:
            if hasattr(self.extra_info_key, 'to_alipay_dict'):
                params['extra_info_key'] = self.extra_info_key.to_alipay_dict()
            else:
                params['extra_info_key'] = self.extra_info_key
        if self.extra_info_value:
            if hasattr(self.extra_info_value, 'to_alipay_dict'):
                params['extra_info_value'] = self.extra_info_value.to_alipay_dict()
            else:
                params['extra_info_value'] = self.extra_info_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExtraInfo()
        if 'extra_info_key' in d:
            o.extra_info_key = d['extra_info_key']
        if 'extra_info_value' in d:
            o.extra_info_value = d['extra_info_value']
        return o


