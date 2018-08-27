#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoCplifePayResultQueryModel(object):

    def __init__(self):
        self._query_token = None
        self._trade_no = None

    @property
    def query_token(self):
        return self._query_token

    @query_token.setter
    def query_token(self, value):
        self._query_token = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.query_token:
            if hasattr(self.query_token, 'to_alipay_dict'):
                params['query_token'] = self.query_token.to_alipay_dict()
            else:
                params['query_token'] = self.query_token
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoCplifePayResultQueryModel()
        if 'query_token' in d:
            o.query_token = d['query_token']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


