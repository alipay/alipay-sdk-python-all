#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LoadInfoNode import LoadInfoNode
from alipay.aop.api.domain.LoadInfoNode import LoadInfoNode


class DeclareStrategy(object):

    def __init__(self):
        self._declare_adjustment = None
        self._declare_load = None

    @property
    def declare_adjustment(self):
        return self._declare_adjustment

    @declare_adjustment.setter
    def declare_adjustment(self, value):
        if isinstance(value, list):
            self._declare_adjustment = list()
            for i in value:
                if isinstance(i, LoadInfoNode):
                    self._declare_adjustment.append(i)
                else:
                    self._declare_adjustment.append(LoadInfoNode.from_alipay_dict(i))
    @property
    def declare_load(self):
        return self._declare_load

    @declare_load.setter
    def declare_load(self, value):
        if isinstance(value, list):
            self._declare_load = list()
            for i in value:
                if isinstance(i, LoadInfoNode):
                    self._declare_load.append(i)
                else:
                    self._declare_load.append(LoadInfoNode.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.declare_adjustment:
            if isinstance(self.declare_adjustment, list):
                for i in range(0, len(self.declare_adjustment)):
                    element = self.declare_adjustment[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.declare_adjustment[i] = element.to_alipay_dict()
            if hasattr(self.declare_adjustment, 'to_alipay_dict'):
                params['declare_adjustment'] = self.declare_adjustment.to_alipay_dict()
            else:
                params['declare_adjustment'] = self.declare_adjustment
        if self.declare_load:
            if isinstance(self.declare_load, list):
                for i in range(0, len(self.declare_load)):
                    element = self.declare_load[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.declare_load[i] = element.to_alipay_dict()
            if hasattr(self.declare_load, 'to_alipay_dict'):
                params['declare_load'] = self.declare_load.to_alipay_dict()
            else:
                params['declare_load'] = self.declare_load
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeclareStrategy()
        if 'declare_adjustment' in d:
            o.declare_adjustment = d['declare_adjustment']
        if 'declare_load' in d:
            o.declare_load = d['declare_load']
        return o


