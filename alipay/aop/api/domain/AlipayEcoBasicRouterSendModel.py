#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoBasicRouterSendModel(object):

    def __init__(self):
        self._input = None
        self._interface_name = None
        self._trace_id = None

    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, value):
        self._input = value
    @property
    def interface_name(self):
        return self._interface_name

    @interface_name.setter
    def interface_name(self, value):
        self._interface_name = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.input:
            if hasattr(self.input, 'to_alipay_dict'):
                params['input'] = self.input.to_alipay_dict()
            else:
                params['input'] = self.input
        if self.interface_name:
            if hasattr(self.interface_name, 'to_alipay_dict'):
                params['interface_name'] = self.interface_name.to_alipay_dict()
            else:
                params['interface_name'] = self.interface_name
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoBasicRouterSendModel()
        if 'input' in d:
            o.input = d['input']
        if 'interface_name' in d:
            o.interface_name = d['interface_name']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        return o


