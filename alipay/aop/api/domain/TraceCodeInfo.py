#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TraceCodeInfo(object):

    def __init__(self):
        self._app_item_code = None
        self._trace_codes = None

    @property
    def app_item_code(self):
        return self._app_item_code

    @app_item_code.setter
    def app_item_code(self, value):
        self._app_item_code = value
    @property
    def trace_codes(self):
        return self._trace_codes

    @trace_codes.setter
    def trace_codes(self, value):
        if isinstance(value, list):
            self._trace_codes = list()
            for i in value:
                self._trace_codes.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.app_item_code:
            if hasattr(self.app_item_code, 'to_alipay_dict'):
                params['app_item_code'] = self.app_item_code.to_alipay_dict()
            else:
                params['app_item_code'] = self.app_item_code
        if self.trace_codes:
            if isinstance(self.trace_codes, list):
                for i in range(0, len(self.trace_codes)):
                    element = self.trace_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trace_codes[i] = element.to_alipay_dict()
            if hasattr(self.trace_codes, 'to_alipay_dict'):
                params['trace_codes'] = self.trace_codes.to_alipay_dict()
            else:
                params['trace_codes'] = self.trace_codes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TraceCodeInfo()
        if 'app_item_code' in d:
            o.app_item_code = d['app_item_code']
        if 'trace_codes' in d:
            o.trace_codes = d['trace_codes']
        return o


