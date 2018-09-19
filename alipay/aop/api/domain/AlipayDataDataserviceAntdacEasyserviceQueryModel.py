#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAntdacEasyserviceQueryModel(object):

    def __init__(self):
        self._method_id = None
        self._parameter_json = None

    @property
    def method_id(self):
        return self._method_id

    @method_id.setter
    def method_id(self, value):
        self._method_id = value
    @property
    def parameter_json(self):
        return self._parameter_json

    @parameter_json.setter
    def parameter_json(self, value):
        self._parameter_json = value


    def to_alipay_dict(self):
        params = dict()
        if self.method_id:
            if hasattr(self.method_id, 'to_alipay_dict'):
                params['method_id'] = self.method_id.to_alipay_dict()
            else:
                params['method_id'] = self.method_id
        if self.parameter_json:
            if hasattr(self.parameter_json, 'to_alipay_dict'):
                params['parameter_json'] = self.parameter_json.to_alipay_dict()
            else:
                params['parameter_json'] = self.parameter_json
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAntdacEasyserviceQueryModel()
        if 'method_id' in d:
            o.method_id = d['method_id']
        if 'parameter_json' in d:
            o.parameter_json = d['parameter_json']
        return o


