#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GavintestNewLeveaOne(object):

    def __init__(self):
        self._boolen = None
        self._ces = None
        self._des = None
        self._str = None

    @property
    def boolen(self):
        return self._boolen

    @boolen.setter
    def boolen(self, value):
        self._boolen = value
    @property
    def ces(self):
        return self._ces

    @ces.setter
    def ces(self, value):
        if isinstance(value, list):
            self._ces = list()
            for i in value:
                self._ces.append(i)
    @property
    def des(self):
        return self._des

    @des.setter
    def des(self, value):
        self._des = value
    @property
    def str(self):
        return self._str

    @str.setter
    def str(self, value):
        if isinstance(value, list):
            self._str = list()
            for i in value:
                self._str.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.boolen:
            if hasattr(self.boolen, 'to_alipay_dict'):
                params['boolen'] = self.boolen.to_alipay_dict()
            else:
                params['boolen'] = self.boolen
        if self.ces:
            if isinstance(self.ces, list):
                for i in range(0, len(self.ces)):
                    element = self.ces[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ces[i] = element.to_alipay_dict()
            if hasattr(self.ces, 'to_alipay_dict'):
                params['ces'] = self.ces.to_alipay_dict()
            else:
                params['ces'] = self.ces
        if self.des:
            if hasattr(self.des, 'to_alipay_dict'):
                params['des'] = self.des.to_alipay_dict()
            else:
                params['des'] = self.des
        if self.str:
            if isinstance(self.str, list):
                for i in range(0, len(self.str)):
                    element = self.str[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.str[i] = element.to_alipay_dict()
            if hasattr(self.str, 'to_alipay_dict'):
                params['str'] = self.str.to_alipay_dict()
            else:
                params['str'] = self.str
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GavintestNewLeveaOne()
        if 'boolen' in d:
            o.boolen = d['boolen']
        if 'ces' in d:
            o.ces = d['ces']
        if 'des' in d:
            o.des = d['des']
        if 'str' in d:
            o.str = d['str']
        return o


