#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCcmRobotAvatarbaseQueryModel(object):

    def __init__(self):
        self._method_params = None
        self._target_method = None

    @property
    def method_params(self):
        return self._method_params

    @method_params.setter
    def method_params(self, value):
        self._method_params = value
    @property
    def target_method(self):
        return self._target_method

    @target_method.setter
    def target_method(self, value):
        self._target_method = value


    def to_alipay_dict(self):
        params = dict()
        if self.method_params:
            if hasattr(self.method_params, 'to_alipay_dict'):
                params['method_params'] = self.method_params.to_alipay_dict()
            else:
                params['method_params'] = self.method_params
        if self.target_method:
            if hasattr(self.target_method, 'to_alipay_dict'):
                params['target_method'] = self.target_method.to_alipay_dict()
            else:
                params['target_method'] = self.target_method
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmRobotAvatarbaseQueryModel()
        if 'method_params' in d:
            o.method_params = d['method_params']
        if 'target_method' in d:
            o.target_method = d['target_method']
        return o


