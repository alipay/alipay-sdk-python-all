#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DormitoryConfig(object):

    def __init__(self):
        self._enable_multiple = None
        self._max_multiple = None

    @property
    def enable_multiple(self):
        return self._enable_multiple

    @enable_multiple.setter
    def enable_multiple(self, value):
        self._enable_multiple = value
    @property
    def max_multiple(self):
        return self._max_multiple

    @max_multiple.setter
    def max_multiple(self, value):
        self._max_multiple = value


    def to_alipay_dict(self):
        params = dict()
        if self.enable_multiple:
            if hasattr(self.enable_multiple, 'to_alipay_dict'):
                params['enable_multiple'] = self.enable_multiple.to_alipay_dict()
            else:
                params['enable_multiple'] = self.enable_multiple
        if self.max_multiple:
            if hasattr(self.max_multiple, 'to_alipay_dict'):
                params['max_multiple'] = self.max_multiple.to_alipay_dict()
            else:
                params['max_multiple'] = self.max_multiple
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DormitoryConfig()
        if 'enable_multiple' in d:
            o.enable_multiple = d['enable_multiple']
        if 'max_multiple' in d:
            o.max_multiple = d['max_multiple']
        return o


