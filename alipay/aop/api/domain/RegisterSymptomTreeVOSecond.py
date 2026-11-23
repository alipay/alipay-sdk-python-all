#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RegisterSymptomTreeVOThird import RegisterSymptomTreeVOThird


class RegisterSymptomTreeVOSecond(object):

    def __init__(self):
        self._children = None
        self._level = None
        self._name = None

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, value):
        if isinstance(value, list):
            self._children = list()
            for i in value:
                if isinstance(i, RegisterSymptomTreeVOThird):
                    self._children.append(i)
                else:
                    self._children.append(RegisterSymptomTreeVOThird.from_alipay_dict(i))
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.children:
            if isinstance(self.children, list):
                for i in range(0, len(self.children)):
                    element = self.children[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.children[i] = element.to_alipay_dict()
            if hasattr(self.children, 'to_alipay_dict'):
                params['children'] = self.children.to_alipay_dict()
            else:
                params['children'] = self.children
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RegisterSymptomTreeVOSecond()
        if 'children' in d:
            o.children = d['children']
        if 'level' in d:
            o.level = d['level']
        if 'name' in d:
            o.name = d['name']
        return o


