#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeProductModifyModel(object):

    def __init__(self):
        self._default_price_id = None
        self._description = None
        self._metadata = None
        self._name = None
        self._product_id = None

    @property
    def default_price_id(self):
        return self._default_price_id

    @default_price_id.setter
    def default_price_id(self, value):
        self._default_price_id = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, value):
        self._metadata = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.default_price_id:
            if hasattr(self.default_price_id, 'to_alipay_dict'):
                params['default_price_id'] = self.default_price_id.to_alipay_dict()
            else:
                params['default_price_id'] = self.default_price_id
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.metadata:
            if hasattr(self.metadata, 'to_alipay_dict'):
                params['metadata'] = self.metadata.to_alipay_dict()
            else:
                params['metadata'] = self.metadata
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeProductModifyModel()
        if 'default_price_id' in d:
            o.default_price_id = d['default_price_id']
        if 'description' in d:
            o.description = d['description']
        if 'metadata' in d:
            o.metadata = d['metadata']
        if 'name' in d:
            o.name = d['name']
        if 'product_id' in d:
            o.product_id = d['product_id']
        return o


