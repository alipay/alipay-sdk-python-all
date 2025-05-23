#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalMiorinsuranceJumpurlQueryModel(object):

    def __init__(self):
        self._insurance_code = None
        self._mi_code = None
        self._source = None

    @property
    def insurance_code(self):
        return self._insurance_code

    @insurance_code.setter
    def insurance_code(self, value):
        self._insurance_code = value
    @property
    def mi_code(self):
        return self._mi_code

    @mi_code.setter
    def mi_code(self, value):
        self._mi_code = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.insurance_code:
            if hasattr(self.insurance_code, 'to_alipay_dict'):
                params['insurance_code'] = self.insurance_code.to_alipay_dict()
            else:
                params['insurance_code'] = self.insurance_code
        if self.mi_code:
            if hasattr(self.mi_code, 'to_alipay_dict'):
                params['mi_code'] = self.mi_code.to_alipay_dict()
            else:
                params['mi_code'] = self.mi_code
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalMiorinsuranceJumpurlQueryModel()
        if 'insurance_code' in d:
            o.insurance_code = d['insurance_code']
        if 'mi_code' in d:
            o.mi_code = d['mi_code']
        if 'source' in d:
            o.source = d['source']
        return o


