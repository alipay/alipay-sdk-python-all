#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudrunEnvShareQueryModel(object):

    def __init__(self):
        self._product_code = None
        self._query_app_id = None

    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def query_app_id(self):
        return self._query_app_id

    @query_app_id.setter
    def query_app_id(self, value):
        self._query_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.query_app_id:
            if hasattr(self.query_app_id, 'to_alipay_dict'):
                params['query_app_id'] = self.query_app_id.to_alipay_dict()
            else:
                params['query_app_id'] = self.query_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudrunEnvShareQueryModel()
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'query_app_id' in d:
            o.query_app_id = d['query_app_id']
        return o


