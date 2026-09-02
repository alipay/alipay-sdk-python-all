#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLifeserviceUnifiedshopBatchqueryModel(object):

    def __init__(self):
        self._city_codes = None
        self._district_codes = None
        self._has_business_license = None
        self._page_num = None
        self._page_size = None
        self._province_codes = None
        self._shop_id = None
        self._shop_name = None
        self._shop_type = None
        self._status = None
        self._store_id = None

    @property
    def city_codes(self):
        return self._city_codes

    @city_codes.setter
    def city_codes(self, value):
        if isinstance(value, list):
            self._city_codes = list()
            for i in value:
                self._city_codes.append(i)
    @property
    def district_codes(self):
        return self._district_codes

    @district_codes.setter
    def district_codes(self, value):
        if isinstance(value, list):
            self._district_codes = list()
            for i in value:
                self._district_codes.append(i)
    @property
    def has_business_license(self):
        return self._has_business_license

    @has_business_license.setter
    def has_business_license(self, value):
        self._has_business_license = value
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
    def province_codes(self):
        return self._province_codes

    @province_codes.setter
    def province_codes(self, value):
        if isinstance(value, list):
            self._province_codes = list()
            for i in value:
                self._province_codes.append(i)
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
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, value):
        self._shop_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if isinstance(value, list):
            self._status = list()
            for i in value:
                self._status.append(i)
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_codes:
            if isinstance(self.city_codes, list):
                for i in range(0, len(self.city_codes)):
                    element = self.city_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.city_codes[i] = element.to_alipay_dict()
            if hasattr(self.city_codes, 'to_alipay_dict'):
                params['city_codes'] = self.city_codes.to_alipay_dict()
            else:
                params['city_codes'] = self.city_codes
        if self.district_codes:
            if isinstance(self.district_codes, list):
                for i in range(0, len(self.district_codes)):
                    element = self.district_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.district_codes[i] = element.to_alipay_dict()
            if hasattr(self.district_codes, 'to_alipay_dict'):
                params['district_codes'] = self.district_codes.to_alipay_dict()
            else:
                params['district_codes'] = self.district_codes
        if self.has_business_license:
            if hasattr(self.has_business_license, 'to_alipay_dict'):
                params['has_business_license'] = self.has_business_license.to_alipay_dict()
            else:
                params['has_business_license'] = self.has_business_license
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
        if self.province_codes:
            if isinstance(self.province_codes, list):
                for i in range(0, len(self.province_codes)):
                    element = self.province_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.province_codes[i] = element.to_alipay_dict()
            if hasattr(self.province_codes, 'to_alipay_dict'):
                params['province_codes'] = self.province_codes.to_alipay_dict()
            else:
                params['province_codes'] = self.province_codes
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
        if self.shop_type:
            if hasattr(self.shop_type, 'to_alipay_dict'):
                params['shop_type'] = self.shop_type.to_alipay_dict()
            else:
                params['shop_type'] = self.shop_type
        if self.status:
            if isinstance(self.status, list):
                for i in range(0, len(self.status)):
                    element = self.status[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.status[i] = element.to_alipay_dict()
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = AlipayCommerceLifeserviceUnifiedshopBatchqueryModel()
        if 'city_codes' in d:
            o.city_codes = d['city_codes']
        if 'district_codes' in d:
            o.district_codes = d['district_codes']
        if 'has_business_license' in d:
            o.has_business_license = d['has_business_license']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'province_codes' in d:
            o.province_codes = d['province_codes']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_type' in d:
            o.shop_type = d['shop_type']
        if 'status' in d:
            o.status = d['status']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


