#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PortfolioDetailProductInfo(object):

    def __init__(self):
        self._asset_category = None
        self._product_abbr_name = None
        self._product_code = None
        self._product_id = None
        self._product_proportion = None
        self._product_type = None

    @property
    def asset_category(self):
        return self._asset_category

    @asset_category.setter
    def asset_category(self, value):
        self._asset_category = value
    @property
    def product_abbr_name(self):
        return self._product_abbr_name

    @product_abbr_name.setter
    def product_abbr_name(self, value):
        self._product_abbr_name = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def product_proportion(self):
        return self._product_proportion

    @product_proportion.setter
    def product_proportion(self, value):
        self._product_proportion = value
    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, value):
        self._product_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_category:
            if hasattr(self.asset_category, 'to_alipay_dict'):
                params['asset_category'] = self.asset_category.to_alipay_dict()
            else:
                params['asset_category'] = self.asset_category
        if self.product_abbr_name:
            if hasattr(self.product_abbr_name, 'to_alipay_dict'):
                params['product_abbr_name'] = self.product_abbr_name.to_alipay_dict()
            else:
                params['product_abbr_name'] = self.product_abbr_name
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.product_proportion:
            if hasattr(self.product_proportion, 'to_alipay_dict'):
                params['product_proportion'] = self.product_proportion.to_alipay_dict()
            else:
                params['product_proportion'] = self.product_proportion
        if self.product_type:
            if hasattr(self.product_type, 'to_alipay_dict'):
                params['product_type'] = self.product_type.to_alipay_dict()
            else:
                params['product_type'] = self.product_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PortfolioDetailProductInfo()
        if 'asset_category' in d:
            o.asset_category = d['asset_category']
        if 'product_abbr_name' in d:
            o.product_abbr_name = d['product_abbr_name']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'product_proportion' in d:
            o.product_proportion = d['product_proportion']
        if 'product_type' in d:
            o.product_type = d['product_type']
        return o


