#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleAssessProductVO(object):

    def __init__(self):
        self._assess_amount = None
        self._assess_min_amount = None
        self._assess_min_quality = None
        self._assess_quality = None
        self._assess_type = None
        self._out_sku_id = None
        self._out_sku_name = None
        self._product_category = None
        self._product_code = None
        self._product_logo = None
        self._product_name = None
        self._unit_type = None

    @property
    def assess_amount(self):
        return self._assess_amount

    @assess_amount.setter
    def assess_amount(self, value):
        self._assess_amount = value
    @property
    def assess_min_amount(self):
        return self._assess_min_amount

    @assess_min_amount.setter
    def assess_min_amount(self, value):
        self._assess_min_amount = value
    @property
    def assess_min_quality(self):
        return self._assess_min_quality

    @assess_min_quality.setter
    def assess_min_quality(self, value):
        self._assess_min_quality = value
    @property
    def assess_quality(self):
        return self._assess_quality

    @assess_quality.setter
    def assess_quality(self, value):
        self._assess_quality = value
    @property
    def assess_type(self):
        return self._assess_type

    @assess_type.setter
    def assess_type(self, value):
        self._assess_type = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def out_sku_name(self):
        return self._out_sku_name

    @out_sku_name.setter
    def out_sku_name(self, value):
        self._out_sku_name = value
    @property
    def product_category(self):
        return self._product_category

    @product_category.setter
    def product_category(self, value):
        self._product_category = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_logo(self):
        return self._product_logo

    @product_logo.setter
    def product_logo(self, value):
        self._product_logo = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def unit_type(self):
        return self._unit_type

    @unit_type.setter
    def unit_type(self, value):
        self._unit_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.assess_amount:
            if hasattr(self.assess_amount, 'to_alipay_dict'):
                params['assess_amount'] = self.assess_amount.to_alipay_dict()
            else:
                params['assess_amount'] = self.assess_amount
        if self.assess_min_amount:
            if hasattr(self.assess_min_amount, 'to_alipay_dict'):
                params['assess_min_amount'] = self.assess_min_amount.to_alipay_dict()
            else:
                params['assess_min_amount'] = self.assess_min_amount
        if self.assess_min_quality:
            if hasattr(self.assess_min_quality, 'to_alipay_dict'):
                params['assess_min_quality'] = self.assess_min_quality.to_alipay_dict()
            else:
                params['assess_min_quality'] = self.assess_min_quality
        if self.assess_quality:
            if hasattr(self.assess_quality, 'to_alipay_dict'):
                params['assess_quality'] = self.assess_quality.to_alipay_dict()
            else:
                params['assess_quality'] = self.assess_quality
        if self.assess_type:
            if hasattr(self.assess_type, 'to_alipay_dict'):
                params['assess_type'] = self.assess_type.to_alipay_dict()
            else:
                params['assess_type'] = self.assess_type
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.out_sku_name:
            if hasattr(self.out_sku_name, 'to_alipay_dict'):
                params['out_sku_name'] = self.out_sku_name.to_alipay_dict()
            else:
                params['out_sku_name'] = self.out_sku_name
        if self.product_category:
            if hasattr(self.product_category, 'to_alipay_dict'):
                params['product_category'] = self.product_category.to_alipay_dict()
            else:
                params['product_category'] = self.product_category
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.product_logo:
            if hasattr(self.product_logo, 'to_alipay_dict'):
                params['product_logo'] = self.product_logo.to_alipay_dict()
            else:
                params['product_logo'] = self.product_logo
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.unit_type:
            if hasattr(self.unit_type, 'to_alipay_dict'):
                params['unit_type'] = self.unit_type.to_alipay_dict()
            else:
                params['unit_type'] = self.unit_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleAssessProductVO()
        if 'assess_amount' in d:
            o.assess_amount = d['assess_amount']
        if 'assess_min_amount' in d:
            o.assess_min_amount = d['assess_min_amount']
        if 'assess_min_quality' in d:
            o.assess_min_quality = d['assess_min_quality']
        if 'assess_quality' in d:
            o.assess_quality = d['assess_quality']
        if 'assess_type' in d:
            o.assess_type = d['assess_type']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'out_sku_name' in d:
            o.out_sku_name = d['out_sku_name']
        if 'product_category' in d:
            o.product_category = d['product_category']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_logo' in d:
            o.product_logo = d['product_logo']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'unit_type' in d:
            o.unit_type = d['unit_type']
        return o


