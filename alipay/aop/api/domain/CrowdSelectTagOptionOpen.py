#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CrowdSelectTagSubOptionOpen import CrowdSelectTagSubOptionOpen


class CrowdSelectTagOptionOpen(object):

    def __init__(self):
        self._children = None
        self._text = None
        self._value = None

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, value):
        if isinstance(value, list):
            self._children = list()
            for i in value:
                if isinstance(i, CrowdSelectTagSubOptionOpen):
                    self._children.append(i)
                else:
                    self._children.append(CrowdSelectTagSubOptionOpen.from_alipay_dict(i))
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


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
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CrowdSelectTagOptionOpen()
        if 'children' in d:
            o.children = d['children']
        if 'text' in d:
            o.text = d['text']
        if 'value' in d:
            o.value = d['value']
        return o


