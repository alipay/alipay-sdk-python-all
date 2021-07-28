#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantStoreShopcodeCreateModel(object):

    def __init__(self):
        self._address = None
        self._category_id = None
        self._city_code = None
        self._district_code = None
        self._latitude = None
        self._longitude = None
        self._merchant_logon_id = None
        self._operator_id = None
        self._out_biz_no = None
        self._phone_no = None
        self._province_code = None
        self._shop_front_photo = None
        self._shop_id = None
        self._shop_name = None
        self._shop_no = None
        self._smid = None
        self._tokens = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
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
    def merchant_logon_id(self):
        return self._merchant_logon_id

    @merchant_logon_id.setter
    def merchant_logon_id(self, value):
        self._merchant_logon_id = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def shop_front_photo(self):
        return self._shop_front_photo

    @shop_front_photo.setter
    def shop_front_photo(self, value):
        self._shop_front_photo = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
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
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def tokens(self):
        return self._tokens

    @tokens.setter
    def tokens(self, value):
        if isinstance(value, list):
            self._tokens = list()
            for i in value:
                self._tokens.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
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
        if self.merchant_logon_id:
            if hasattr(self.merchant_logon_id, 'to_alipay_dict'):
                params['merchant_logon_id'] = self.merchant_logon_id.to_alipay_dict()
            else:
                params['merchant_logon_id'] = self.merchant_logon_id
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.phone_no:
            if hasattr(self.phone_no, 'to_alipay_dict'):
                params['phone_no'] = self.phone_no.to_alipay_dict()
            else:
                params['phone_no'] = self.phone_no
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.shop_front_photo:
            if hasattr(self.shop_front_photo, 'to_alipay_dict'):
                params['shop_front_photo'] = self.shop_front_photo.to_alipay_dict()
            else:
                params['shop_front_photo'] = self.shop_front_photo
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
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
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.tokens:
            if isinstance(self.tokens, list):
                for i in range(0, len(self.tokens)):
                    element = self.tokens[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tokens[i] = element.to_alipay_dict()
            if hasattr(self.tokens, 'to_alipay_dict'):
                params['tokens'] = self.tokens.to_alipay_dict()
            else:
                params['tokens'] = self.tokens
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantStoreShopcodeCreateModel()
        if 'address' in d:
            o.address = d['address']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'merchant_logon_id' in d:
            o.merchant_logon_id = d['merchant_logon_id']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'phone_no' in d:
            o.phone_no = d['phone_no']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'shop_front_photo' in d:
            o.shop_front_photo = d['shop_front_photo']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_no' in d:
            o.shop_no = d['shop_no']
        if 'smid' in d:
            o.smid = d['smid']
        if 'tokens' in d:
            o.tokens = d['tokens']
        return o


