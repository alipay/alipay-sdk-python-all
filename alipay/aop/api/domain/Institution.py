#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Institution(object):

    def __init__(self):
        self._code = None
        self._name = None
        self._root_code = None
        self._root_name = None

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
    def root_code(self):
        return self._root_code

    @root_code.setter
    def root_code(self, value):
        self._root_code = value
    @property
    def root_name(self):
        return self._root_name

    @root_name.setter
    def root_name(self, value):
        self._root_name = value


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
        if self.root_code:
            if hasattr(self.root_code, 'to_alipay_dict'):
                params['root_code'] = self.root_code.to_alipay_dict()
            else:
                params['root_code'] = self.root_code
        if self.root_name:
            if hasattr(self.root_name, 'to_alipay_dict'):
                params['root_name'] = self.root_name.to_alipay_dict()
            else:
                params['root_name'] = self.root_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Institution()
        if 'code' in d:
            o.code = d['code']
        if 'name' in d:
            o.name = d['name']
        if 'root_code' in d:
            o.root_code = d['root_code']
        if 'root_name' in d:
            o.root_name = d['root_name']
        return o


