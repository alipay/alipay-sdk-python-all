#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReliableEnterpriseProfilesDTO(object):

    def __init__(self):
        self._access_channel = None
        self._activity_level = None
        self._auth_type = None
        self._biz_license_no = None
        self._biz_license_url = None
        self._count_employee = None
        self._legal_person_cert_no = None
        self._platform_gmt_create = None
        self._tax_no = None

    @property
    def access_channel(self):
        return self._access_channel

    @access_channel.setter
    def access_channel(self, value):
        self._access_channel = value
    @property
    def activity_level(self):
        return self._activity_level

    @activity_level.setter
    def activity_level(self, value):
        self._activity_level = value
    @property
    def auth_type(self):
        return self._auth_type

    @auth_type.setter
    def auth_type(self, value):
        self._auth_type = value
    @property
    def biz_license_no(self):
        return self._biz_license_no

    @biz_license_no.setter
    def biz_license_no(self, value):
        self._biz_license_no = value
    @property
    def biz_license_url(self):
        return self._biz_license_url

    @biz_license_url.setter
    def biz_license_url(self, value):
        self._biz_license_url = value
    @property
    def count_employee(self):
        return self._count_employee

    @count_employee.setter
    def count_employee(self, value):
        self._count_employee = value
    @property
    def legal_person_cert_no(self):
        return self._legal_person_cert_no

    @legal_person_cert_no.setter
    def legal_person_cert_no(self, value):
        self._legal_person_cert_no = value
    @property
    def platform_gmt_create(self):
        return self._platform_gmt_create

    @platform_gmt_create.setter
    def platform_gmt_create(self, value):
        self._platform_gmt_create = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_channel:
            if hasattr(self.access_channel, 'to_alipay_dict'):
                params['access_channel'] = self.access_channel.to_alipay_dict()
            else:
                params['access_channel'] = self.access_channel
        if self.activity_level:
            if hasattr(self.activity_level, 'to_alipay_dict'):
                params['activity_level'] = self.activity_level.to_alipay_dict()
            else:
                params['activity_level'] = self.activity_level
        if self.auth_type:
            if hasattr(self.auth_type, 'to_alipay_dict'):
                params['auth_type'] = self.auth_type.to_alipay_dict()
            else:
                params['auth_type'] = self.auth_type
        if self.biz_license_no:
            if hasattr(self.biz_license_no, 'to_alipay_dict'):
                params['biz_license_no'] = self.biz_license_no.to_alipay_dict()
            else:
                params['biz_license_no'] = self.biz_license_no
        if self.biz_license_url:
            if hasattr(self.biz_license_url, 'to_alipay_dict'):
                params['biz_license_url'] = self.biz_license_url.to_alipay_dict()
            else:
                params['biz_license_url'] = self.biz_license_url
        if self.count_employee:
            if hasattr(self.count_employee, 'to_alipay_dict'):
                params['count_employee'] = self.count_employee.to_alipay_dict()
            else:
                params['count_employee'] = self.count_employee
        if self.legal_person_cert_no:
            if hasattr(self.legal_person_cert_no, 'to_alipay_dict'):
                params['legal_person_cert_no'] = self.legal_person_cert_no.to_alipay_dict()
            else:
                params['legal_person_cert_no'] = self.legal_person_cert_no
        if self.platform_gmt_create:
            if hasattr(self.platform_gmt_create, 'to_alipay_dict'):
                params['platform_gmt_create'] = self.platform_gmt_create.to_alipay_dict()
            else:
                params['platform_gmt_create'] = self.platform_gmt_create
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReliableEnterpriseProfilesDTO()
        if 'access_channel' in d:
            o.access_channel = d['access_channel']
        if 'activity_level' in d:
            o.activity_level = d['activity_level']
        if 'auth_type' in d:
            o.auth_type = d['auth_type']
        if 'biz_license_no' in d:
            o.biz_license_no = d['biz_license_no']
        if 'biz_license_url' in d:
            o.biz_license_url = d['biz_license_url']
        if 'count_employee' in d:
            o.count_employee = d['count_employee']
        if 'legal_person_cert_no' in d:
            o.legal_person_cert_no = d['legal_person_cert_no']
        if 'platform_gmt_create' in d:
            o.platform_gmt_create = d['platform_gmt_create']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        return o


