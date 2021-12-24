#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserBaseInfo(object):

    def __init__(self):
        self._cert_date_invalid = None
        self._cert_date_valid = None
        self._cert_file_back = None
        self._cert_file_front = None
        self._cert_no = None
        self._cert_type = None
        self._email = None
        self._mobile = None
        self._name = None
        self._phone = None

    @property
    def cert_date_invalid(self):
        return self._cert_date_invalid

    @cert_date_invalid.setter
    def cert_date_invalid(self, value):
        self._cert_date_invalid = value
    @property
    def cert_date_valid(self):
        return self._cert_date_valid

    @cert_date_valid.setter
    def cert_date_valid(self, value):
        self._cert_date_valid = value
    @property
    def cert_file_back(self):
        return self._cert_file_back

    @cert_file_back.setter
    def cert_file_back(self, value):
        self._cert_file_back = value
    @property
    def cert_file_front(self):
        return self._cert_file_front

    @cert_file_front.setter
    def cert_file_front(self, value):
        self._cert_file_front = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.cert_date_invalid:
            if hasattr(self.cert_date_invalid, 'to_alipay_dict'):
                params['cert_date_invalid'] = self.cert_date_invalid.to_alipay_dict()
            else:
                params['cert_date_invalid'] = self.cert_date_invalid
        if self.cert_date_valid:
            if hasattr(self.cert_date_valid, 'to_alipay_dict'):
                params['cert_date_valid'] = self.cert_date_valid.to_alipay_dict()
            else:
                params['cert_date_valid'] = self.cert_date_valid
        if self.cert_file_back:
            if hasattr(self.cert_file_back, 'to_alipay_dict'):
                params['cert_file_back'] = self.cert_file_back.to_alipay_dict()
            else:
                params['cert_file_back'] = self.cert_file_back
        if self.cert_file_front:
            if hasattr(self.cert_file_front, 'to_alipay_dict'):
                params['cert_file_front'] = self.cert_file_front.to_alipay_dict()
            else:
                params['cert_file_front'] = self.cert_file_front
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserBaseInfo()
        if 'cert_date_invalid' in d:
            o.cert_date_invalid = d['cert_date_invalid']
        if 'cert_date_valid' in d:
            o.cert_date_valid = d['cert_date_valid']
        if 'cert_file_back' in d:
            o.cert_file_back = d['cert_file_back']
        if 'cert_file_front' in d:
            o.cert_file_front = d['cert_file_front']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'email' in d:
            o.email = d['email']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        if 'phone' in d:
            o.phone = d['phone']
        return o


