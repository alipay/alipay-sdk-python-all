#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskHufuAuthQueryModel(object):

    def __init__(self):
        self._code = None
        self._policy = None
        self._serial = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def policy(self):
        return self._policy

    @policy.setter
    def policy(self, value):
        self._policy = value
    @property
    def serial(self):
        return self._serial

    @serial.setter
    def serial(self, value):
        self._serial = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.policy:
            if hasattr(self.policy, 'to_alipay_dict'):
                params['policy'] = self.policy.to_alipay_dict()
            else:
                params['policy'] = self.policy
        if self.serial:
            if hasattr(self.serial, 'to_alipay_dict'):
                params['serial'] = self.serial.to_alipay_dict()
            else:
                params['serial'] = self.serial
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskHufuAuthQueryModel()
        if 'code' in d:
            o.code = d['code']
        if 'policy' in d:
            o.policy = d['policy']
        if 'serial' in d:
            o.serial = d['serial']
        return o


