#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalFractalRagsearchQueryModel(object):

    def __init__(self):
        self._access_key = None
        self._extra_params = None
        self._max_results = None
        self._query = None

    @property
    def access_key(self):
        return self._access_key

    @access_key.setter
    def access_key(self, value):
        self._access_key = value
    @property
    def extra_params(self):
        return self._extra_params

    @extra_params.setter
    def extra_params(self, value):
        self._extra_params = value
    @property
    def max_results(self):
        return self._max_results

    @max_results.setter
    def max_results(self, value):
        self._max_results = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_key:
            if hasattr(self.access_key, 'to_alipay_dict'):
                params['access_key'] = self.access_key.to_alipay_dict()
            else:
                params['access_key'] = self.access_key
        if self.extra_params:
            if hasattr(self.extra_params, 'to_alipay_dict'):
                params['extra_params'] = self.extra_params.to_alipay_dict()
            else:
                params['extra_params'] = self.extra_params
        if self.max_results:
            if hasattr(self.max_results, 'to_alipay_dict'):
                params['max_results'] = self.max_results.to_alipay_dict()
            else:
                params['max_results'] = self.max_results
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalFractalRagsearchQueryModel()
        if 'access_key' in d:
            o.access_key = d['access_key']
        if 'extra_params' in d:
            o.extra_params = d['extra_params']
        if 'max_results' in d:
            o.max_results = d['max_results']
        if 'query' in d:
            o.query = d['query']
        return o


