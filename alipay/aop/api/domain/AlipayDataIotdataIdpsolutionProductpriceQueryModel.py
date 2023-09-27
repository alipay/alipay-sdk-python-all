#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeviceLocation import DeviceLocation
from alipay.aop.api.domain.ProductSize import ProductSize


class AlipayDataIotdataIdpsolutionProductpriceQueryModel(object):

    def __init__(self):
        self._bar_code = None
        self._brand = None
        self._category_name_1 = None
        self._category_name_2 = None
        self._category_name_3 = None
        self._device_sn = None
        self._goods_name = None
        self._image = None
        self._latitude = None
        self._location = None
        self._longitude = None
        self._shop_id = None
        self._size = None
        self._specification = None

    @property
    def bar_code(self):
        return self._bar_code

    @bar_code.setter
    def bar_code(self, value):
        self._bar_code = value
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
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
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
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if isinstance(value, DeviceLocation):
            self._location = value
        else:
            self._location = DeviceLocation.from_alipay_dict(value)
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.bar_code:
            if hasattr(self.bar_code, 'to_alipay_dict'):
                params['bar_code'] = self.bar_code.to_alipay_dict()
            else:
                params['bar_code'] = self.bar_code
        if self.brand:
            if hasattr(self.brand, 'to_alipay_dict'):
                params['brand'] = self.brand.to_alipay_dict()
            else:
                params['brand'] = self.brand
        if self.category_name_1:
            if hasattr(self.category_name_1, 'to_alipay_dict'):
                params['category_name_1'] = self.category_name_1.to_alipay_dict()
            else:
                params['category_name_1'] = self.category_name_1
        if self.category_name_2:
            if hasattr(self.category_name_2, 'to_alipay_dict'):
                params['category_name_2'] = self.category_name_2.to_alipay_dict()
            else:
                params['category_name_2'] = self.category_name_2
        if self.category_name_3:
            if hasattr(self.category_name_3, 'to_alipay_dict'):
                params['category_name_3'] = self.category_name_3.to_alipay_dict()
            else:
                params['category_name_3'] = self.category_name_3
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.image:
            if hasattr(self.image, 'to_alipay_dict'):
                params['image'] = self.image.to_alipay_dict()
            else:
                params['image'] = self.image
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.location:
            if hasattr(self.location, 'to_alipay_dict'):
                params['location'] = self.location.to_alipay_dict()
            else:
                params['location'] = self.location
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
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
        o = AlipayDataIotdataIdpsolutionProductpriceQueryModel()
        if 'bar_code' in d:
            o.bar_code = d['bar_code']
        if 'brand' in d:
            o.brand = d['brand']
        if 'category_name_1' in d:
            o.category_name_1 = d['category_name_1']
        if 'category_name_2' in d:
            o.category_name_2 = d['category_name_2']
        if 'category_name_3' in d:
            o.category_name_3 = d['category_name_3']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'image' in d:
            o.image = d['image']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'location' in d:
            o.location = d['location']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'size' in d:
            o.size = d['size']
        if 'specification' in d:
            o.specification = d['specification']
        return o


