#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCertifyIdentifyinfoInfoQueryModel(object):

    def __init__(self):
        self._query_type = None
        self._query_value = None

    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value
    @property
    def query_value(self):
        return self._query_value

    @query_value.setter
    def query_value(self, value):
        self._query_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        if self.query_value:
            if hasattr(self.query_value, 'to_alipay_dict'):
                params['query_value'] = self.query_value.to_alipay_dict()
            else:
                params['query_value'] = self.query_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserCertifyIdentifyinfoInfoQueryModel()
        if 'query_type' in d:
            o.query_type = d['query_type']
        if 'query_value' in d:
            o.query_value = d['query_value']
        return o


