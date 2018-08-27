#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCertifyStudentinfoSyncModel(object):

    def __init__(self):
        self._cert_no = None
        self._education_level = None
        self._entry_date = None
        self._graduation_date = None
        self._name = None
        self._school_name = None
        self._user_id = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def education_level(self):
        return self._education_level

    @education_level.setter
    def education_level(self, value):
        self._education_level = value
    @property
    def entry_date(self):
        return self._entry_date

    @entry_date.setter
    def entry_date(self, value):
        self._entry_date = value
    @property
    def graduation_date(self):
        return self._graduation_date

    @graduation_date.setter
    def graduation_date(self, value):
        self._graduation_date = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def school_name(self):
        return self._school_name

    @school_name.setter
    def school_name(self, value):
        self._school_name = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.education_level:
            if hasattr(self.education_level, 'to_alipay_dict'):
                params['education_level'] = self.education_level.to_alipay_dict()
            else:
                params['education_level'] = self.education_level
        if self.entry_date:
            if hasattr(self.entry_date, 'to_alipay_dict'):
                params['entry_date'] = self.entry_date.to_alipay_dict()
            else:
                params['entry_date'] = self.entry_date
        if self.graduation_date:
            if hasattr(self.graduation_date, 'to_alipay_dict'):
                params['graduation_date'] = self.graduation_date.to_alipay_dict()
            else:
                params['graduation_date'] = self.graduation_date
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.school_name:
            if hasattr(self.school_name, 'to_alipay_dict'):
                params['school_name'] = self.school_name.to_alipay_dict()
            else:
                params['school_name'] = self.school_name
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserCertifyStudentinfoSyncModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'education_level' in d:
            o.education_level = d['education_level']
        if 'entry_date' in d:
            o.entry_date = d['entry_date']
        if 'graduation_date' in d:
            o.graduation_date = d['graduation_date']
        if 'name' in d:
            o.name = d['name']
        if 'school_name' in d:
            o.school_name = d['school_name']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


