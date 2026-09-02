#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SdkPrivacyFields(object):

    def __init__(self):
        self._code = None
        self._name = None
        self._purpose = None
        self._sdk_name = None
        self._sdk_provider_name = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def purpose(self):
        return self._purpose

    @purpose.setter
    def purpose(self, value):
        self._purpose = value
    @property
    def sdk_name(self):
        return self._sdk_name

    @sdk_name.setter
    def sdk_name(self, value):
        self._sdk_name = value
    @property
    def sdk_provider_name(self):
        return self._sdk_provider_name

    @sdk_provider_name.setter
    def sdk_provider_name(self, value):
        self._sdk_provider_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.purpose:
            if hasattr(self.purpose, 'to_alipay_dict'):
                params['purpose'] = self.purpose.to_alipay_dict()
            else:
                params['purpose'] = self.purpose
        if self.sdk_name:
            if hasattr(self.sdk_name, 'to_alipay_dict'):
                params['sdk_name'] = self.sdk_name.to_alipay_dict()
            else:
                params['sdk_name'] = self.sdk_name
        if self.sdk_provider_name:
            if hasattr(self.sdk_provider_name, 'to_alipay_dict'):
                params['sdk_provider_name'] = self.sdk_provider_name.to_alipay_dict()
            else:
                params['sdk_provider_name'] = self.sdk_provider_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SdkPrivacyFields()
        if 'code' in d:
            o.code = d['code']
        if 'name' in d:
            o.name = d['name']
        if 'purpose' in d:
            o.purpose = d['purpose']
        if 'sdk_name' in d:
            o.sdk_name = d['sdk_name']
        if 'sdk_provider_name' in d:
            o.sdk_provider_name = d['sdk_provider_name']
        return o


