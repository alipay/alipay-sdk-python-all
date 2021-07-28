#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppOpenbizmockApisdkgrayQueryModel(object):

    def __init__(self):
        self._input_param = None

    @property
    def input_param(self):
        return self._input_param

    @input_param.setter
    def input_param(self, value):
        self._input_param = value


    def to_alipay_dict(self):
        params = dict()
        if self.input_param:
            if hasattr(self.input_param, 'to_alipay_dict'):
                params['input_param'] = self.input_param.to_alipay_dict()
            else:
                params['input_param'] = self.input_param
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppOpenbizmockApisdkgrayQueryModel()
        if 'input_param' in d:
            o.input_param = d['input_param']
        return o


