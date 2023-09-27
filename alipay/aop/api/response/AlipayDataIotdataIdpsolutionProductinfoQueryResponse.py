#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ProductSize import ProductSize


class AlipayDataIotdataIdpsolutionProductinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataIotdataIdpsolutionProductinfoQueryResponse, self).__init__()
        self._brand = None
        self._category_name_1 = None
        self._category_name_2 = None
        self._category_name_3 = None
        self._goods_name = None
        self._image = None
        self._size = None
        self._specification = None

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value
    @property
    def category_name_1(self):
        return self._category_name_1

    @category_name_1.setter
    def category_name_1(self, value):
        self._category_name_1 = value
    @property
    def category_name_2(self):
        return self._category_name_2

    @category_name_2.setter
    def category_name_2(self, value):
        self._category_name_2 = value
    @property
    def category_name_3(self):
        return self._category_name_3

    @category_name_3.setter
    def category_name_3(self, value):
        self._category_name_3 = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, ProductSize):
            self._size = value
        else:
            self._size = ProductSize.from_alipay_dict(value)
    @property
    def specification(self):
        return self._specification

    @specification.setter
    def specification(self, value):
        self._specification = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataIotdataIdpsolutionProductinfoQueryResponse, self).parse_response_content(response_content)
        if 'brand' in response:
            self.brand = response['brand']
        if 'category_name_1' in response:
            self.category_name_1 = response['category_name_1']
        if 'category_name_2' in response:
            self.category_name_2 = response['category_name_2']
        if 'category_name_3' in response:
            self.category_name_3 = response['category_name_3']
        if 'goods_name' in response:
            self.goods_name = response['goods_name']
        if 'image' in response:
            self.image = response['image']
        if 'size' in response:
            self.size = response['size']
        if 'specification' in response:
            self.specification = response['specification']
