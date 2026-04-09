#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeProductQueryModel(object):

    def __init__(self):
        self._product_id = None
        self._query_options = None

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
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
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
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
        o = AlipayTradeProductQueryModel()
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'query_options' in d:
            o.query_options = d['query_options']
        return o


