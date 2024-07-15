#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserInfoDetailDTO(object):

    def __init__(self):
        self._account_name = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self._passport_id = None
        self._phone_number = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
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
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
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
        if self.last_name:
            if hasattr(self.last_name, 'to_alipay_dict'):
                params['last_name'] = self.last_name.to_alipay_dict()
            else:
                params['last_name'] = self.last_name
        if self.passport_id:
            if hasattr(self.passport_id, 'to_alipay_dict'):
                params['passport_id'] = self.passport_id.to_alipay_dict()
            else:
                params['passport_id'] = self.passport_id
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
        o = UserInfoDetailDTO()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'email' in d:
            o.email = d['email']
        if 'first_name' in d:
            o.first_name = d['first_name']
        if 'last_name' in d:
            o.last_name = d['last_name']
        if 'passport_id' in d:
            o.passport_id = d['passport_id']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        return o


