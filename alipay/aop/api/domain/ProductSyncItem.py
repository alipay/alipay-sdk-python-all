#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProductSyncItem(object):

    def __init__(self):
        self._barcode = None
        self._marketing_voice_text = None
        self._merchant_product_code = None
        self._original_price = None
        self._product_image_file_id = None
        self._product_name = None
        self._promotion_price = None
        self._specification = None

    @property
    def barcode(self):
        return self._barcode

    @barcode.setter
    def barcode(self, value):
        self._barcode = value
    @property
    def marketing_voice_text(self):
        return self._marketing_voice_text

    @marketing_voice_text.setter
    def marketing_voice_text(self, value):
        self._marketing_voice_text = value
    @property
    def merchant_product_code(self):
        return self._merchant_product_code

    @merchant_product_code.setter
    def merchant_product_code(self, value):
        self._merchant_product_code = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def product_image_file_id(self):
        return self._product_image_file_id

    @product_image_file_id.setter
    def product_image_file_id(self, value):
        self._product_image_file_id = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def promotion_price(self):
        return self._promotion_price

    @promotion_price.setter
    def promotion_price(self, value):
        self._promotion_price = value
    @property
    def specification(self):
        return self._specification

    @specification.setter
    def specification(self, value):
        self._specification = value


    def to_alipay_dict(self):
        params = dict()
        if self.barcode:
            if hasattr(self.barcode, 'to_alipay_dict'):
                params['barcode'] = self.barcode.to_alipay_dict()
            else:
                params['barcode'] = self.barcode
        if self.marketing_voice_text:
            if hasattr(self.marketing_voice_text, 'to_alipay_dict'):
                params['marketing_voice_text'] = self.marketing_voice_text.to_alipay_dict()
            else:
                params['marketing_voice_text'] = self.marketing_voice_text
        if self.merchant_product_code:
            if hasattr(self.merchant_product_code, 'to_alipay_dict'):
                params['merchant_product_code'] = self.merchant_product_code.to_alipay_dict()
            else:
                params['merchant_product_code'] = self.merchant_product_code
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.product_image_file_id:
            if hasattr(self.product_image_file_id, 'to_alipay_dict'):
                params['product_image_file_id'] = self.product_image_file_id.to_alipay_dict()
            else:
                params['product_image_file_id'] = self.product_image_file_id
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.promotion_price:
            if hasattr(self.promotion_price, 'to_alipay_dict'):
                params['promotion_price'] = self.promotion_price.to_alipay_dict()
            else:
                params['promotion_price'] = self.promotion_price
        if self.specification:
            if hasattr(self.specification, 'to_alipay_dict'):
                params['specification'] = self.specification.to_alipay_dict()
            else:
                params['specification'] = self.specification
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductSyncItem()
        if 'barcode' in d:
            o.barcode = d['barcode']
        if 'marketing_voice_text' in d:
            o.marketing_voice_text = d['marketing_voice_text']
        if 'merchant_product_code' in d:
            o.merchant_product_code = d['merchant_product_code']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'product_image_file_id' in d:
            o.product_image_file_id = d['product_image_file_id']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'promotion_price' in d:
            o.promotion_price = d['promotion_price']
        if 'specification' in d:
            o.specification = d['specification']
        return o


