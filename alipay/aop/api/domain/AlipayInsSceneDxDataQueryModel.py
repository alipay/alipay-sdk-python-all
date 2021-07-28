#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneDxDataQueryModel(object):

    def __init__(self):
        self._dx_name = None
        self._param = None

    @property
    def dx_name(self):
        return self._dx_name

    @dx_name.setter
    def dx_name(self, value):
        self._dx_name = value
    @property
    def param(self):
        return self._param

    @param.setter
    def param(self, value):
        self._param = value


    def to_alipay_dict(self):
        params = dict()
        if self.dx_name:
            if hasattr(self.dx_name, 'to_alipay_dict'):
                params['dx_name'] = self.dx_name.to_alipay_dict()
            else:
                params['dx_name'] = self.dx_name
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
        o = AlipayInsSceneDxDataQueryModel()
        if 'dx_name' in d:
            o.dx_name = d['dx_name']
        if 'param' in d:
            o.param = d['param']
        return o


