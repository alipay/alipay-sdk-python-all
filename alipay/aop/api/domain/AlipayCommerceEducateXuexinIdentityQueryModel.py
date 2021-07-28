#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateXuexinIdentityQueryModel(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._education_level = None
        self._enroll_date = None
        self._school_name = None
        self._user_name = None

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
    def education_level(self):
        return self._education_level

    @education_level.setter
    def education_level(self, value):
        self._education_level = value
    @property
    def enroll_date(self):
        return self._enroll_date

    @enroll_date.setter
    def enroll_date(self, value):
        self._enroll_date = value
    @property
    def school_name(self):
        return self._school_name

    @school_name.setter
    def school_name(self, value):
        self._school_name = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.education_level:
            if hasattr(self.education_level, 'to_alipay_dict'):
                params['education_level'] = self.education_level.to_alipay_dict()
            else:
                params['education_level'] = self.education_level
        if self.enroll_date:
            if hasattr(self.enroll_date, 'to_alipay_dict'):
                params['enroll_date'] = self.enroll_date.to_alipay_dict()
            else:
                params['enroll_date'] = self.enroll_date
        if self.school_name:
            if hasattr(self.school_name, 'to_alipay_dict'):
                params['school_name'] = self.school_name.to_alipay_dict()
            else:
                params['school_name'] = self.school_name
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateXuexinIdentityQueryModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'education_level' in d:
            o.education_level = d['education_level']
        if 'enroll_date' in d:
            o.enroll_date = d['enroll_date']
        if 'school_name' in d:
            o.school_name = d['school_name']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


