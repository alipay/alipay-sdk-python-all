#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAntarchiveFaceQueryModel(object):

    def __init__(self):
        self._birthday = None
        self._cert_expire_date = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._gender = None

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value
    @property
    def cert_expire_date(self):
        return self._cert_expire_date

    @cert_expire_date.setter
    def cert_expire_date(self, value):
        self._cert_expire_date = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
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
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value


    def to_alipay_dict(self):
        params = dict()
        if self.birthday:
            if hasattr(self.birthday, 'to_alipay_dict'):
                params['birthday'] = self.birthday.to_alipay_dict()
            else:
                params['birthday'] = self.birthday
        if self.cert_expire_date:
            if hasattr(self.cert_expire_date, 'to_alipay_dict'):
                params['cert_expire_date'] = self.cert_expire_date.to_alipay_dict()
            else:
                params['cert_expire_date'] = self.cert_expire_date
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
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
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAntarchiveFaceQueryModel()
        if 'birthday' in d:
            o.birthday = d['birthday']
        if 'cert_expire_date' in d:
            o.cert_expire_date = d['cert_expire_date']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'gender' in d:
            o.gender = d['gender']
        return o


