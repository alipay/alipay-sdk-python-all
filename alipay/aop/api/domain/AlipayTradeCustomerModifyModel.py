#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CorporationInfo import CorporationInfo


class AlipayTradeCustomerModifyModel(object):

    def __init__(self):
        self._corporation_info = None
        self._customer_id = None
        self._description = None
        self._email = None
        self._name = None
        self._phone = None
        self._type = None

    @property
    def corporation_info(self):
        return self._corporation_info

    @corporation_info.setter
    def corporation_info(self, value):
        if isinstance(value, CorporationInfo):
            self._corporation_info = value
        else:
            self._corporation_info = CorporationInfo.from_alipay_dict(value)
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
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
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.corporation_info:
            if hasattr(self.corporation_info, 'to_alipay_dict'):
                params['corporation_info'] = self.corporation_info.to_alipay_dict()
            else:
                params['corporation_info'] = self.corporation_info
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
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
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeCustomerModifyModel()
        if 'corporation_info' in d:
            o.corporation_info = d['corporation_info']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'description' in d:
            o.description = d['description']
        if 'email' in d:
            o.email = d['email']
        if 'name' in d:
            o.name = d['name']
        if 'phone' in d:
            o.phone = d['phone']
        if 'type' in d:
            o.type = d['type']
        return o


