#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCcmRobotAvatarbaseQueryModel(object):

    def __init__(self):
        self._commodity_code = None
        self._method_params = None
        self._target_method = None
        self._tenant_code = None

    @property
    def commodity_code(self):
        return self._commodity_code

    @commodity_code.setter
    def commodity_code(self, value):
        self._commodity_code = value
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
    @property
    def tenant_code(self):
        return self._tenant_code

    @tenant_code.setter
    def tenant_code(self, value):
        self._tenant_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.commodity_code:
            if hasattr(self.commodity_code, 'to_alipay_dict'):
                params['commodity_code'] = self.commodity_code.to_alipay_dict()
            else:
                params['commodity_code'] = self.commodity_code
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
        if self.tenant_code:
            if hasattr(self.tenant_code, 'to_alipay_dict'):
                params['tenant_code'] = self.tenant_code.to_alipay_dict()
            else:
                params['tenant_code'] = self.tenant_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmRobotAvatarbaseQueryModel()
        if 'commodity_code' in d:
            o.commodity_code = d['commodity_code']
        if 'method_params' in d:
            o.method_params = d['method_params']
        if 'target_method' in d:
            o.target_method = d['target_method']
        if 'tenant_code' in d:
            o.tenant_code = d['tenant_code']
        return o


