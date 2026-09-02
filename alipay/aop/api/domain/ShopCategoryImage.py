#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopCategoryImage(object):

    def __init__(self):
        self._category_code = None
        self._category_image = None

    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def category_image(self):
        return self._category_image

    @category_image.setter
    def category_image(self, value):
        self._category_image = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.category_image:
            if hasattr(self.category_image, 'to_alipay_dict'):
                params['category_image'] = self.category_image.to_alipay_dict()
            else:
                params['category_image'] = self.category_image
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopCategoryImage()
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'category_image' in d:
            o.category_image = d['category_image']
        return o


