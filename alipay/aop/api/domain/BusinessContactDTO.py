#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessAddressDTO import BusinessAddressDTO


class BusinessContactDTO(object):

    def __init__(self):
        self._contact_address = None
        self._contact_email = None
        self._contact_mobile = None
        self._contact_name = None
        self._contact_phone = None
        self._contact_position = None
        self._contact_type = None

    @property
    def contact_address(self):
        return self._contact_address

    @contact_address.setter
    def contact_address(self, value):
        if isinstance(value, BusinessAddressDTO):
            self._contact_address = value
        else:
            self._contact_address = BusinessAddressDTO.from_alipay_dict(value)
    @property
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, value):
        self._contact_email = value
    @property
    def contact_mobile(self):
        return self._contact_mobile

    @contact_mobile.setter
    def contact_mobile(self, value):
        self._contact_mobile = value
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
    def contact_position(self):
        return self._contact_position

    @contact_position.setter
    def contact_position(self, value):
        self._contact_position = value
    @property
    def contact_type(self):
        return self._contact_type

    @contact_type.setter
    def contact_type(self, value):
        self._contact_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_address:
            if hasattr(self.contact_address, 'to_alipay_dict'):
                params['contact_address'] = self.contact_address.to_alipay_dict()
            else:
                params['contact_address'] = self.contact_address
        if self.contact_email:
            if hasattr(self.contact_email, 'to_alipay_dict'):
                params['contact_email'] = self.contact_email.to_alipay_dict()
            else:
                params['contact_email'] = self.contact_email
        if self.contact_mobile:
            if hasattr(self.contact_mobile, 'to_alipay_dict'):
                params['contact_mobile'] = self.contact_mobile.to_alipay_dict()
            else:
                params['contact_mobile'] = self.contact_mobile
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
        if self.contact_position:
            if hasattr(self.contact_position, 'to_alipay_dict'):
                params['contact_position'] = self.contact_position.to_alipay_dict()
            else:
                params['contact_position'] = self.contact_position
        if self.contact_type:
            if hasattr(self.contact_type, 'to_alipay_dict'):
                params['contact_type'] = self.contact_type.to_alipay_dict()
            else:
                params['contact_type'] = self.contact_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessContactDTO()
        if 'contact_address' in d:
            o.contact_address = d['contact_address']
        if 'contact_email' in d:
            o.contact_email = d['contact_email']
        if 'contact_mobile' in d:
            o.contact_mobile = d['contact_mobile']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'contact_phone' in d:
            o.contact_phone = d['contact_phone']
        if 'contact_position' in d:
            o.contact_position = d['contact_position']
        if 'contact_type' in d:
            o.contact_type = d['contact_type']
        return o


