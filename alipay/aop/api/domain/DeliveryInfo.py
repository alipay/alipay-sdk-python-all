#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeliveryInfo(object):

    def __init__(self):
        self._city_code = None
        self._consignee = None
        self._contact_phone = None
        self._detail_address = None
        self._district_code = None
        self._province_code = None
        self._zip_code = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def consignee(self):
        return self._consignee

    @consignee.setter
    def consignee(self, value):
        self._consignee = value
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
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value):
        self._zip_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.consignee:
            if hasattr(self.consignee, 'to_alipay_dict'):
                params['consignee'] = self.consignee.to_alipay_dict()
            else:
                params['consignee'] = self.consignee
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
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.zip_code:
            if hasattr(self.zip_code, 'to_alipay_dict'):
                params['zip_code'] = self.zip_code.to_alipay_dict()
            else:
                params['zip_code'] = self.zip_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryInfo()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'consignee' in d:
            o.consignee = d['consignee']
        if 'contact_phone' in d:
            o.contact_phone = d['contact_phone']
        if 'detail_address' in d:
            o.detail_address = d['detail_address']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'zip_code' in d:
            o.zip_code = d['zip_code']
        return o


