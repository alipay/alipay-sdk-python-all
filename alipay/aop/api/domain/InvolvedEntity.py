#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvolvedEntity(object):

    def __init__(self):
        self._code = None
        self._code_type = None
        self._name = None
        self._type = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def code_type(self):
        return self._code_type

    @code_type.setter
    def code_type(self, value):
        self._code_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.code_type:
            if hasattr(self.code_type, 'to_alipay_dict'):
                params['code_type'] = self.code_type.to_alipay_dict()
            else:
                params['code_type'] = self.code_type
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvolvedEntity()
        if 'code' in d:
            o.code = d['code']
        if 'code_type' in d:
            o.code_type = d['code_type']
        if 'name' in d:
            o.name = d['name']
        if 'type' in d:
            o.type = d['type']
        return o


