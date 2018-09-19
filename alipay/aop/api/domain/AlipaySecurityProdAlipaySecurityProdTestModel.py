#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdAlipaySecurityProdTestModel(object):

    def __init__(self):
        self._cds = None
        self._ddd = None

    @property
    def cds(self):
        return self._cds

    @cds.setter
    def cds(self, value):
        if isinstance(value, list):
            self._cds = list()
            for i in value:
                self._cds.append(i)
    @property
    def ddd(self):
        return self._ddd

    @ddd.setter
    def ddd(self, value):
        self._ddd = value


    def to_alipay_dict(self):
        params = dict()
        if self.cds:
            if isinstance(self.cds, list):
                for i in range(0, len(self.cds)):
                    element = self.cds[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cds[i] = element.to_alipay_dict()
            if hasattr(self.cds, 'to_alipay_dict'):
                params['cds'] = self.cds.to_alipay_dict()
            else:
                params['cds'] = self.cds
        if self.ddd:
            if hasattr(self.ddd, 'to_alipay_dict'):
                params['ddd'] = self.ddd.to_alipay_dict()
            else:
                params['ddd'] = self.ddd
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdAlipaySecurityProdTestModel()
        if 'cds' in d:
            o.cds = d['cds']
        if 'ddd' in d:
            o.ddd = d['ddd']
        return o


