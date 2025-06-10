#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleProductInfo(object):

    def __init__(self):
        self._brand_code = None
        self._category_code = None
        self._entity_image_url_list = None
        self._invoice_image_url_list = None
        self._product_code = None
        self._product_name = None
        self._quantity = None
        self._quantity_max = None
        self._quantity_min = None
        self._unit = None
        self._unit_price = None

    @property
    def brand_code(self):
        return self._brand_code

    @brand_code.setter
    def brand_code(self, value):
        self._brand_code = value
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def entity_image_url_list(self):
        return self._entity_image_url_list

    @entity_image_url_list.setter
    def entity_image_url_list(self, value):
        if isinstance(value, list):
            self._entity_image_url_list = list()
            for i in value:
                self._entity_image_url_list.append(i)
    @property
    def invoice_image_url_list(self):
        return self._invoice_image_url_list

    @invoice_image_url_list.setter
    def invoice_image_url_list(self, value):
        if isinstance(value, list):
            self._invoice_image_url_list = list()
            for i in value:
                self._invoice_image_url_list.append(i)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def quantity_max(self):
        return self._quantity_max

    @quantity_max.setter
    def quantity_max(self, value):
        self._quantity_max = value
    @property
    def quantity_min(self):
        return self._quantity_min

    @quantity_min.setter
    def quantity_min(self, value):
        self._quantity_min = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_code:
            if hasattr(self.brand_code, 'to_alipay_dict'):
                params['brand_code'] = self.brand_code.to_alipay_dict()
            else:
                params['brand_code'] = self.brand_code
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.entity_image_url_list:
            if isinstance(self.entity_image_url_list, list):
                for i in range(0, len(self.entity_image_url_list)):
                    element = self.entity_image_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.entity_image_url_list[i] = element.to_alipay_dict()
            if hasattr(self.entity_image_url_list, 'to_alipay_dict'):
                params['entity_image_url_list'] = self.entity_image_url_list.to_alipay_dict()
            else:
                params['entity_image_url_list'] = self.entity_image_url_list
        if self.invoice_image_url_list:
            if isinstance(self.invoice_image_url_list, list):
                for i in range(0, len(self.invoice_image_url_list)):
                    element = self.invoice_image_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_image_url_list[i] = element.to_alipay_dict()
            if hasattr(self.invoice_image_url_list, 'to_alipay_dict'):
                params['invoice_image_url_list'] = self.invoice_image_url_list.to_alipay_dict()
            else:
                params['invoice_image_url_list'] = self.invoice_image_url_list
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.quantity_max:
            if hasattr(self.quantity_max, 'to_alipay_dict'):
                params['quantity_max'] = self.quantity_max.to_alipay_dict()
            else:
                params['quantity_max'] = self.quantity_max
        if self.quantity_min:
            if hasattr(self.quantity_min, 'to_alipay_dict'):
                params['quantity_min'] = self.quantity_min.to_alipay_dict()
            else:
                params['quantity_min'] = self.quantity_min
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        if self.unit_price:
            if hasattr(self.unit_price, 'to_alipay_dict'):
                params['unit_price'] = self.unit_price.to_alipay_dict()
            else:
                params['unit_price'] = self.unit_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleProductInfo()
        if 'brand_code' in d:
            o.brand_code = d['brand_code']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'entity_image_url_list' in d:
            o.entity_image_url_list = d['entity_image_url_list']
        if 'invoice_image_url_list' in d:
            o.invoice_image_url_list = d['invoice_image_url_list']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'quantity_max' in d:
            o.quantity_max = d['quantity_max']
        if 'quantity_min' in d:
            o.quantity_min = d['quantity_min']
        if 'unit' in d:
            o.unit = d['unit']
        if 'unit_price' in d:
            o.unit_price = d['unit_price']
        return o


