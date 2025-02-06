#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FaqModel(object):

    def __init__(self):
        self._column_a = None
        self._column_q = None

    @property
    def column_a(self):
        return self._column_a

    @column_a.setter
    def column_a(self, value):
        self._column_a = value
    @property
    def column_q(self):
        return self._column_q

    @column_q.setter
    def column_q(self, value):
        self._column_q = value


    def to_alipay_dict(self):
        params = dict()
        if self.column_a:
            if hasattr(self.column_a, 'to_alipay_dict'):
                params['column_a'] = self.column_a.to_alipay_dict()
            else:
                params['column_a'] = self.column_a
        if self.column_q:
            if hasattr(self.column_q, 'to_alipay_dict'):
                params['column_q'] = self.column_q.to_alipay_dict()
            else:
                params['column_q'] = self.column_q
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FaqModel()
        if 'column_a' in d:
            o.column_a = d['column_a']
        if 'column_q' in d:
            o.column_q = d['column_q']
        return o


