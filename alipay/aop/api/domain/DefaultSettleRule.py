#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DefaultSettleRule(object):

    def __init__(self):
        self._default_settle_target = None
        self._default_settle_type = None

    @property
    def default_settle_target(self):
        return self._default_settle_target

    @default_settle_target.setter
    def default_settle_target(self, value):
        self._default_settle_target = value
    @property
    def default_settle_type(self):
        return self._default_settle_type

    @default_settle_type.setter
    def default_settle_type(self, value):
        self._default_settle_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.default_settle_target:
            if hasattr(self.default_settle_target, 'to_alipay_dict'):
                params['default_settle_target'] = self.default_settle_target.to_alipay_dict()
            else:
                params['default_settle_target'] = self.default_settle_target
        if self.default_settle_type:
            if hasattr(self.default_settle_type, 'to_alipay_dict'):
                params['default_settle_type'] = self.default_settle_type.to_alipay_dict()
            else:
                params['default_settle_type'] = self.default_settle_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DefaultSettleRule()
        if 'default_settle_target' in d:
            o.default_settle_target = d['default_settle_target']
        if 'default_settle_type' in d:
            o.default_settle_type = d['default_settle_type']
        return o


