#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AIChatCustomerLike(object):

    def __init__(self):
        self._input_method = None

    @property
    def input_method(self):
        return self._input_method

    @input_method.setter
    def input_method(self, value):
        self._input_method = value


    def to_alipay_dict(self):
        params = dict()
        if self.input_method:
            if hasattr(self.input_method, 'to_alipay_dict'):
                params['input_method'] = self.input_method.to_alipay_dict()
            else:
                params['input_method'] = self.input_method
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AIChatCustomerLike()
        if 'input_method' in d:
            o.input_method = d['input_method']
        return o


