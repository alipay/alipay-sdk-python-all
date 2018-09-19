#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsAddressee(object):

    def __init__(self):
        self._address = None
        self._address_code = None
        self._area = None
        self._city = None
        self._email = None
        self._mobile = None
        self._name = None
        self._phone = None
        self._province = None
        self._zip = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def address_code(self):
        return self._address_code

    @address_code.setter
    def address_code(self, value):
        self._address_code = value
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
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
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
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def zip(self):
        return self._zip

    @zip.setter
    def zip(self, value):
        self._zip = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.address_code:
            if hasattr(self.address_code, 'to_alipay_dict'):
                params['address_code'] = self.address_code.to_alipay_dict()
            else:
                params['address_code'] = self.address_code
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
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
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
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.zip:
            if hasattr(self.zip, 'to_alipay_dict'):
                params['zip'] = self.zip.to_alipay_dict()
            else:
                params['zip'] = self.zip
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsAddressee()
        if 'address' in d:
            o.address = d['address']
        if 'address_code' in d:
            o.address_code = d['address_code']
        if 'area' in d:
            o.area = d['area']
        if 'city' in d:
            o.city = d['city']
        if 'email' in d:
            o.email = d['email']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        if 'phone' in d:
            o.phone = d['phone']
        if 'province' in d:
            o.province = d['province']
        if 'zip' in d:
            o.zip = d['zip']
        return o


