#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ProductVOOptions import ProductVOOptions


class AntProdpaasProductCommonQueryModel(object):

    def __init__(self):
        self._product_code = None
        self._product_options = None
        self._product_version = None

    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_options(self):
        return self._product_options

    @product_options.setter
    def product_options(self, value):
        if isinstance(value, ProductVOOptions):
            self._product_options = value
        else:
            self._product_options = ProductVOOptions.from_alipay_dict(value)
    @property
    def product_version(self):
        return self._product_version

    @product_version.setter
    def product_version(self, value):
        self._product_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.product_options:
            if hasattr(self.product_options, 'to_alipay_dict'):
                params['product_options'] = self.product_options.to_alipay_dict()
            else:
                params['product_options'] = self.product_options
        if self.product_version:
            if hasattr(self.product_version, 'to_alipay_dict'):
                params['product_version'] = self.product_version.to_alipay_dict()
            else:
                params['product_version'] = self.product_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntProdpaasProductCommonQueryModel()
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_options' in d:
            o.product_options = d['product_options']
        if 'product_version' in d:
            o.product_version = d['product_version']
        return o


