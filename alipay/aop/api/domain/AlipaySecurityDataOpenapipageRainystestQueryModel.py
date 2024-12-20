#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityDataOpenapipageRainystestQueryModel(object):

    def __init__(self):
        self._input_param_01 = None

    @property
    def input_param_01(self):
        return self._input_param_01

    @input_param_01.setter
    def input_param_01(self, value):
        self._input_param_01 = value


    def to_alipay_dict(self):
        params = dict()
        if self.input_param_01:
            if hasattr(self.input_param_01, 'to_alipay_dict'):
                params['input_param_01'] = self.input_param_01.to_alipay_dict()
            else:
                params['input_param_01'] = self.input_param_01
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityDataOpenapipageRainystestQueryModel()
        if 'input_param_01' in d:
            o.input_param_01 = d['input_param_01']
        return o


