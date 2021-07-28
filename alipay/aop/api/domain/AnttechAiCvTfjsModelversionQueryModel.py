#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechAiCvTfjsModelversionQueryModel(object):

    def __init__(self):
        self._model_code = None

    @property
    def model_code(self):
        return self._model_code

    @model_code.setter
    def model_code(self, value):
        self._model_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.model_code:
            if hasattr(self.model_code, 'to_alipay_dict'):
                params['model_code'] = self.model_code.to_alipay_dict()
            else:
                params['model_code'] = self.model_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechAiCvTfjsModelversionQueryModel()
        if 'model_code' in d:
            o.model_code = d['model_code']
        return o


