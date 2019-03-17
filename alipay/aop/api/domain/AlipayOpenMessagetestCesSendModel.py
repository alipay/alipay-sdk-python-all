#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GavintestNewLeveaOne import GavintestNewLeveaOne


class AlipayOpenMessagetestCesSendModel(object):

    def __init__(self):
        self._cop = None
        self._str = None

    @property
    def cop(self):
        return self._cop

    @cop.setter
    def cop(self, value):
        if isinstance(value, list):
            self._cop = list()
            for i in value:
                if isinstance(i, GavintestNewLeveaOne):
                    self._cop.append(i)
                else:
                    self._cop.append(GavintestNewLeveaOne.from_alipay_dict(i))
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
        if self.cop:
            if isinstance(self.cop, list):
                for i in range(0, len(self.cop)):
                    element = self.cop[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cop[i] = element.to_alipay_dict()
            if hasattr(self.cop, 'to_alipay_dict'):
                params['cop'] = self.cop.to_alipay_dict()
            else:
                params['cop'] = self.cop
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
        o = AlipayOpenMessagetestCesSendModel()
        if 'cop' in d:
            o.cop = d['cop']
        if 'str' in d:
            o.str = d['str']
        return o


