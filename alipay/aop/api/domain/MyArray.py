#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MyArray(object):

    def __init__(self):
        self._aa = None

    @property
    def aa(self):
        return self._aa

    @aa.setter
    def aa(self, value):
        if isinstance(value, list):
            self._aa = list()
            for i in value:
                self._aa.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.aa:
            if isinstance(self.aa, list):
                for i in range(0, len(self.aa)):
                    element = self.aa[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.aa[i] = element.to_alipay_dict()
            if hasattr(self.aa, 'to_alipay_dict'):
                params['aa'] = self.aa.to_alipay_dict()
            else:
                params['aa'] = self.aa
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MyArray()
        if 'aa' in d:
            o.aa = d['aa']
        return o


