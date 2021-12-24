#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NewsAggregationValue(object):

    def __init__(self):
        self._doc_count = None
        self._key = None

    @property
    def doc_count(self):
        return self._doc_count

    @doc_count.setter
    def doc_count(self, value):
        self._doc_count = value
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value


    def to_alipay_dict(self):
        params = dict()
        if self.doc_count:
            if hasattr(self.doc_count, 'to_alipay_dict'):
                params['doc_count'] = self.doc_count.to_alipay_dict()
            else:
                params['doc_count'] = self.doc_count
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NewsAggregationValue()
        if 'doc_count' in d:
            o.doc_count = d['doc_count']
        if 'key' in d:
            o.key = d['key']
        return o


