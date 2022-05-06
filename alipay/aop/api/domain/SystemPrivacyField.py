#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SystemPrivacyField(object):

    def __init__(self):
        self._code = None
        self._interface_code = None
        self._purpose = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def interface_code(self):
        return self._interface_code

    @interface_code.setter
    def interface_code(self, value):
        self._interface_code = value
    @property
    def purpose(self):
        return self._purpose

    @purpose.setter
    def purpose(self, value):
        self._purpose = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.interface_code:
            if hasattr(self.interface_code, 'to_alipay_dict'):
                params['interface_code'] = self.interface_code.to_alipay_dict()
            else:
                params['interface_code'] = self.interface_code
        if self.purpose:
            if hasattr(self.purpose, 'to_alipay_dict'):
                params['purpose'] = self.purpose.to_alipay_dict()
            else:
                params['purpose'] = self.purpose
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SystemPrivacyField()
        if 'code' in d:
            o.code = d['code']
        if 'interface_code' in d:
            o.interface_code = d['interface_code']
        if 'purpose' in d:
            o.purpose = d['purpose']
        return o


