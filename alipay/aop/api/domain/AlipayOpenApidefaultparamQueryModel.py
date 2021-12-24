#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenApidefaultparamQueryModel(object):

    def __init__(self):
        self._interface_name = None

    @property
    def interface_name(self):
        return self._interface_name

    @interface_name.setter
    def interface_name(self, value):
        self._interface_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.interface_name:
            if hasattr(self.interface_name, 'to_alipay_dict'):
                params['interface_name'] = self.interface_name.to_alipay_dict()
            else:
                params['interface_name'] = self.interface_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenApidefaultparamQueryModel()
        if 'interface_name' in d:
            o.interface_name = d['interface_name']
        return o


