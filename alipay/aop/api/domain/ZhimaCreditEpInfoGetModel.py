#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpInfoGetModel(object):

    def __init__(self):
        self._data_type = None
        self._data_value = None
        self._product_code = None
        self._transaction_id = None

    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def data_value(self):
        return self._data_value

    @data_value.setter
    def data_value(self, value):
        self._data_value = value
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
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.data_value:
            if hasattr(self.data_value, 'to_alipay_dict'):
                params['data_value'] = self.data_value.to_alipay_dict()
            else:
                params['data_value'] = self.data_value
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
        o = ZhimaCreditEpInfoGetModel()
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'data_value' in d:
            o.data_value = d['data_value']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'transaction_id' in d:
            o.transaction_id = d['transaction_id']
        return o


