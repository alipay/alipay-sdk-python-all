#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GavintestNewLeveaOne import GavintestNewLeveaOne
from alipay.aop.api.domain.Gavinmed import Gavinmed


class AlipayOpenAppReproCesCreateModel(object):

    def __init__(self):
        self._comp = None
        self._nam = None
        self._str = None

    @property
    def comp(self):
        return self._comp

    @comp.setter
    def comp(self, value):
        if isinstance(value, list):
            self._comp = list()
            for i in value:
                if isinstance(i, GavintestNewLeveaOne):
                    self._comp.append(i)
                else:
                    self._comp.append(GavintestNewLeveaOne.from_alipay_dict(i))
    @property
    def nam(self):
        return self._nam

    @nam.setter
    def nam(self, value):
        if isinstance(value, Gavinmed):
            self._nam = value
        else:
            self._nam = Gavinmed.from_alipay_dict(value)
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
        if self.comp:
            if isinstance(self.comp, list):
                for i in range(0, len(self.comp)):
                    element = self.comp[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.comp[i] = element.to_alipay_dict()
            if hasattr(self.comp, 'to_alipay_dict'):
                params['comp'] = self.comp.to_alipay_dict()
            else:
                params['comp'] = self.comp
        if self.nam:
            if hasattr(self.nam, 'to_alipay_dict'):
                params['nam'] = self.nam.to_alipay_dict()
            else:
                params['nam'] = self.nam
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
        o = AlipayOpenAppReproCesCreateModel()
        if 'comp' in d:
            o.comp = d['comp']
        if 'nam' in d:
            o.nam = d['nam']
        if 'str' in d:
            o.str = d['str']
        return o


