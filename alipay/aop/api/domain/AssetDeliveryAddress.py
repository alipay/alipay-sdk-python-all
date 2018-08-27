#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetDeliveryAddress(object):

    def __init__(self):
        self._address = None
        self._city = None
        self._contact_name = None
        self._contact_phone = None
        self._district = None
        self._province = None
        self._warehouse_id = None
        self._warehouse_name = None
        self._zip_code = None

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
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, value):
        self._contact_phone = value
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def warehouse_id(self):
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, value):
        self._warehouse_id = value
    @property
    def warehouse_name(self):
        return self._warehouse_name

    @warehouse_name.setter
    def warehouse_name(self, value):
        self._warehouse_name = value
    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value):
        self._zip_code = value


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
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.contact_phone:
            if hasattr(self.contact_phone, 'to_alipay_dict'):
                params['contact_phone'] = self.contact_phone.to_alipay_dict()
            else:
                params['contact_phone'] = self.contact_phone
        if self.district:
            if hasattr(self.district, 'to_alipay_dict'):
                params['district'] = self.district.to_alipay_dict()
            else:
                params['district'] = self.district
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.warehouse_id:
            if hasattr(self.warehouse_id, 'to_alipay_dict'):
                params['warehouse_id'] = self.warehouse_id.to_alipay_dict()
            else:
                params['warehouse_id'] = self.warehouse_id
        if self.warehouse_name:
            if hasattr(self.warehouse_name, 'to_alipay_dict'):
                params['warehouse_name'] = self.warehouse_name.to_alipay_dict()
            else:
                params['warehouse_name'] = self.warehouse_name
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
        o = AssetDeliveryAddress()
        if 'address' in d:
            o.address = d['address']
        if 'city' in d:
            o.city = d['city']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'contact_phone' in d:
            o.contact_phone = d['contact_phone']
        if 'district' in d:
            o.district = d['district']
        if 'province' in d:
            o.province = d['province']
        if 'warehouse_id' in d:
            o.warehouse_id = d['warehouse_id']
        if 'warehouse_name' in d:
            o.warehouse_name = d['warehouse_name']
        if 'zip_code' in d:
            o.zip_code = d['zip_code']
        return o


