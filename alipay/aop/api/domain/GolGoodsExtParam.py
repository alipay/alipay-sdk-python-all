#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GolGoodsExtParam(object):

    def __init__(self):
        self._brand_name = None
        self._description = None
        self._discount_content = None
        self._is_tax_free = None
        self._specifications = None
        self._stock_status = None
        self._tax_rate = None

    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def discount_content(self):
        return self._discount_content

    @discount_content.setter
    def discount_content(self, value):
        self._discount_content = value
    @property
    def is_tax_free(self):
        return self._is_tax_free

    @is_tax_free.setter
    def is_tax_free(self, value):
        self._is_tax_free = value
    @property
    def specifications(self):
        return self._specifications

    @specifications.setter
    def specifications(self, value):
        if isinstance(value, list):
            self._specifications = list()
            for i in value:
                self._specifications.append(i)
    @property
    def stock_status(self):
        return self._stock_status

    @stock_status.setter
    def stock_status(self, value):
        self._stock_status = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.discount_content:
            if hasattr(self.discount_content, 'to_alipay_dict'):
                params['discount_content'] = self.discount_content.to_alipay_dict()
            else:
                params['discount_content'] = self.discount_content
        if self.is_tax_free:
            if hasattr(self.is_tax_free, 'to_alipay_dict'):
                params['is_tax_free'] = self.is_tax_free.to_alipay_dict()
            else:
                params['is_tax_free'] = self.is_tax_free
        if self.specifications:
            if isinstance(self.specifications, list):
                for i in range(0, len(self.specifications)):
                    element = self.specifications[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.specifications[i] = element.to_alipay_dict()
            if hasattr(self.specifications, 'to_alipay_dict'):
                params['specifications'] = self.specifications.to_alipay_dict()
            else:
                params['specifications'] = self.specifications
        if self.stock_status:
            if hasattr(self.stock_status, 'to_alipay_dict'):
                params['stock_status'] = self.stock_status.to_alipay_dict()
            else:
                params['stock_status'] = self.stock_status
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GolGoodsExtParam()
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'description' in d:
            o.description = d['description']
        if 'discount_content' in d:
            o.discount_content = d['discount_content']
        if 'is_tax_free' in d:
            o.is_tax_free = d['is_tax_free']
        if 'specifications' in d:
            o.specifications = d['specifications']
        if 'stock_status' in d:
            o.stock_status = d['stock_status']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        return o


