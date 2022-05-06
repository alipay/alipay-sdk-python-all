#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecipientInfoOrder(object):

    def __init__(self):
        self._detail_address = None
        self._email = None
        self._ip_role_id = None
        self._name = None
        self._telephone = None

    @property
    def detail_address(self):
        return self._detail_address

    @detail_address.setter
    def detail_address(self, value):
        self._detail_address = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, value):
        self._telephone = value


    def to_alipay_dict(self):
        params = dict()
        if self.detail_address:
            if hasattr(self.detail_address, 'to_alipay_dict'):
                params['detail_address'] = self.detail_address.to_alipay_dict()
            else:
                params['detail_address'] = self.detail_address
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.telephone:
            if hasattr(self.telephone, 'to_alipay_dict'):
                params['telephone'] = self.telephone.to_alipay_dict()
            else:
                params['telephone'] = self.telephone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecipientInfoOrder()
        if 'detail_address' in d:
            o.detail_address = d['detail_address']
        if 'email' in d:
            o.email = d['email']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'name' in d:
            o.name = d['name']
        if 'telephone' in d:
            o.telephone = d['telephone']
        return o


