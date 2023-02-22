#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TrendQueryRequest import TrendQueryRequest


class AlipayMerchantQipanTrendQueryModel(object):

    def __init__(self):
        self._index_key = None
        self._request_params = None

    @property
    def index_key(self):
        return self._index_key

    @index_key.setter
    def index_key(self, value):
        self._index_key = value
    @property
    def request_params(self):
        return self._request_params

    @request_params.setter
    def request_params(self, value):
        if isinstance(value, TrendQueryRequest):
            self._request_params = value
        else:
            self._request_params = TrendQueryRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.index_key:
            if hasattr(self.index_key, 'to_alipay_dict'):
                params['index_key'] = self.index_key.to_alipay_dict()
            else:
                params['index_key'] = self.index_key
        if self.request_params:
            if hasattr(self.request_params, 'to_alipay_dict'):
                params['request_params'] = self.request_params.to_alipay_dict()
            else:
                params['request_params'] = self.request_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantQipanTrendQueryModel()
        if 'index_key' in d:
            o.index_key = d['index_key']
        if 'request_params' in d:
            o.request_params = d['request_params']
        return o


