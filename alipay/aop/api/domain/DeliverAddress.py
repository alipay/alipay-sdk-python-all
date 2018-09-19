#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeliverAddress(object):

    def __init__(self):
        self._address = None
        self._address_code = None
        self._default_deliver_address = None
        self._deliver_area = None
        self._deliver_city = None
        self._deliver_fullname = None
        self._deliver_mobile = None
        self._deliver_phone = None
        self._deliver_province = None
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
    def default_deliver_address(self):
        return self._default_deliver_address

    @default_deliver_address.setter
    def default_deliver_address(self, value):
        self._default_deliver_address = value
    @property
    def deliver_area(self):
        return self._deliver_area

    @deliver_area.setter
    def deliver_area(self, value):
        self._deliver_area = value
    @property
    def deliver_city(self):
        return self._deliver_city

    @deliver_city.setter
    def deliver_city(self, value):
        self._deliver_city = value
    @property
    def deliver_fullname(self):
        return self._deliver_fullname

    @deliver_fullname.setter
    def deliver_fullname(self, value):
        self._deliver_fullname = value
    @property
    def deliver_mobile(self):
        return self._deliver_mobile

    @deliver_mobile.setter
    def deliver_mobile(self, value):
        self._deliver_mobile = value
    @property
    def deliver_phone(self):
        return self._deliver_phone

    @deliver_phone.setter
    def deliver_phone(self, value):
        self._deliver_phone = value
    @property
    def deliver_province(self):
        return self._deliver_province

    @deliver_province.setter
    def deliver_province(self, value):
        self._deliver_province = value
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
        if self.default_deliver_address:
            if hasattr(self.default_deliver_address, 'to_alipay_dict'):
                params['default_deliver_address'] = self.default_deliver_address.to_alipay_dict()
            else:
                params['default_deliver_address'] = self.default_deliver_address
        if self.deliver_area:
            if hasattr(self.deliver_area, 'to_alipay_dict'):
                params['deliver_area'] = self.deliver_area.to_alipay_dict()
            else:
                params['deliver_area'] = self.deliver_area
        if self.deliver_city:
            if hasattr(self.deliver_city, 'to_alipay_dict'):
                params['deliver_city'] = self.deliver_city.to_alipay_dict()
            else:
                params['deliver_city'] = self.deliver_city
        if self.deliver_fullname:
            if hasattr(self.deliver_fullname, 'to_alipay_dict'):
                params['deliver_fullname'] = self.deliver_fullname.to_alipay_dict()
            else:
                params['deliver_fullname'] = self.deliver_fullname
        if self.deliver_mobile:
            if hasattr(self.deliver_mobile, 'to_alipay_dict'):
                params['deliver_mobile'] = self.deliver_mobile.to_alipay_dict()
            else:
                params['deliver_mobile'] = self.deliver_mobile
        if self.deliver_phone:
            if hasattr(self.deliver_phone, 'to_alipay_dict'):
                params['deliver_phone'] = self.deliver_phone.to_alipay_dict()
            else:
                params['deliver_phone'] = self.deliver_phone
        if self.deliver_province:
            if hasattr(self.deliver_province, 'to_alipay_dict'):
                params['deliver_province'] = self.deliver_province.to_alipay_dict()
            else:
                params['deliver_province'] = self.deliver_province
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
        o = DeliverAddress()
        if 'address' in d:
            o.address = d['address']
        if 'address_code' in d:
            o.address_code = d['address_code']
        if 'default_deliver_address' in d:
            o.default_deliver_address = d['default_deliver_address']
        if 'deliver_area' in d:
            o.deliver_area = d['deliver_area']
        if 'deliver_city' in d:
            o.deliver_city = d['deliver_city']
        if 'deliver_fullname' in d:
            o.deliver_fullname = d['deliver_fullname']
        if 'deliver_mobile' in d:
            o.deliver_mobile = d['deliver_mobile']
        if 'deliver_phone' in d:
            o.deliver_phone = d['deliver_phone']
        if 'deliver_province' in d:
            o.deliver_province = d['deliver_province']
        if 'zip' in d:
            o.zip = d['zip']
        return o


