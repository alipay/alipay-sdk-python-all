#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneFinresearchModelConsultModel(object):

    def __init__(self):
        self._model_code = None
        self._model_input = None
        self._service_key = None

    @property
    def model_code(self):
        return self._model_code

    @model_code.setter
    def model_code(self, value):
        self._model_code = value
    @property
    def model_input(self):
        return self._model_input

    @model_input.setter
    def model_input(self, value):
        self._model_input = value
    @property
    def service_key(self):
        return self._service_key

    @service_key.setter
    def service_key(self, value):
        self._service_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.model_code:
            if hasattr(self.model_code, 'to_alipay_dict'):
                params['model_code'] = self.model_code.to_alipay_dict()
            else:
                params['model_code'] = self.model_code
        if self.model_input:
            if hasattr(self.model_input, 'to_alipay_dict'):
                params['model_input'] = self.model_input.to_alipay_dict()
            else:
                params['model_input'] = self.model_input
        if self.service_key:
            if hasattr(self.service_key, 'to_alipay_dict'):
                params['service_key'] = self.service_key.to_alipay_dict()
            else:
                params['service_key'] = self.service_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneFinresearchModelConsultModel()
        if 'model_code' in d:
            o.model_code = d['model_code']
        if 'model_input' in d:
            o.model_input = d['model_input']
        if 'service_key' in d:
            o.service_key = d['service_key']
        return o


