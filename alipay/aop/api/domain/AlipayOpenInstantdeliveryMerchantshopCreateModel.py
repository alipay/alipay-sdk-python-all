#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenInstantdeliveryMerchantshopCreateModel(object):

    def __init__(self):
        self._contact_name = None
        self._detail_address = None
        self._enterprise_city = None
        self._enterprise_district = None
        self._enterprise_province = None
        self._latitude = None
        self._longitude = None
        self._out_biz_no = None
        self._phone = None
        self._poiid = None
        self._shop_category = None
        self._shop_name = None
        self._shop_no = None

    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def detail_address(self):
        return self._detail_address

    @detail_address.setter
    def detail_address(self, value):
        self._detail_address = value
    @property
    def enterprise_city(self):
        return self._enterprise_city

    @enterprise_city.setter
    def enterprise_city(self, value):
        self._enterprise_city = value
    @property
    def enterprise_district(self):
        return self._enterprise_district

    @enterprise_district.setter
    def enterprise_district(self, value):
        self._enterprise_district = value
    @property
    def enterprise_province(self):
        return self._enterprise_province

    @enterprise_province.setter
    def enterprise_province(self, value):
        self._enterprise_province = value
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
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def poiid(self):
        return self._poiid

    @poiid.setter
    def poiid(self, value):
        self._poiid = value
    @property
    def shop_category(self):
        return self._shop_category

    @shop_category.setter
    def shop_category(self, value):
        self._shop_category = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_no(self):
        return self._shop_no

    @shop_no.setter
    def shop_no(self, value):
        self._shop_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.detail_address:
            if hasattr(self.detail_address, 'to_alipay_dict'):
                params['detail_address'] = self.detail_address.to_alipay_dict()
            else:
                params['detail_address'] = self.detail_address
        if self.enterprise_city:
            if hasattr(self.enterprise_city, 'to_alipay_dict'):
                params['enterprise_city'] = self.enterprise_city.to_alipay_dict()
            else:
                params['enterprise_city'] = self.enterprise_city
        if self.enterprise_district:
            if hasattr(self.enterprise_district, 'to_alipay_dict'):
                params['enterprise_district'] = self.enterprise_district.to_alipay_dict()
            else:
                params['enterprise_district'] = self.enterprise_district
        if self.enterprise_province:
            if hasattr(self.enterprise_province, 'to_alipay_dict'):
                params['enterprise_province'] = self.enterprise_province.to_alipay_dict()
            else:
                params['enterprise_province'] = self.enterprise_province
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
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.poiid:
            if hasattr(self.poiid, 'to_alipay_dict'):
                params['poiid'] = self.poiid.to_alipay_dict()
            else:
                params['poiid'] = self.poiid
        if self.shop_category:
            if hasattr(self.shop_category, 'to_alipay_dict'):
                params['shop_category'] = self.shop_category.to_alipay_dict()
            else:
                params['shop_category'] = self.shop_category
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_no:
            if hasattr(self.shop_no, 'to_alipay_dict'):
                params['shop_no'] = self.shop_no.to_alipay_dict()
            else:
                params['shop_no'] = self.shop_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenInstantdeliveryMerchantshopCreateModel()
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'detail_address' in d:
            o.detail_address = d['detail_address']
        if 'enterprise_city' in d:
            o.enterprise_city = d['enterprise_city']
        if 'enterprise_district' in d:
            o.enterprise_district = d['enterprise_district']
        if 'enterprise_province' in d:
            o.enterprise_province = d['enterprise_province']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'phone' in d:
            o.phone = d['phone']
        if 'poiid' in d:
            o.poiid = d['poiid']
        if 'shop_category' in d:
            o.shop_category = d['shop_category']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_no' in d:
            o.shop_no = d['shop_no']
        return o


