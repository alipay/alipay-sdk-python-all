#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcBrandShopQueryModel(object):

    def __init__(self):
        self._brand_id_list = None
        self._latitude = None
        self._longitude = None
        self._page_num = None
        self._page_size = None
        self._shop_name = None

    @property
    def brand_id_list(self):
        return self._brand_id_list

    @brand_id_list.setter
    def brand_id_list(self, value):
        if isinstance(value, list):
            self._brand_id_list = list()
            for i in value:
                self._brand_id_list.append(i)
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_id_list:
            if isinstance(self.brand_id_list, list):
                for i in range(0, len(self.brand_id_list)):
                    element = self.brand_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.brand_id_list[i] = element.to_alipay_dict()
            if hasattr(self.brand_id_list, 'to_alipay_dict'):
                params['brand_id_list'] = self.brand_id_list.to_alipay_dict()
            else:
                params['brand_id_list'] = self.brand_id_list
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcBrandShopQueryModel()
        if 'brand_id_list' in d:
            o.brand_id_list = d['brand_id_list']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        return o


