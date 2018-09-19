#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppProdmodeProvcityQueryModel(object):

    def __init__(self):
        self._adcode = None
        self._query_type = None

    @property
    def adcode(self):
        return self._adcode

    @adcode.setter
    def adcode(self, value):
        self._adcode = value
    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.adcode:
            if hasattr(self.adcode, 'to_alipay_dict'):
                params['adcode'] = self.adcode.to_alipay_dict()
            else:
                params['adcode'] = self.adcode
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppProdmodeProvcityQueryModel()
        if 'adcode' in d:
            o.adcode = d['adcode']
        if 'query_type' in d:
            o.query_type = d['query_type']
        return o


