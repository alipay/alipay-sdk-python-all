#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExaminationPackageItem import ExaminationPackageItem


class ExaminationSpuInfo(object):

    def __init__(self):
        self._combination_product = None
        self._description = None
        self._fulfillment_desc = None
        self._fulfillment_type = None
        self._indicators = None
        self._max_price = None
        self._min_price = None
        self._notice_info = None
        self._package_items = None
        self._price = None
        self._specification = None
        self._spu_id = None
        self._spu_title = None
        self._vendor_code = None

    @property
    def combination_product(self):
        return self._combination_product

    @combination_product.setter
    def combination_product(self, value):
        self._combination_product = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def fulfillment_desc(self):
        return self._fulfillment_desc

    @fulfillment_desc.setter
    def fulfillment_desc(self, value):
        self._fulfillment_desc = value
    @property
    def fulfillment_type(self):
        return self._fulfillment_type

    @fulfillment_type.setter
    def fulfillment_type(self, value):
        self._fulfillment_type = value
    @property
    def indicators(self):
        return self._indicators

    @indicators.setter
    def indicators(self, value):
        self._indicators = value
    @property
    def max_price(self):
        return self._max_price

    @max_price.setter
    def max_price(self, value):
        self._max_price = value
    @property
    def min_price(self):
        return self._min_price

    @min_price.setter
    def min_price(self, value):
        self._min_price = value
    @property
    def notice_info(self):
        return self._notice_info

    @notice_info.setter
    def notice_info(self, value):
        self._notice_info = value
    @property
    def package_items(self):
        return self._package_items

    @package_items.setter
    def package_items(self, value):
        if isinstance(value, list):
            self._package_items = list()
            for i in value:
                if isinstance(i, ExaminationPackageItem):
                    self._package_items.append(i)
                else:
                    self._package_items.append(ExaminationPackageItem.from_alipay_dict(i))
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def specification(self):
        return self._specification

    @specification.setter
    def specification(self, value):
        self._specification = value
    @property
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, value):
        self._spu_id = value
    @property
    def spu_title(self):
        return self._spu_title

    @spu_title.setter
    def spu_title(self, value):
        self._spu_title = value
    @property
    def vendor_code(self):
        return self._vendor_code

    @vendor_code.setter
    def vendor_code(self, value):
        self._vendor_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.combination_product:
            if hasattr(self.combination_product, 'to_alipay_dict'):
                params['combination_product'] = self.combination_product.to_alipay_dict()
            else:
                params['combination_product'] = self.combination_product
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.fulfillment_desc:
            if hasattr(self.fulfillment_desc, 'to_alipay_dict'):
                params['fulfillment_desc'] = self.fulfillment_desc.to_alipay_dict()
            else:
                params['fulfillment_desc'] = self.fulfillment_desc
        if self.fulfillment_type:
            if hasattr(self.fulfillment_type, 'to_alipay_dict'):
                params['fulfillment_type'] = self.fulfillment_type.to_alipay_dict()
            else:
                params['fulfillment_type'] = self.fulfillment_type
        if self.indicators:
            if hasattr(self.indicators, 'to_alipay_dict'):
                params['indicators'] = self.indicators.to_alipay_dict()
            else:
                params['indicators'] = self.indicators
        if self.max_price:
            if hasattr(self.max_price, 'to_alipay_dict'):
                params['max_price'] = self.max_price.to_alipay_dict()
            else:
                params['max_price'] = self.max_price
        if self.min_price:
            if hasattr(self.min_price, 'to_alipay_dict'):
                params['min_price'] = self.min_price.to_alipay_dict()
            else:
                params['min_price'] = self.min_price
        if self.notice_info:
            if hasattr(self.notice_info, 'to_alipay_dict'):
                params['notice_info'] = self.notice_info.to_alipay_dict()
            else:
                params['notice_info'] = self.notice_info
        if self.package_items:
            if isinstance(self.package_items, list):
                for i in range(0, len(self.package_items)):
                    element = self.package_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.package_items[i] = element.to_alipay_dict()
            if hasattr(self.package_items, 'to_alipay_dict'):
                params['package_items'] = self.package_items.to_alipay_dict()
            else:
                params['package_items'] = self.package_items
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.specification:
            if hasattr(self.specification, 'to_alipay_dict'):
                params['specification'] = self.specification.to_alipay_dict()
            else:
                params['specification'] = self.specification
        if self.spu_id:
            if hasattr(self.spu_id, 'to_alipay_dict'):
                params['spu_id'] = self.spu_id.to_alipay_dict()
            else:
                params['spu_id'] = self.spu_id
        if self.spu_title:
            if hasattr(self.spu_title, 'to_alipay_dict'):
                params['spu_title'] = self.spu_title.to_alipay_dict()
            else:
                params['spu_title'] = self.spu_title
        if self.vendor_code:
            if hasattr(self.vendor_code, 'to_alipay_dict'):
                params['vendor_code'] = self.vendor_code.to_alipay_dict()
            else:
                params['vendor_code'] = self.vendor_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExaminationSpuInfo()
        if 'combination_product' in d:
            o.combination_product = d['combination_product']
        if 'description' in d:
            o.description = d['description']
        if 'fulfillment_desc' in d:
            o.fulfillment_desc = d['fulfillment_desc']
        if 'fulfillment_type' in d:
            o.fulfillment_type = d['fulfillment_type']
        if 'indicators' in d:
            o.indicators = d['indicators']
        if 'max_price' in d:
            o.max_price = d['max_price']
        if 'min_price' in d:
            o.min_price = d['min_price']
        if 'notice_info' in d:
            o.notice_info = d['notice_info']
        if 'package_items' in d:
            o.package_items = d['package_items']
        if 'price' in d:
            o.price = d['price']
        if 'specification' in d:
            o.specification = d['specification']
        if 'spu_id' in d:
            o.spu_id = d['spu_id']
        if 'spu_title' in d:
            o.spu_title = d['spu_title']
        if 'vendor_code' in d:
            o.vendor_code = d['vendor_code']
        return o


