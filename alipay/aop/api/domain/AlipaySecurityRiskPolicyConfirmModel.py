#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskPolicyConfirmModel(object):

    def __init__(self):
        self._confirm_params = None
        self._security_id = None

    @property
    def confirm_params(self):
        return self._confirm_params

    @confirm_params.setter
    def confirm_params(self, value):
        self._confirm_params = value
    @property
    def security_id(self):
        return self._security_id

    @security_id.setter
    def security_id(self, value):
        self._security_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.confirm_params:
            if hasattr(self.confirm_params, 'to_alipay_dict'):
                params['confirm_params'] = self.confirm_params.to_alipay_dict()
            else:
                params['confirm_params'] = self.confirm_params
        if self.security_id:
            if hasattr(self.security_id, 'to_alipay_dict'):
                params['security_id'] = self.security_id.to_alipay_dict()
            else:
                params['security_id'] = self.security_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskPolicyConfirmModel()
        if 'confirm_params' in d:
            o.confirm_params = d['confirm_params']
        if 'security_id' in d:
            o.security_id = d['security_id']
        return o


