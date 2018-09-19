#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPeLawsuitDetailQueryModel(object):

    def __init__(self):
        self._lawsuit_id = None
        self._lawsuit_type = None
        self._product_code = None
        self._transaction_id = None

    @property
    def lawsuit_id(self):
        return self._lawsuit_id

    @lawsuit_id.setter
    def lawsuit_id(self, value):
        self._lawsuit_id = value
    @property
    def lawsuit_type(self):
        return self._lawsuit_type

    @lawsuit_type.setter
    def lawsuit_type(self, value):
        self._lawsuit_type = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.lawsuit_id:
            if hasattr(self.lawsuit_id, 'to_alipay_dict'):
                params['lawsuit_id'] = self.lawsuit_id.to_alipay_dict()
            else:
                params['lawsuit_id'] = self.lawsuit_id
        if self.lawsuit_type:
            if hasattr(self.lawsuit_type, 'to_alipay_dict'):
                params['lawsuit_type'] = self.lawsuit_type.to_alipay_dict()
            else:
                params['lawsuit_type'] = self.lawsuit_type
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.transaction_id:
            if hasattr(self.transaction_id, 'to_alipay_dict'):
                params['transaction_id'] = self.transaction_id.to_alipay_dict()
            else:
                params['transaction_id'] = self.transaction_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPeLawsuitDetailQueryModel()
        if 'lawsuit_id' in d:
            o.lawsuit_id = d['lawsuit_id']
        if 'lawsuit_type' in d:
            o.lawsuit_type = d['lawsuit_type']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'transaction_id' in d:
            o.transaction_id = d['transaction_id']
        return o


