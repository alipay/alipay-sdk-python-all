#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CustomUnitAmount(object):

    def __init__(self):
        self._enable = None
        self._maximum = None
        self._minimum = None
        self._preset = None

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value
    @property
    def maximum(self):
        return self._maximum

    @maximum.setter
    def maximum(self, value):
        self._maximum = value
    @property
    def minimum(self):
        return self._minimum

    @minimum.setter
    def minimum(self, value):
        self._minimum = value
    @property
    def preset(self):
        return self._preset

    @preset.setter
    def preset(self, value):
        self._preset = value


    def to_alipay_dict(self):
        params = dict()
        if self.enable:
            if hasattr(self.enable, 'to_alipay_dict'):
                params['enable'] = self.enable.to_alipay_dict()
            else:
                params['enable'] = self.enable
        if self.maximum:
            if hasattr(self.maximum, 'to_alipay_dict'):
                params['maximum'] = self.maximum.to_alipay_dict()
            else:
                params['maximum'] = self.maximum
        if self.minimum:
            if hasattr(self.minimum, 'to_alipay_dict'):
                params['minimum'] = self.minimum.to_alipay_dict()
            else:
                params['minimum'] = self.minimum
        if self.preset:
            if hasattr(self.preset, 'to_alipay_dict'):
                params['preset'] = self.preset.to_alipay_dict()
            else:
                params['preset'] = self.preset
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomUnitAmount()
        if 'enable' in d:
            o.enable = d['enable']
        if 'maximum' in d:
            o.maximum = d['maximum']
        if 'minimum' in d:
            o.minimum = d['minimum']
        if 'preset' in d:
            o.preset = d['preset']
        return o


