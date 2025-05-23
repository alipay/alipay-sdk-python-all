#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InfraTemplateEnumRuleOptionResp(object):

    def __init__(self):
        self._code = None
        self._desc = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InfraTemplateEnumRuleOptionResp()
        if 'code' in d:
            o.code = d['code']
        if 'desc' in d:
            o.desc = d['desc']
        return o


