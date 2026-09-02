#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VcpBizIndicatorChildren(object):

    def __init__(self):
        self._target_code = None
        self._target_name = None

    @property
    def target_code(self):
        return self._target_code

    @target_code.setter
    def target_code(self, value):
        self._target_code = value
    @property
    def target_name(self):
        return self._target_name

    @target_name.setter
    def target_name(self, value):
        self._target_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.target_code:
            if hasattr(self.target_code, 'to_alipay_dict'):
                params['target_code'] = self.target_code.to_alipay_dict()
            else:
                params['target_code'] = self.target_code
        if self.target_name:
            if hasattr(self.target_name, 'to_alipay_dict'):
                params['target_name'] = self.target_name.to_alipay_dict()
            else:
                params['target_name'] = self.target_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VcpBizIndicatorChildren()
        if 'target_code' in d:
            o.target_code = d['target_code']
        if 'target_name' in d:
            o.target_name = d['target_name']
        return o


