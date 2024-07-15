#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SkuSpec import SkuSpec


class LinkedMallSkuDTO(object):

    def __init__(self):
        self._barcode = None
        self._can_sell = None
        self._division_code = None
        self._fuzzy_quantity = None
        self._mark_price = None
        self._pic_url = None
        self._platform_price = None
        self._price = None
        self._product_id = None
        self._shop_id = None
        self._sku_id = None
        self._sku_specs = None
        self._sku_specs_code = None
        self._sku_status = None
        self._title = None

    @property
    def barcode(self):
        return self._barcode

    @barcode.setter
    def barcode(self, value):
        self._barcode = value
    @property
    def can_sell(self):
        return self._can_sell

    @can_sell.setter
    def can_sell(self, value):
        self._can_sell = value
    @property
    def division_code(self):
        return self._division_code

    @division_code.setter
    def division_code(self, value):
        self._division_code = value
    @property
    def fuzzy_quantity(self):
        return self._fuzzy_quantity

    @fuzzy_quantity.setter
    def fuzzy_quantity(self, value):
        self._fuzzy_quantity = value
    @property
    def mark_price(self):
        return self._mark_price

    @mark_price.setter
    def mark_price(self, value):
        self._mark_price = value
    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        self._pic_url = value
    @property
    def platform_price(self):
        return self._platform_price

    @platform_price.setter
    def platform_price(self, value):
        self._platform_price = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def sku_specs(self):
        return self._sku_specs

    @sku_specs.setter
    def sku_specs(self, value):
        if isinstance(value, list):
            self._sku_specs = list()
            for i in value:
                if isinstance(i, SkuSpec):
                    self._sku_specs.append(i)
                else:
                    self._sku_specs.append(SkuSpec.from_alipay_dict(i))
    @property
    def sku_specs_code(self):
        return self._sku_specs_code

    @sku_specs_code.setter
    def sku_specs_code(self, value):
        self._sku_specs_code = value
    @property
    def sku_status(self):
        return self._sku_status

    @sku_status.setter
    def sku_status(self, value):
        self._sku_status = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.barcode:
            if hasattr(self.barcode, 'to_alipay_dict'):
                params['barcode'] = self.barcode.to_alipay_dict()
            else:
                params['barcode'] = self.barcode
        if self.can_sell:
            if hasattr(self.can_sell, 'to_alipay_dict'):
                params['can_sell'] = self.can_sell.to_alipay_dict()
            else:
                params['can_sell'] = self.can_sell
        if self.division_code:
            if hasattr(self.division_code, 'to_alipay_dict'):
                params['division_code'] = self.division_code.to_alipay_dict()
            else:
                params['division_code'] = self.division_code
        if self.fuzzy_quantity:
            if hasattr(self.fuzzy_quantity, 'to_alipay_dict'):
                params['fuzzy_quantity'] = self.fuzzy_quantity.to_alipay_dict()
            else:
                params['fuzzy_quantity'] = self.fuzzy_quantity
        if self.mark_price:
            if hasattr(self.mark_price, 'to_alipay_dict'):
                params['mark_price'] = self.mark_price.to_alipay_dict()
            else:
                params['mark_price'] = self.mark_price
        if self.pic_url:
            if hasattr(self.pic_url, 'to_alipay_dict'):
                params['pic_url'] = self.pic_url.to_alipay_dict()
            else:
                params['pic_url'] = self.pic_url
        if self.platform_price:
            if hasattr(self.platform_price, 'to_alipay_dict'):
                params['platform_price'] = self.platform_price.to_alipay_dict()
            else:
                params['platform_price'] = self.platform_price
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.sku_specs:
            if isinstance(self.sku_specs, list):
                for i in range(0, len(self.sku_specs)):
                    element = self.sku_specs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_specs[i] = element.to_alipay_dict()
            if hasattr(self.sku_specs, 'to_alipay_dict'):
                params['sku_specs'] = self.sku_specs.to_alipay_dict()
            else:
                params['sku_specs'] = self.sku_specs
        if self.sku_specs_code:
            if hasattr(self.sku_specs_code, 'to_alipay_dict'):
                params['sku_specs_code'] = self.sku_specs_code.to_alipay_dict()
            else:
                params['sku_specs_code'] = self.sku_specs_code
        if self.sku_status:
            if hasattr(self.sku_status, 'to_alipay_dict'):
                params['sku_status'] = self.sku_status.to_alipay_dict()
            else:
                params['sku_status'] = self.sku_status
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LinkedMallSkuDTO()
        if 'barcode' in d:
            o.barcode = d['barcode']
        if 'can_sell' in d:
            o.can_sell = d['can_sell']
        if 'division_code' in d:
            o.division_code = d['division_code']
        if 'fuzzy_quantity' in d:
            o.fuzzy_quantity = d['fuzzy_quantity']
        if 'mark_price' in d:
            o.mark_price = d['mark_price']
        if 'pic_url' in d:
            o.pic_url = d['pic_url']
        if 'platform_price' in d:
            o.platform_price = d['platform_price']
        if 'price' in d:
            o.price = d['price']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'sku_specs' in d:
            o.sku_specs = d['sku_specs']
        if 'sku_specs_code' in d:
            o.sku_specs_code = d['sku_specs_code']
        if 'sku_status' in d:
            o.sku_status = d['sku_status']
        if 'title' in d:
            o.title = d['title']
        return o


