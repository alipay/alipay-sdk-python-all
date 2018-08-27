#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MyObjectDdd(object):

    def __init__(self):
        self._param = None

    @property
    def param(self):
        return self._param

    @param.setter
    def param(self, value):
        self._param = value


    def to_alipay_dict(self):
        params = dict()
        if self.param:
            if hasattr(self.param, 'to_alipay_dict'):
                params['param'] = self.param.to_alipay_dict()
            else:
                params['param'] = self.param
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MyObjectDdd()
        if 'param' in d:
            o.param = d['param']
        return o


