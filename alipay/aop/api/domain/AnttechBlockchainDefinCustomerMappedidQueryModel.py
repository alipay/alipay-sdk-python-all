#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainDefinCustomerMappedidQueryModel(object):

    def __init__(self):
        self._biz_product = None
        self._id_type = None
        self._id_value = None

    @property
    def biz_product(self):
        return self._biz_product

    @biz_product.setter
    def biz_product(self, value):
        self._biz_product = value
    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        self._id_type = value
    @property
    def id_value(self):
        return self._id_value

    @id_value.setter
    def id_value(self, value):
        self._id_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_product:
            if hasattr(self.biz_product, 'to_alipay_dict'):
                params['biz_product'] = self.biz_product.to_alipay_dict()
            else:
                params['biz_product'] = self.biz_product
        if self.id_type:
            if hasattr(self.id_type, 'to_alipay_dict'):
                params['id_type'] = self.id_type.to_alipay_dict()
            else:
                params['id_type'] = self.id_type
        if self.id_value:
            if hasattr(self.id_value, 'to_alipay_dict'):
                params['id_value'] = self.id_value.to_alipay_dict()
            else:
                params['id_value'] = self.id_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinCustomerMappedidQueryModel()
        if 'biz_product' in d:
            o.biz_product = d['biz_product']
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'id_value' in d:
            o.id_value = d['id_value']
        return o


