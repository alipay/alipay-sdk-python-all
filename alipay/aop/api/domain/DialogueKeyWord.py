#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DialogueKeyWord(object):

    def __init__(self):
        self._from = None
        self._to = None

    @property
    def from(self):
        return self._from

    @from.setter
    def from(self, value):
        self._from = value
    @property
    def to(self):
        return self._to

    @to.setter
    def to(self, value):
        self._to = value


    def to_alipay_dict(self):
        params = dict()
        if self.from:
            if hasattr(self.from, 'to_alipay_dict'):
                params['from'] = self.from.to_alipay_dict()
            else:
                params['from'] = self.from
        if self.to:
            if hasattr(self.to, 'to_alipay_dict'):
                params['to'] = self.to.to_alipay_dict()
            else:
                params['to'] = self.to
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DialogueKeyWord()
        if 'from' in d:
            o.from = d['from']
        if 'to' in d:
            o.to = d['to']
        return o


