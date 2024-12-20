#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesTheFirst import RainyComplexTypesTheFirst


class AlipaySecurityDataOpenapisdkRainystestQueryModel(object):

    def __init__(self):
        self._input_param_01 = None
        self._ref_params = None

    @property
    def input_param_01(self):
        return self._input_param_01

    @input_param_01.setter
    def input_param_01(self, value):
        self._input_param_01 = value
    @property
    def ref_params(self):
        return self._ref_params

    @ref_params.setter
    def ref_params(self, value):
        if isinstance(value, RainyComplexTypesTheFirst):
            self._ref_params = value
        else:
            self._ref_params = RainyComplexTypesTheFirst.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.input_param_01:
            if hasattr(self.input_param_01, 'to_alipay_dict'):
                params['input_param_01'] = self.input_param_01.to_alipay_dict()
            else:
                params['input_param_01'] = self.input_param_01
        if self.ref_params:
            if hasattr(self.ref_params, 'to_alipay_dict'):
                params['ref_params'] = self.ref_params.to_alipay_dict()
            else:
                params['ref_params'] = self.ref_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityDataOpenapisdkRainystestQueryModel()
        if 'input_param_01' in d:
            o.input_param_01 = d['input_param_01']
        if 'ref_params' in d:
            o.ref_params = d['ref_params']
        return o


