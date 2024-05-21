#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardUseMethodInfo(object):

    def __init__(self):
        self._use_method_type = None
        self._use_path = None

    @property
    def use_method_type(self):
        return self._use_method_type

    @use_method_type.setter
    def use_method_type(self, value):
        self._use_method_type = value
    @property
    def use_path(self):
        return self._use_path

    @use_path.setter
    def use_path(self, value):
        self._use_path = value


    def to_alipay_dict(self):
        params = dict()
        if self.use_method_type:
            if hasattr(self.use_method_type, 'to_alipay_dict'):
                params['use_method_type'] = self.use_method_type.to_alipay_dict()
            else:
                params['use_method_type'] = self.use_method_type
        if self.use_path:
            if hasattr(self.use_path, 'to_alipay_dict'):
                params['use_path'] = self.use_path.to_alipay_dict()
            else:
                params['use_path'] = self.use_path
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardUseMethodInfo()
        if 'use_method_type' in d:
            o.use_method_type = d['use_method_type']
        if 'use_path' in d:
            o.use_path = d['use_path']
        return o


