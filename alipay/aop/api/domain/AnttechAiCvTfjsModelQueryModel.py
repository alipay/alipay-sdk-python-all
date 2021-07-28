#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechAiCvTfjsModelQueryModel(object):

    def __init__(self):
        self._model_code = None
        self._model_version = None

    @property
    def model_code(self):
        return self._model_code

    @model_code.setter
    def model_code(self, value):
        self._model_code = value
    @property
    def model_version(self):
        return self._model_version

    @model_version.setter
    def model_version(self, value):
        self._model_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.model_code:
            if hasattr(self.model_code, 'to_alipay_dict'):
                params['model_code'] = self.model_code.to_alipay_dict()
            else:
                params['model_code'] = self.model_code
        if self.model_version:
            if hasattr(self.model_version, 'to_alipay_dict'):
                params['model_version'] = self.model_version.to_alipay_dict()
            else:
                params['model_version'] = self.model_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechAiCvTfjsModelQueryModel()
        if 'model_code' in d:
            o.model_code = d['model_code']
        if 'model_version' in d:
            o.model_version = d['model_version']
        return o


