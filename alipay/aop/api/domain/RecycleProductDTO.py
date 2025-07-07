#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleBrand import RecycleBrand


class RecycleProductDTO(object):

    def __init__(self):
        self._product_brand_info = None
        self._product_code = None
        self._product_logo_url = None
        self._product_name = None
        self._stain_pic_url = None

    @property
    def product_brand_info(self):
        return self._product_brand_info

    @product_brand_info.setter
    def product_brand_info(self, value):
        if isinstance(value, RecycleBrand):
            self._product_brand_info = value
        else:
            self._product_brand_info = RecycleBrand.from_alipay_dict(value)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_logo_url(self):
        return self._product_logo_url

    @product_logo_url.setter
    def product_logo_url(self, value):
        self._product_logo_url = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def stain_pic_url(self):
        return self._stain_pic_url

    @stain_pic_url.setter
    def stain_pic_url(self, value):
        self._stain_pic_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.product_brand_info:
            if hasattr(self.product_brand_info, 'to_alipay_dict'):
                params['product_brand_info'] = self.product_brand_info.to_alipay_dict()
            else:
                params['product_brand_info'] = self.product_brand_info
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.product_logo_url:
            if hasattr(self.product_logo_url, 'to_alipay_dict'):
                params['product_logo_url'] = self.product_logo_url.to_alipay_dict()
            else:
                params['product_logo_url'] = self.product_logo_url
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.stain_pic_url:
            if hasattr(self.stain_pic_url, 'to_alipay_dict'):
                params['stain_pic_url'] = self.stain_pic_url.to_alipay_dict()
            else:
                params['stain_pic_url'] = self.stain_pic_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleProductDTO()
        if 'product_brand_info' in d:
            o.product_brand_info = d['product_brand_info']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_logo_url' in d:
            o.product_logo_url = d['product_logo_url']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'stain_pic_url' in d:
            o.stain_pic_url = d['stain_pic_url']
        return o


