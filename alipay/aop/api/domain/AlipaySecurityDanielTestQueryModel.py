#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityDanielTestQueryModel(object):

    def __init__(self):
        self._input_query = None

    @property
    def input_query(self):
        return self._input_query

    @input_query.setter
    def input_query(self, value):
        self._input_query = value


    def to_alipay_dict(self):
        params = dict()
        if self.input_query:
            if hasattr(self.input_query, 'to_alipay_dict'):
                params['input_query'] = self.input_query.to_alipay_dict()
            else:
                params['input_query'] = self.input_query
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityDanielTestQueryModel()
        if 'input_query' in d:
            o.input_query = d['input_query']
        return o


