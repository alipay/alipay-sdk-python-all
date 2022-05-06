#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserDefinePrivacyPolicyField(object):

    def __init__(self):
        self._name = None
        self._purpose = None

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


    def to_alipay_dict(self):
        params = dict()
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserDefinePrivacyPolicyField()
        if 'name' in d:
            o.name = d['name']
        if 'purpose' in d:
            o.purpose = d['purpose']
        return o


