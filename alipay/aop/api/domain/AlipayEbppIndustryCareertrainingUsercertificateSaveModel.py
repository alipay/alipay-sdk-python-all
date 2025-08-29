#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryCareertrainingUsercertificateSaveModel(object):

    def __init__(self):
        self._certificate_code = None
        self._certificate_name = None
        self._certification_time = None
        self._open_id = None
        self._rating_org = None
        self._user_certificate_code = None
        self._user_certificate_level = None
        self._user_id = None

    @property
    def certificate_code(self):
        return self._certificate_code

    @certificate_code.setter
    def certificate_code(self, value):
        self._certificate_code = value
    @property
    def certificate_name(self):
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, value):
        self._certificate_name = value
    @property
    def certification_time(self):
        return self._certification_time

    @certification_time.setter
    def certification_time(self, value):
        self._certification_time = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def rating_org(self):
        return self._rating_org

    @rating_org.setter
    def rating_org(self, value):
        self._rating_org = value
    @property
    def user_certificate_code(self):
        return self._user_certificate_code

    @user_certificate_code.setter
    def user_certificate_code(self, value):
        self._user_certificate_code = value
    @property
    def user_certificate_level(self):
        return self._user_certificate_level

    @user_certificate_level.setter
    def user_certificate_level(self, value):
        self._user_certificate_level = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_code:
            if hasattr(self.certificate_code, 'to_alipay_dict'):
                params['certificate_code'] = self.certificate_code.to_alipay_dict()
            else:
                params['certificate_code'] = self.certificate_code
        if self.certificate_name:
            if hasattr(self.certificate_name, 'to_alipay_dict'):
                params['certificate_name'] = self.certificate_name.to_alipay_dict()
            else:
                params['certificate_name'] = self.certificate_name
        if self.certification_time:
            if hasattr(self.certification_time, 'to_alipay_dict'):
                params['certification_time'] = self.certification_time.to_alipay_dict()
            else:
                params['certification_time'] = self.certification_time
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.rating_org:
            if hasattr(self.rating_org, 'to_alipay_dict'):
                params['rating_org'] = self.rating_org.to_alipay_dict()
            else:
                params['rating_org'] = self.rating_org
        if self.user_certificate_code:
            if hasattr(self.user_certificate_code, 'to_alipay_dict'):
                params['user_certificate_code'] = self.user_certificate_code.to_alipay_dict()
            else:
                params['user_certificate_code'] = self.user_certificate_code
        if self.user_certificate_level:
            if hasattr(self.user_certificate_level, 'to_alipay_dict'):
                params['user_certificate_level'] = self.user_certificate_level.to_alipay_dict()
            else:
                params['user_certificate_level'] = self.user_certificate_level
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
        o = AlipayEbppIndustryCareertrainingUsercertificateSaveModel()
        if 'certificate_code' in d:
            o.certificate_code = d['certificate_code']
        if 'certificate_name' in d:
            o.certificate_name = d['certificate_name']
        if 'certification_time' in d:
            o.certification_time = d['certification_time']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'rating_org' in d:
            o.rating_org = d['rating_org']
        if 'user_certificate_code' in d:
            o.user_certificate_code = d['user_certificate_code']
        if 'user_certificate_level' in d:
            o.user_certificate_level = d['user_certificate_level']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


