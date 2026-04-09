#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradePriceQueryModel(object):

    def __init__(self):
        self._price_id = None
        self._query_options = None

    @property
    def price_id(self):
        return self._price_id

    @price_id.setter
    def price_id(self, value):
        self._price_id = value
    @property
    def query_options(self):
        return self._query_options

    @query_options.setter
    def query_options(self, value):
        if isinstance(value, list):
            self._query_options = list()
            for i in value:
                self._query_options.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.price_id:
            if hasattr(self.price_id, 'to_alipay_dict'):
                params['price_id'] = self.price_id.to_alipay_dict()
            else:
                params['price_id'] = self.price_id
        if self.query_options:
            if isinstance(self.query_options, list):
                for i in range(0, len(self.query_options)):
                    element = self.query_options[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.query_options[i] = element.to_alipay_dict()
            if hasattr(self.query_options, 'to_alipay_dict'):
                params['query_options'] = self.query_options.to_alipay_dict()
            else:
                params['query_options'] = self.query_options
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradePriceQueryModel()
        if 'price_id' in d:
            o.price_id = d['price_id']
        if 'query_options' in d:
            o.query_options = d['query_options']
        return o


