#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportWorldCardscriptQueryModel(object):

    def __init__(self):
        self._script_name = None
        self._script_type = None

    @property
    def script_name(self):
        return self._script_name

    @script_name.setter
    def script_name(self, value):
        self._script_name = value
    @property
    def script_type(self):
        return self._script_type

    @script_type.setter
    def script_type(self, value):
        self._script_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.script_name:
            if hasattr(self.script_name, 'to_alipay_dict'):
                params['script_name'] = self.script_name.to_alipay_dict()
            else:
                params['script_name'] = self.script_name
        if self.script_type:
            if hasattr(self.script_type, 'to_alipay_dict'):
                params['script_type'] = self.script_type.to_alipay_dict()
            else:
                params['script_type'] = self.script_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportWorldCardscriptQueryModel()
        if 'script_name' in d:
            o.script_name = d['script_name']
        if 'script_type' in d:
            o.script_type = d['script_type']
        return o


