#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CheckPointVO(object):

    def __init__(self):
        self._is_pass = None
        self._name = None

    @property
    def is_pass(self):
        return self._is_pass

    @is_pass.setter
    def is_pass(self, value):
        self._is_pass = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.is_pass:
            if hasattr(self.is_pass, 'to_alipay_dict'):
                params['is_pass'] = self.is_pass.to_alipay_dict()
            else:
                params['is_pass'] = self.is_pass
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CheckPointVO()
        if 'is_pass' in d:
            o.is_pass = d['is_pass']
        if 'name' in d:
            o.name = d['name']
        return o


