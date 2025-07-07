#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRecycleBrandQueryModel(object):

    def __init__(self):
        self._page_num = None
        self._page_size = None
        self._product_category_code = None

    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def product_category_code(self):
        return self._product_category_code

    @product_category_code.setter
    def product_category_code(self, value):
        self._product_category_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.product_category_code:
            if hasattr(self.product_category_code, 'to_alipay_dict'):
                params['product_category_code'] = self.product_category_code.to_alipay_dict()
            else:
                params['product_category_code'] = self.product_category_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRecycleBrandQueryModel()
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'product_category_code' in d:
            o.product_category_code = d['product_category_code']
        return o


