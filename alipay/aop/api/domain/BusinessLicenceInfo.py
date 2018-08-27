#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessLicenceInfo(object):

    def __init__(self):
        self._business_license_auth_pic = None
        self._business_license_city = None
        self._business_license_indate = None
        self._business_license_is_three_in_one = None
        self._business_license_no = None
        self._business_license_pic = None
        self._business_license_province = None
        self._business_scope = None
        self._company_address = None
        self._company_name = None
        self._org_code_certificate_no = None
        self._org_code_certificate_pic = None

    @property
    def business_license_auth_pic(self):
        return self._business_license_auth_pic

    @business_license_auth_pic.setter
    def business_license_auth_pic(self, value):
        self._business_license_auth_pic = value
    @property
    def business_license_city(self):
        return self._business_license_city

    @business_license_city.setter
    def business_license_city(self, value):
        self._business_license_city = value
    @property
    def business_license_indate(self):
        return self._business_license_indate

    @business_license_indate.setter
    def business_license_indate(self, value):
        self._business_license_indate = value
    @property
    def business_license_is_three_in_one(self):
        return self._business_license_is_three_in_one

    @business_license_is_three_in_one.setter
    def business_license_is_three_in_one(self, value):
        self._business_license_is_three_in_one = value
    @property
    def business_license_no(self):
        return self._business_license_no

    @business_license_no.setter
    def business_license_no(self, value):
        self._business_license_no = value
    @property
    def business_license_pic(self):
        return self._business_license_pic

    @business_license_pic.setter
    def business_license_pic(self, value):
        self._business_license_pic = value
    @property
    def business_license_province(self):
        return self._business_license_province

    @business_license_province.setter
    def business_license_province(self, value):
        self._business_license_province = value
    @property
    def business_scope(self):
        return self._business_scope

    @business_scope.setter
    def business_scope(self, value):
        self._business_scope = value
    @property
    def company_address(self):
        return self._company_address

    @company_address.setter
    def company_address(self, value):
        self._company_address = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def org_code_certificate_no(self):
        return self._org_code_certificate_no

    @org_code_certificate_no.setter
    def org_code_certificate_no(self, value):
        self._org_code_certificate_no = value
    @property
    def org_code_certificate_pic(self):
        return self._org_code_certificate_pic

    @org_code_certificate_pic.setter
    def org_code_certificate_pic(self, value):
        self._org_code_certificate_pic = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_license_auth_pic:
            if hasattr(self.business_license_auth_pic, 'to_alipay_dict'):
                params['business_license_auth_pic'] = self.business_license_auth_pic.to_alipay_dict()
            else:
                params['business_license_auth_pic'] = self.business_license_auth_pic
        if self.business_license_city:
            if hasattr(self.business_license_city, 'to_alipay_dict'):
                params['business_license_city'] = self.business_license_city.to_alipay_dict()
            else:
                params['business_license_city'] = self.business_license_city
        if self.business_license_indate:
            if hasattr(self.business_license_indate, 'to_alipay_dict'):
                params['business_license_indate'] = self.business_license_indate.to_alipay_dict()
            else:
                params['business_license_indate'] = self.business_license_indate
        if self.business_license_is_three_in_one:
            if hasattr(self.business_license_is_three_in_one, 'to_alipay_dict'):
                params['business_license_is_three_in_one'] = self.business_license_is_three_in_one.to_alipay_dict()
            else:
                params['business_license_is_three_in_one'] = self.business_license_is_three_in_one
        if self.business_license_no:
            if hasattr(self.business_license_no, 'to_alipay_dict'):
                params['business_license_no'] = self.business_license_no.to_alipay_dict()
            else:
                params['business_license_no'] = self.business_license_no
        if self.business_license_pic:
            if hasattr(self.business_license_pic, 'to_alipay_dict'):
                params['business_license_pic'] = self.business_license_pic.to_alipay_dict()
            else:
                params['business_license_pic'] = self.business_license_pic
        if self.business_license_province:
            if hasattr(self.business_license_province, 'to_alipay_dict'):
                params['business_license_province'] = self.business_license_province.to_alipay_dict()
            else:
                params['business_license_province'] = self.business_license_province
        if self.business_scope:
            if hasattr(self.business_scope, 'to_alipay_dict'):
                params['business_scope'] = self.business_scope.to_alipay_dict()
            else:
                params['business_scope'] = self.business_scope
        if self.company_address:
            if hasattr(self.company_address, 'to_alipay_dict'):
                params['company_address'] = self.company_address.to_alipay_dict()
            else:
                params['company_address'] = self.company_address
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.org_code_certificate_no:
            if hasattr(self.org_code_certificate_no, 'to_alipay_dict'):
                params['org_code_certificate_no'] = self.org_code_certificate_no.to_alipay_dict()
            else:
                params['org_code_certificate_no'] = self.org_code_certificate_no
        if self.org_code_certificate_pic:
            if hasattr(self.org_code_certificate_pic, 'to_alipay_dict'):
                params['org_code_certificate_pic'] = self.org_code_certificate_pic.to_alipay_dict()
            else:
                params['org_code_certificate_pic'] = self.org_code_certificate_pic
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessLicenceInfo()
        if 'business_license_auth_pic' in d:
            o.business_license_auth_pic = d['business_license_auth_pic']
        if 'business_license_city' in d:
            o.business_license_city = d['business_license_city']
        if 'business_license_indate' in d:
            o.business_license_indate = d['business_license_indate']
        if 'business_license_is_three_in_one' in d:
            o.business_license_is_three_in_one = d['business_license_is_three_in_one']
        if 'business_license_no' in d:
            o.business_license_no = d['business_license_no']
        if 'business_license_pic' in d:
            o.business_license_pic = d['business_license_pic']
        if 'business_license_province' in d:
            o.business_license_province = d['business_license_province']
        if 'business_scope' in d:
            o.business_scope = d['business_scope']
        if 'company_address' in d:
            o.company_address = d['company_address']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'org_code_certificate_no' in d:
            o.org_code_certificate_no = d['org_code_certificate_no']
        if 'org_code_certificate_pic' in d:
            o.org_code_certificate_pic = d['org_code_certificate_pic']
        return o


