#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppSilanApigrayQueryModel(object):

    def __init__(self):
        self._param_1 = None

    @property
    def param_1(self):
        return self._param_1

    @param_1.setter
    def param_1(self, value):
        self._param_1 = value


    def to_alipay_dict(self):
        params = dict()
        if self.param_1:
            if hasattr(self.param_1, 'to_alipay_dict'):
                params['param_1'] = self.param_1.to_alipay_dict()
            else:
                params['param_1'] = self.param_1
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppSilanApigrayQueryModel()
        if 'param_1' in d:
            o.param_1 = d['param_1']
        return o


