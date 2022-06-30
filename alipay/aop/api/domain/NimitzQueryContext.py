#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NimitzQueryContext(object):

    def __init__(self):
        self._query_strategy = None
        self._query_token = None

    @property
    def query_strategy(self):
        return self._query_strategy

    @query_strategy.setter
    def query_strategy(self, value):
        self._query_strategy = value
    @property
    def query_token(self):
        return self._query_token

    @query_token.setter
    def query_token(self, value):
        self._query_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.query_strategy:
            if hasattr(self.query_strategy, 'to_alipay_dict'):
                params['query_strategy'] = self.query_strategy.to_alipay_dict()
            else:
                params['query_strategy'] = self.query_strategy
        if self.query_token:
            if hasattr(self.query_token, 'to_alipay_dict'):
                params['query_token'] = self.query_token.to_alipay_dict()
            else:
                params['query_token'] = self.query_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NimitzQueryContext()
        if 'query_strategy' in d:
            o.query_strategy = d['query_strategy']
        if 'query_token' in d:
            o.query_token = d['query_token']
        return o


