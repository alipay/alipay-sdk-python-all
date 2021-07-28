#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TextDiff(object):

    def __init__(self):
        self._operation = None
        self._text = None

    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, value):
        self._operation = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.operation:
            if hasattr(self.operation, 'to_alipay_dict'):
                params['operation'] = self.operation.to_alipay_dict()
            else:
                params['operation'] = self.operation
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TextDiff()
        if 'operation' in d:
            o.operation = d['operation']
        if 'text' in d:
            o.text = d['text']
        return o


