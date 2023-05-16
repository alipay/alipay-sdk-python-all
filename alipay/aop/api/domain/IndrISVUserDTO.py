#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndrISVAddressDTO import IndrISVAddressDTO


class IndrISVUserDTO(object):

    def __init__(self):
        self._address = None
        self._email = None
        self._first_name = None
        self._full_name = None
        self._identity_card_number = None
        self._identity_type = None
        self._last_name = None
        self._native_full_name = None
        self._phone_area_code = None
        self._phone_country = None
        self._phone_number = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if isinstance(value, IndrISVAddressDTO):
            self._address = value
        else:
            self._address = IndrISVAddressDTO.from_alipay_dict(value)
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value
    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value
    @property
    def identity_card_number(self):
        return self._identity_card_number

    @identity_card_number.setter
    def identity_card_number(self, value):
        self._identity_card_number = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value
    @property
    def native_full_name(self):
        return self._native_full_name

    @native_full_name.setter
    def native_full_name(self, value):
        self._native_full_name = value
    @property
    def phone_area_code(self):
        return self._phone_area_code

    @phone_area_code.setter
    def phone_area_code(self, value):
        self._phone_area_code = value
    @property
    def phone_country(self):
        return self._phone_country

    @phone_country.setter
    def phone_country(self, value):
        self._phone_country = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.first_name:
            if hasattr(self.first_name, 'to_alipay_dict'):
                params['first_name'] = self.first_name.to_alipay_dict()
            else:
                params['first_name'] = self.first_name
        if self.full_name:
            if hasattr(self.full_name, 'to_alipay_dict'):
                params['full_name'] = self.full_name.to_alipay_dict()
            else:
                params['full_name'] = self.full_name
        if self.identity_card_number:
            if hasattr(self.identity_card_number, 'to_alipay_dict'):
                params['identity_card_number'] = self.identity_card_number.to_alipay_dict()
            else:
                params['identity_card_number'] = self.identity_card_number
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.last_name:
            if hasattr(self.last_name, 'to_alipay_dict'):
                params['last_name'] = self.last_name.to_alipay_dict()
            else:
                params['last_name'] = self.last_name
        if self.native_full_name:
            if hasattr(self.native_full_name, 'to_alipay_dict'):
                params['native_full_name'] = self.native_full_name.to_alipay_dict()
            else:
                params['native_full_name'] = self.native_full_name
        if self.phone_area_code:
            if hasattr(self.phone_area_code, 'to_alipay_dict'):
                params['phone_area_code'] = self.phone_area_code.to_alipay_dict()
            else:
                params['phone_area_code'] = self.phone_area_code
        if self.phone_country:
            if hasattr(self.phone_country, 'to_alipay_dict'):
                params['phone_country'] = self.phone_country.to_alipay_dict()
            else:
                params['phone_country'] = self.phone_country
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndrISVUserDTO()
        if 'address' in d:
            o.address = d['address']
        if 'email' in d:
            o.email = d['email']
        if 'first_name' in d:
            o.first_name = d['first_name']
        if 'full_name' in d:
            o.full_name = d['full_name']
        if 'identity_card_number' in d:
            o.identity_card_number = d['identity_card_number']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'last_name' in d:
            o.last_name = d['last_name']
        if 'native_full_name' in d:
            o.native_full_name = d['native_full_name']
        if 'phone_area_code' in d:
            o.phone_area_code = d['phone_area_code']
        if 'phone_country' in d:
            o.phone_country = d['phone_country']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        return o


