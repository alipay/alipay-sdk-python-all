#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndustryQueryOption(object):

    def __init__(self):
        self._include_oil_product = None

    @property
    def include_oil_product(self):
        return self._include_oil_product

    @include_oil_product.setter
    def include_oil_product(self, value):
        self._include_oil_product = value


    def to_alipay_dict(self):
        params = dict()
        if self.include_oil_product:
            if hasattr(self.include_oil_product, 'to_alipay_dict'):
                params['include_oil_product'] = self.include_oil_product.to_alipay_dict()
            else:
                params['include_oil_product'] = self.include_oil_product
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndustryQueryOption()
        if 'include_oil_product' in d:
            o.include_oil_product = d['include_oil_product']
        return o


