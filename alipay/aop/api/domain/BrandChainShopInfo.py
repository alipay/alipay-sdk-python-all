#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InteOpShopBusinessTime import InteOpShopBusinessTime


class BrandChainShopInfo(object):

    def __init__(self):
        self._business_time = None
        self._city_code = None
        self._contact_mobile = None
        self._contact_phone = None
        self._detail_address = None
        self._district_code = None
        self._out_door_images = None
        self._province_code = None
        self._shop_brand_id = None
        self._shop_name = None
        self._store_id = None

    @property
    def business_time(self):
        return self._business_time

    @business_time.setter
    def business_time(self, value):
        if isinstance(value, list):
            self._business_time = list()
            for i in value:
                if isinstance(i, InteOpShopBusinessTime):
                    self._business_time.append(i)
                else:
                    self._business_time.append(InteOpShopBusinessTime.from_alipay_dict(i))
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def contact_mobile(self):
        return self._contact_mobile

    @contact_mobile.setter
    def contact_mobile(self, value):
        self._contact_mobile = value
    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, value):
        self._contact_phone = value
    @property
    def detail_address(self):
        return self._detail_address

    @detail_address.setter
    def detail_address(self, value):
        self._detail_address = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def out_door_images(self):
        return self._out_door_images

    @out_door_images.setter
    def out_door_images(self, value):
        self._out_door_images = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def shop_brand_id(self):
        return self._shop_brand_id

    @shop_brand_id.setter
    def shop_brand_id(self, value):
        self._shop_brand_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_time:
            if isinstance(self.business_time, list):
                for i in range(0, len(self.business_time)):
                    element = self.business_time[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_time[i] = element.to_alipay_dict()
            if hasattr(self.business_time, 'to_alipay_dict'):
                params['business_time'] = self.business_time.to_alipay_dict()
            else:
                params['business_time'] = self.business_time
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.contact_mobile:
            if hasattr(self.contact_mobile, 'to_alipay_dict'):
                params['contact_mobile'] = self.contact_mobile.to_alipay_dict()
            else:
                params['contact_mobile'] = self.contact_mobile
        if self.contact_phone:
            if hasattr(self.contact_phone, 'to_alipay_dict'):
                params['contact_phone'] = self.contact_phone.to_alipay_dict()
            else:
                params['contact_phone'] = self.contact_phone
        if self.detail_address:
            if hasattr(self.detail_address, 'to_alipay_dict'):
                params['detail_address'] = self.detail_address.to_alipay_dict()
            else:
                params['detail_address'] = self.detail_address
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.out_door_images:
            if hasattr(self.out_door_images, 'to_alipay_dict'):
                params['out_door_images'] = self.out_door_images.to_alipay_dict()
            else:
                params['out_door_images'] = self.out_door_images
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.shop_brand_id:
            if hasattr(self.shop_brand_id, 'to_alipay_dict'):
                params['shop_brand_id'] = self.shop_brand_id.to_alipay_dict()
            else:
                params['shop_brand_id'] = self.shop_brand_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BrandChainShopInfo()
        if 'business_time' in d:
            o.business_time = d['business_time']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'contact_mobile' in d:
            o.contact_mobile = d['contact_mobile']
        if 'contact_phone' in d:
            o.contact_phone = d['contact_phone']
        if 'detail_address' in d:
            o.detail_address = d['detail_address']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'out_door_images' in d:
            o.out_door_images = d['out_door_images']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'shop_brand_id' in d:
            o.shop_brand_id = d['shop_brand_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


