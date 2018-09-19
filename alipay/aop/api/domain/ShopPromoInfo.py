#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromoVoucherInfo import PromoVoucherInfo


class ShopPromoInfo(object):

    def __init__(self):
        self._action_param = None
        self._address = None
        self._brand_name = None
        self._city_id = None
        self._cuisine = None
        self._ext_info = None
        self._has_hui = None
        self._head_shop_name = None
        self._latitude = None
        self._longitude = None
        self._popularity = None
        self._popularity_level = None
        self._price_average = None
        self._root_display_category_info = None
        self._shop_id = None
        self._shop_logo_url = None
        self._shop_name = None
        self._shop_recommend_one_tag_compose = None
        self._voucher_info_list = None

    @property
    def action_param(self):
        return self._action_param

    @action_param.setter
    def action_param(self, value):
        self._action_param = value
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def city_id(self):
        return self._city_id

    @city_id.setter
    def city_id(self, value):
        self._city_id = value
    @property
    def cuisine(self):
        return self._cuisine

    @cuisine.setter
    def cuisine(self, value):
        self._cuisine = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def has_hui(self):
        return self._has_hui

    @has_hui.setter
    def has_hui(self, value):
        self._has_hui = value
    @property
    def head_shop_name(self):
        return self._head_shop_name

    @head_shop_name.setter
    def head_shop_name(self, value):
        self._head_shop_name = value
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
    def popularity(self):
        return self._popularity

    @popularity.setter
    def popularity(self, value):
        self._popularity = value
    @property
    def popularity_level(self):
        return self._popularity_level

    @popularity_level.setter
    def popularity_level(self, value):
        self._popularity_level = value
    @property
    def price_average(self):
        return self._price_average

    @price_average.setter
    def price_average(self, value):
        self._price_average = value
    @property
    def root_display_category_info(self):
        return self._root_display_category_info

    @root_display_category_info.setter
    def root_display_category_info(self, value):
        self._root_display_category_info = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_logo_url(self):
        return self._shop_logo_url

    @shop_logo_url.setter
    def shop_logo_url(self, value):
        self._shop_logo_url = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_recommend_one_tag_compose(self):
        return self._shop_recommend_one_tag_compose

    @shop_recommend_one_tag_compose.setter
    def shop_recommend_one_tag_compose(self, value):
        self._shop_recommend_one_tag_compose = value
    @property
    def voucher_info_list(self):
        return self._voucher_info_list

    @voucher_info_list.setter
    def voucher_info_list(self, value):
        if isinstance(value, list):
            self._voucher_info_list = list()
            for i in value:
                if isinstance(i, PromoVoucherInfo):
                    self._voucher_info_list.append(i)
                else:
                    self._voucher_info_list.append(PromoVoucherInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.action_param:
            if hasattr(self.action_param, 'to_alipay_dict'):
                params['action_param'] = self.action_param.to_alipay_dict()
            else:
                params['action_param'] = self.action_param
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.city_id:
            if hasattr(self.city_id, 'to_alipay_dict'):
                params['city_id'] = self.city_id.to_alipay_dict()
            else:
                params['city_id'] = self.city_id
        if self.cuisine:
            if hasattr(self.cuisine, 'to_alipay_dict'):
                params['cuisine'] = self.cuisine.to_alipay_dict()
            else:
                params['cuisine'] = self.cuisine
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.has_hui:
            if hasattr(self.has_hui, 'to_alipay_dict'):
                params['has_hui'] = self.has_hui.to_alipay_dict()
            else:
                params['has_hui'] = self.has_hui
        if self.head_shop_name:
            if hasattr(self.head_shop_name, 'to_alipay_dict'):
                params['head_shop_name'] = self.head_shop_name.to_alipay_dict()
            else:
                params['head_shop_name'] = self.head_shop_name
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
        if self.popularity:
            if hasattr(self.popularity, 'to_alipay_dict'):
                params['popularity'] = self.popularity.to_alipay_dict()
            else:
                params['popularity'] = self.popularity
        if self.popularity_level:
            if hasattr(self.popularity_level, 'to_alipay_dict'):
                params['popularity_level'] = self.popularity_level.to_alipay_dict()
            else:
                params['popularity_level'] = self.popularity_level
        if self.price_average:
            if hasattr(self.price_average, 'to_alipay_dict'):
                params['price_average'] = self.price_average.to_alipay_dict()
            else:
                params['price_average'] = self.price_average
        if self.root_display_category_info:
            if hasattr(self.root_display_category_info, 'to_alipay_dict'):
                params['root_display_category_info'] = self.root_display_category_info.to_alipay_dict()
            else:
                params['root_display_category_info'] = self.root_display_category_info
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_logo_url:
            if hasattr(self.shop_logo_url, 'to_alipay_dict'):
                params['shop_logo_url'] = self.shop_logo_url.to_alipay_dict()
            else:
                params['shop_logo_url'] = self.shop_logo_url
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_recommend_one_tag_compose:
            if hasattr(self.shop_recommend_one_tag_compose, 'to_alipay_dict'):
                params['shop_recommend_one_tag_compose'] = self.shop_recommend_one_tag_compose.to_alipay_dict()
            else:
                params['shop_recommend_one_tag_compose'] = self.shop_recommend_one_tag_compose
        if self.voucher_info_list:
            if isinstance(self.voucher_info_list, list):
                for i in range(0, len(self.voucher_info_list)):
                    element = self.voucher_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.voucher_info_list[i] = element.to_alipay_dict()
            if hasattr(self.voucher_info_list, 'to_alipay_dict'):
                params['voucher_info_list'] = self.voucher_info_list.to_alipay_dict()
            else:
                params['voucher_info_list'] = self.voucher_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopPromoInfo()
        if 'action_param' in d:
            o.action_param = d['action_param']
        if 'address' in d:
            o.address = d['address']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'city_id' in d:
            o.city_id = d['city_id']
        if 'cuisine' in d:
            o.cuisine = d['cuisine']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'has_hui' in d:
            o.has_hui = d['has_hui']
        if 'head_shop_name' in d:
            o.head_shop_name = d['head_shop_name']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'popularity' in d:
            o.popularity = d['popularity']
        if 'popularity_level' in d:
            o.popularity_level = d['popularity_level']
        if 'price_average' in d:
            o.price_average = d['price_average']
        if 'root_display_category_info' in d:
            o.root_display_category_info = d['root_display_category_info']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_logo_url' in d:
            o.shop_logo_url = d['shop_logo_url']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_recommend_one_tag_compose' in d:
            o.shop_recommend_one_tag_compose = d['shop_recommend_one_tag_compose']
        if 'voucher_info_list' in d:
            o.voucher_info_list = d['voucher_info_list']
        return o


