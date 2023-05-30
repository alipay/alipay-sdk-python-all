#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationDcsProxysignSubmitModel(object):

    def __init__(self):
        self._latitude = None
        self._longitude = None
        self._shop_address = None
        self._shop_city_code = None
        self._shop_contact = None
        self._shop_contact_phone = None
        self._shop_district_code = None
        self._shop_name = None
        self._shop_province_code = None

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
    def shop_address(self):
        return self._shop_address

    @shop_address.setter
    def shop_address(self, value):
        self._shop_address = value
    @property
    def shop_city_code(self):
        return self._shop_city_code

    @shop_city_code.setter
    def shop_city_code(self, value):
        self._shop_city_code = value
    @property
    def shop_contact(self):
        return self._shop_contact

    @shop_contact.setter
    def shop_contact(self, value):
        self._shop_contact = value
    @property
    def shop_contact_phone(self):
        return self._shop_contact_phone

    @shop_contact_phone.setter
    def shop_contact_phone(self, value):
        self._shop_contact_phone = value
    @property
    def shop_district_code(self):
        return self._shop_district_code

    @shop_district_code.setter
    def shop_district_code(self, value):
        self._shop_district_code = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_province_code(self):
        return self._shop_province_code

    @shop_province_code.setter
    def shop_province_code(self, value):
        self._shop_province_code = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.shop_address:
            if hasattr(self.shop_address, 'to_alipay_dict'):
                params['shop_address'] = self.shop_address.to_alipay_dict()
            else:
                params['shop_address'] = self.shop_address
        if self.shop_city_code:
            if hasattr(self.shop_city_code, 'to_alipay_dict'):
                params['shop_city_code'] = self.shop_city_code.to_alipay_dict()
            else:
                params['shop_city_code'] = self.shop_city_code
        if self.shop_contact:
            if hasattr(self.shop_contact, 'to_alipay_dict'):
                params['shop_contact'] = self.shop_contact.to_alipay_dict()
            else:
                params['shop_contact'] = self.shop_contact
        if self.shop_contact_phone:
            if hasattr(self.shop_contact_phone, 'to_alipay_dict'):
                params['shop_contact_phone'] = self.shop_contact_phone.to_alipay_dict()
            else:
                params['shop_contact_phone'] = self.shop_contact_phone
        if self.shop_district_code:
            if hasattr(self.shop_district_code, 'to_alipay_dict'):
                params['shop_district_code'] = self.shop_district_code.to_alipay_dict()
            else:
                params['shop_district_code'] = self.shop_district_code
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_province_code:
            if hasattr(self.shop_province_code, 'to_alipay_dict'):
                params['shop_province_code'] = self.shop_province_code.to_alipay_dict()
            else:
                params['shop_province_code'] = self.shop_province_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationDcsProxysignSubmitModel()
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'shop_address' in d:
            o.shop_address = d['shop_address']
        if 'shop_city_code' in d:
            o.shop_city_code = d['shop_city_code']
        if 'shop_contact' in d:
            o.shop_contact = d['shop_contact']
        if 'shop_contact_phone' in d:
            o.shop_contact_phone = d['shop_contact_phone']
        if 'shop_district_code' in d:
            o.shop_district_code = d['shop_district_code']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_province_code' in d:
            o.shop_province_code = d['shop_province_code']
        return o


