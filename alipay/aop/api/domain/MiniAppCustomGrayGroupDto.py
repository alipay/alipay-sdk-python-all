#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniAppCustomGrayGroupDto(object):

    def __init__(self):
        self._name = None
        self._rule_code = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def rule_code(self):
        return self._rule_code

    @rule_code.setter
    def rule_code(self, value):
        self._rule_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.rule_code:
            if hasattr(self.rule_code, 'to_alipay_dict'):
                params['rule_code'] = self.rule_code.to_alipay_dict()
            else:
                params['rule_code'] = self.rule_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniAppCustomGrayGroupDto()
        if 'name' in d:
            o.name = d['name']
        if 'rule_code' in d:
            o.rule_code = d['rule_code']
        return o


