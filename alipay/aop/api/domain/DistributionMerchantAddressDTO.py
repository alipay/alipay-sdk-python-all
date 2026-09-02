#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DistributionMerchantAddressDTO(object):

    def __init__(self):
        self._address = None
        self._address_id = None
        self._area = None
        self._city = None
        self._district_code = None
        self._name = None
        self._phone = None
        self._prov = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def address_id(self):
        return self._address_id

    @address_id.setter
    def address_id(self, value):
        self._address_id = value
    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def prov(self):
        return self._prov

    @prov.setter
    def prov(self, value):
        self._prov = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.address_id:
            if hasattr(self.address_id, 'to_alipay_dict'):
                params['address_id'] = self.address_id.to_alipay_dict()
            else:
                params['address_id'] = self.address_id
        if self.area:
            if hasattr(self.area, 'to_alipay_dict'):
                params['area'] = self.area.to_alipay_dict()
            else:
                params['area'] = self.area
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.prov:
            if hasattr(self.prov, 'to_alipay_dict'):
                params['prov'] = self.prov.to_alipay_dict()
            else:
                params['prov'] = self.prov
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DistributionMerchantAddressDTO()
        if 'address' in d:
            o.address = d['address']
        if 'address_id' in d:
            o.address_id = d['address_id']
        if 'area' in d:
            o.area = d['area']
        if 'city' in d:
            o.city = d['city']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'name' in d:
            o.name = d['name']
        if 'phone' in d:
            o.phone = d['phone']
        if 'prov' in d:
            o.prov = d['prov']
        return o


