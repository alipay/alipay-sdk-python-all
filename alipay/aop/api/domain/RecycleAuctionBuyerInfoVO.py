#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleAuctionBuyerInfoVO(object):

    def __init__(self):
        self._address = None
        self._buyer_identify = None
        self._buyer_mobile = None
        self._buyer_name = None
        self._city = None
        self._city_code = None
        self._distinct = None
        self._district_code = None
        self._province = None
        self._province_code = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def buyer_identify(self):
        return self._buyer_identify

    @buyer_identify.setter
    def buyer_identify(self, value):
        self._buyer_identify = value
    @property
    def buyer_mobile(self):
        return self._buyer_mobile

    @buyer_mobile.setter
    def buyer_mobile(self, value):
        self._buyer_mobile = value
    @property
    def buyer_name(self):
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, value):
        self._buyer_name = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def distinct(self):
        return self._distinct

    @distinct.setter
    def distinct(self, value):
        self._distinct = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.buyer_identify:
            if hasattr(self.buyer_identify, 'to_alipay_dict'):
                params['buyer_identify'] = self.buyer_identify.to_alipay_dict()
            else:
                params['buyer_identify'] = self.buyer_identify
        if self.buyer_mobile:
            if hasattr(self.buyer_mobile, 'to_alipay_dict'):
                params['buyer_mobile'] = self.buyer_mobile.to_alipay_dict()
            else:
                params['buyer_mobile'] = self.buyer_mobile
        if self.buyer_name:
            if hasattr(self.buyer_name, 'to_alipay_dict'):
                params['buyer_name'] = self.buyer_name.to_alipay_dict()
            else:
                params['buyer_name'] = self.buyer_name
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.distinct:
            if hasattr(self.distinct, 'to_alipay_dict'):
                params['distinct'] = self.distinct.to_alipay_dict()
            else:
                params['distinct'] = self.distinct
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleAuctionBuyerInfoVO()
        if 'address' in d:
            o.address = d['address']
        if 'buyer_identify' in d:
            o.buyer_identify = d['buyer_identify']
        if 'buyer_mobile' in d:
            o.buyer_mobile = d['buyer_mobile']
        if 'buyer_name' in d:
            o.buyer_name = d['buyer_name']
        if 'city' in d:
            o.city = d['city']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'distinct' in d:
            o.distinct = d['distinct']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'province' in d:
            o.province = d['province']
        if 'province_code' in d:
            o.province_code = d['province_code']
        return o


