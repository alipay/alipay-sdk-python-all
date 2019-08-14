#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiSalesLeadsShopleadsCreateModel(object):

    def __init__(self):
        self._address = None
        self._branch_name = None
        self._brand_id = None
        self._category_id = None
        self._city_id = None
        self._company_name = None
        self._contacts_name = None
        self._contacts_no = None
        self._country_id = None
        self._district_id = None
        self._ext_info = None
        self._head_shop_name = None
        self._latitude = None
        self._longitude = None
        self._memo = None
        self._province_id = None
        self._register_date = None
        self._request_id = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def branch_name(self):
        return self._branch_name

    @branch_name.setter
    def branch_name(self, value):
        self._branch_name = value
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def city_id(self):
        return self._city_id

    @city_id.setter
    def city_id(self, value):
        self._city_id = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def contacts_name(self):
        return self._contacts_name

    @contacts_name.setter
    def contacts_name(self, value):
        self._contacts_name = value
    @property
    def contacts_no(self):
        return self._contacts_no

    @contacts_no.setter
    def contacts_no(self, value):
        self._contacts_no = value
    @property
    def country_id(self):
        return self._country_id

    @country_id.setter
    def country_id(self, value):
        self._country_id = value
    @property
    def district_id(self):
        return self._district_id

    @district_id.setter
    def district_id(self, value):
        self._district_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
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
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def province_id(self):
        return self._province_id

    @province_id.setter
    def province_id(self, value):
        self._province_id = value
    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, value):
        self._register_date = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.branch_name:
            if hasattr(self.branch_name, 'to_alipay_dict'):
                params['branch_name'] = self.branch_name.to_alipay_dict()
            else:
                params['branch_name'] = self.branch_name
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.city_id:
            if hasattr(self.city_id, 'to_alipay_dict'):
                params['city_id'] = self.city_id.to_alipay_dict()
            else:
                params['city_id'] = self.city_id
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.contacts_name:
            if hasattr(self.contacts_name, 'to_alipay_dict'):
                params['contacts_name'] = self.contacts_name.to_alipay_dict()
            else:
                params['contacts_name'] = self.contacts_name
        if self.contacts_no:
            if hasattr(self.contacts_no, 'to_alipay_dict'):
                params['contacts_no'] = self.contacts_no.to_alipay_dict()
            else:
                params['contacts_no'] = self.contacts_no
        if self.country_id:
            if hasattr(self.country_id, 'to_alipay_dict'):
                params['country_id'] = self.country_id.to_alipay_dict()
            else:
                params['country_id'] = self.country_id
        if self.district_id:
            if hasattr(self.district_id, 'to_alipay_dict'):
                params['district_id'] = self.district_id.to_alipay_dict()
            else:
                params['district_id'] = self.district_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
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
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.province_id:
            if hasattr(self.province_id, 'to_alipay_dict'):
                params['province_id'] = self.province_id.to_alipay_dict()
            else:
                params['province_id'] = self.province_id
        if self.register_date:
            if hasattr(self.register_date, 'to_alipay_dict'):
                params['register_date'] = self.register_date.to_alipay_dict()
            else:
                params['register_date'] = self.register_date
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiSalesLeadsShopleadsCreateModel()
        if 'address' in d:
            o.address = d['address']
        if 'branch_name' in d:
            o.branch_name = d['branch_name']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'city_id' in d:
            o.city_id = d['city_id']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'contacts_name' in d:
            o.contacts_name = d['contacts_name']
        if 'contacts_no' in d:
            o.contacts_no = d['contacts_no']
        if 'country_id' in d:
            o.country_id = d['country_id']
        if 'district_id' in d:
            o.district_id = d['district_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'head_shop_name' in d:
            o.head_shop_name = d['head_shop_name']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'memo' in d:
            o.memo = d['memo']
        if 'province_id' in d:
            o.province_id = d['province_id']
        if 'register_date' in d:
            o.register_date = d['register_date']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


