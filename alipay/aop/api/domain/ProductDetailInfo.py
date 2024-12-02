#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProductDetailInfo(object):

    def __init__(self):
        self._category_lv_1_code = None
        self._category_lv_1_name = None
        self._category_lv_2_code = None
        self._category_lv_2_name = None
        self._category_lv_3_code = None
        self._category_lv_3_name = None
        self._platform_id = None
        self._product_title = None

    @property
    def category_lv_1_code(self):
        return self._category_lv_1_code

    @category_lv_1_code.setter
    def category_lv_1_code(self, value):
        self._category_lv_1_code = value
    @property
    def category_lv_1_name(self):
        return self._category_lv_1_name

    @category_lv_1_name.setter
    def category_lv_1_name(self, value):
        self._category_lv_1_name = value
    @property
    def category_lv_2_code(self):
        return self._category_lv_2_code

    @category_lv_2_code.setter
    def category_lv_2_code(self, value):
        self._category_lv_2_code = value
    @property
    def category_lv_2_name(self):
        return self._category_lv_2_name

    @category_lv_2_name.setter
    def category_lv_2_name(self, value):
        self._category_lv_2_name = value
    @property
    def category_lv_3_code(self):
        return self._category_lv_3_code

    @category_lv_3_code.setter
    def category_lv_3_code(self, value):
        self._category_lv_3_code = value
    @property
    def category_lv_3_name(self):
        return self._category_lv_3_name

    @category_lv_3_name.setter
    def category_lv_3_name(self, value):
        self._category_lv_3_name = value
    @property
    def platform_id(self):
        return self._platform_id

    @platform_id.setter
    def platform_id(self, value):
        self._platform_id = value
    @property
    def product_title(self):
        return self._product_title

    @product_title.setter
    def product_title(self, value):
        self._product_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_lv_1_code:
            if hasattr(self.category_lv_1_code, 'to_alipay_dict'):
                params['category_lv_1_code'] = self.category_lv_1_code.to_alipay_dict()
            else:
                params['category_lv_1_code'] = self.category_lv_1_code
        if self.category_lv_1_name:
            if hasattr(self.category_lv_1_name, 'to_alipay_dict'):
                params['category_lv_1_name'] = self.category_lv_1_name.to_alipay_dict()
            else:
                params['category_lv_1_name'] = self.category_lv_1_name
        if self.category_lv_2_code:
            if hasattr(self.category_lv_2_code, 'to_alipay_dict'):
                params['category_lv_2_code'] = self.category_lv_2_code.to_alipay_dict()
            else:
                params['category_lv_2_code'] = self.category_lv_2_code
        if self.category_lv_2_name:
            if hasattr(self.category_lv_2_name, 'to_alipay_dict'):
                params['category_lv_2_name'] = self.category_lv_2_name.to_alipay_dict()
            else:
                params['category_lv_2_name'] = self.category_lv_2_name
        if self.category_lv_3_code:
            if hasattr(self.category_lv_3_code, 'to_alipay_dict'):
                params['category_lv_3_code'] = self.category_lv_3_code.to_alipay_dict()
            else:
                params['category_lv_3_code'] = self.category_lv_3_code
        if self.category_lv_3_name:
            if hasattr(self.category_lv_3_name, 'to_alipay_dict'):
                params['category_lv_3_name'] = self.category_lv_3_name.to_alipay_dict()
            else:
                params['category_lv_3_name'] = self.category_lv_3_name
        if self.platform_id:
            if hasattr(self.platform_id, 'to_alipay_dict'):
                params['platform_id'] = self.platform_id.to_alipay_dict()
            else:
                params['platform_id'] = self.platform_id
        if self.product_title:
            if hasattr(self.product_title, 'to_alipay_dict'):
                params['product_title'] = self.product_title.to_alipay_dict()
            else:
                params['product_title'] = self.product_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductDetailInfo()
        if 'category_lv_1_code' in d:
            o.category_lv_1_code = d['category_lv_1_code']
        if 'category_lv_1_name' in d:
            o.category_lv_1_name = d['category_lv_1_name']
        if 'category_lv_2_code' in d:
            o.category_lv_2_code = d['category_lv_2_code']
        if 'category_lv_2_name' in d:
            o.category_lv_2_name = d['category_lv_2_name']
        if 'category_lv_3_code' in d:
            o.category_lv_3_code = d['category_lv_3_code']
        if 'category_lv_3_name' in d:
            o.category_lv_3_name = d['category_lv_3_name']
        if 'platform_id' in d:
            o.platform_id = d['platform_id']
        if 'product_title' in d:
            o.product_title = d['product_title']
        return o


