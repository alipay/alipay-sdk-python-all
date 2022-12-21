#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperationOpenbizmockPutQueryModel(object):

    def __init__(self):
        self._b_query = None
        self._c_body = None

    @property
    def b_query(self):
        return self._b_query

    @b_query.setter
    def b_query(self, value):
        self._b_query = value
    @property
    def c_body(self):
        return self._c_body

    @c_body.setter
    def c_body(self, value):
        self._c_body = value


    def to_alipay_dict(self):
        params = dict()
        if self.b_query:
            if hasattr(self.b_query, 'to_alipay_dict'):
                params['b_query'] = self.b_query.to_alipay_dict()
            else:
                params['b_query'] = self.b_query
        if self.c_body:
            if hasattr(self.c_body, 'to_alipay_dict'):
                params['c_body'] = self.c_body.to_alipay_dict()
            else:
                params['c_body'] = self.c_body
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationOpenbizmockPutQueryModel()
        if 'b_query' in d:
            o.b_query = d['b_query']
        if 'c_body' in d:
            o.c_body = d['c_body']
        return o


