#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AmountPartInfo(object):

    def __init__(self):
        self._after_dot = None
        self._before_dot = None

    @property
    def after_dot(self):
        return self._after_dot

    @after_dot.setter
    def after_dot(self, value):
        self._after_dot = value
    @property
    def before_dot(self):
        return self._before_dot

    @before_dot.setter
    def before_dot(self, value):
        self._before_dot = value


    def to_alipay_dict(self):
        params = dict()
        if self.after_dot:
            if hasattr(self.after_dot, 'to_alipay_dict'):
                params['after_dot'] = self.after_dot.to_alipay_dict()
            else:
                params['after_dot'] = self.after_dot
        if self.before_dot:
            if hasattr(self.before_dot, 'to_alipay_dict'):
                params['before_dot'] = self.before_dot.to_alipay_dict()
            else:
                params['before_dot'] = self.before_dot
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AmountPartInfo()
        if 'after_dot' in d:
            o.after_dot = d['after_dot']
        if 'before_dot' in d:
            o.before_dot = d['before_dot']
        return o


