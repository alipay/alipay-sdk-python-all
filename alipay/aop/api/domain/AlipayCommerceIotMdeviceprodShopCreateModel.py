#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotMdeviceprodShopCreateModel(object):

    def __init__(self):
        self._address = None
        self._city = None
        self._creator_pid = None
        self._district = None
        self._ext_info = None
        self._industry_category = None
        self._merchant_pid = None
        self._province = None
        self._shop_name = None
        self._shop_property = None
        self._shop_type = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def creator_pid(self):
        return self._creator_pid

    @creator_pid.setter
    def creator_pid(self, value):
        self._creator_pid = value
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def industry_category(self):
        return self._industry_category

    @industry_category.setter
    def industry_category(self, value):
        self._industry_category = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_property(self):
        return self._shop_property

    @shop_property.setter
    def shop_property(self, value):
        self._shop_property = value
    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, value):
        self._shop_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.creator_pid:
            if hasattr(self.creator_pid, 'to_alipay_dict'):
                params['creator_pid'] = self.creator_pid.to_alipay_dict()
            else:
                params['creator_pid'] = self.creator_pid
        if self.district:
            if hasattr(self.district, 'to_alipay_dict'):
                params['district'] = self.district.to_alipay_dict()
            else:
                params['district'] = self.district
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.industry_category:
            if hasattr(self.industry_category, 'to_alipay_dict'):
                params['industry_category'] = self.industry_category.to_alipay_dict()
            else:
                params['industry_category'] = self.industry_category
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_property:
            if hasattr(self.shop_property, 'to_alipay_dict'):
                params['shop_property'] = self.shop_property.to_alipay_dict()
            else:
                params['shop_property'] = self.shop_property
        if self.shop_type:
            if hasattr(self.shop_type, 'to_alipay_dict'):
                params['shop_type'] = self.shop_type.to_alipay_dict()
            else:
                params['shop_type'] = self.shop_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotMdeviceprodShopCreateModel()
        if 'address' in d:
            o.address = d['address']
        if 'city' in d:
            o.city = d['city']
        if 'creator_pid' in d:
            o.creator_pid = d['creator_pid']
        if 'district' in d:
            o.district = d['district']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'industry_category' in d:
            o.industry_category = d['industry_category']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'province' in d:
            o.province = d['province']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_property' in d:
            o.shop_property = d['shop_property']
        if 'shop_type' in d:
            o.shop_type = d['shop_type']
        return o


