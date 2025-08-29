#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenPayResultModule import OpenPayResultModule


class OpenPayResult(object):

    def __init__(self):
        self._modules = None

    @property
    def modules(self):
        return self._modules

    @modules.setter
    def modules(self, value):
        if isinstance(value, list):
            self._modules = list()
            for i in value:
                if isinstance(i, OpenPayResultModule):
                    self._modules.append(i)
                else:
                    self._modules.append(OpenPayResultModule.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.modules:
            if isinstance(self.modules, list):
                for i in range(0, len(self.modules)):
                    element = self.modules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.modules[i] = element.to_alipay_dict()
            if hasattr(self.modules, 'to_alipay_dict'):
                params['modules'] = self.modules.to_alipay_dict()
            else:
                params['modules'] = self.modules
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenPayResult()
        if 'modules' in d:
            o.modules = d['modules']
        return o


