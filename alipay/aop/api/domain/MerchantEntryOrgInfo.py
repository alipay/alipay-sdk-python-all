#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantEntryOrgInfo(object):

    def __init__(self):
        self._expired_date_is_long_term = None
        self._merchant_type = None
        self._org_address = None
        self._org_business_scope = None
        self._org_cert_image = None
        self._org_cert_no = None
        self._org_cert_type = None
        self._org_expired_date = None
        self._org_name = None

    @property
    def expired_date_is_long_term(self):
        return self._expired_date_is_long_term

    @expired_date_is_long_term.setter
    def expired_date_is_long_term(self, value):
        self._expired_date_is_long_term = value
    @property
    def merchant_type(self):
        return self._merchant_type

    @merchant_type.setter
    def merchant_type(self, value):
        self._merchant_type = value
    @property
    def org_address(self):
        return self._org_address

    @org_address.setter
    def org_address(self, value):
        self._org_address = value
    @property
    def org_business_scope(self):
        return self._org_business_scope

    @org_business_scope.setter
    def org_business_scope(self, value):
        self._org_business_scope = value
    @property
    def org_cert_image(self):
        return self._org_cert_image

    @org_cert_image.setter
    def org_cert_image(self, value):
        self._org_cert_image = value
    @property
    def org_cert_no(self):
        return self._org_cert_no

    @org_cert_no.setter
    def org_cert_no(self, value):
        self._org_cert_no = value
    @property
    def org_cert_type(self):
        return self._org_cert_type

    @org_cert_type.setter
    def org_cert_type(self, value):
        self._org_cert_type = value
    @property
    def org_expired_date(self):
        return self._org_expired_date

    @org_expired_date.setter
    def org_expired_date(self, value):
        self._org_expired_date = value
    @property
    def org_name(self):
        return self._org_name

    @org_name.setter
    def org_name(self, value):
        self._org_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.expired_date_is_long_term:
            if hasattr(self.expired_date_is_long_term, 'to_alipay_dict'):
                params['expired_date_is_long_term'] = self.expired_date_is_long_term.to_alipay_dict()
            else:
                params['expired_date_is_long_term'] = self.expired_date_is_long_term
        if self.merchant_type:
            if hasattr(self.merchant_type, 'to_alipay_dict'):
                params['merchant_type'] = self.merchant_type.to_alipay_dict()
            else:
                params['merchant_type'] = self.merchant_type
        if self.org_address:
            if hasattr(self.org_address, 'to_alipay_dict'):
                params['org_address'] = self.org_address.to_alipay_dict()
            else:
                params['org_address'] = self.org_address
        if self.org_business_scope:
            if hasattr(self.org_business_scope, 'to_alipay_dict'):
                params['org_business_scope'] = self.org_business_scope.to_alipay_dict()
            else:
                params['org_business_scope'] = self.org_business_scope
        if self.org_cert_image:
            if hasattr(self.org_cert_image, 'to_alipay_dict'):
                params['org_cert_image'] = self.org_cert_image.to_alipay_dict()
            else:
                params['org_cert_image'] = self.org_cert_image
        if self.org_cert_no:
            if hasattr(self.org_cert_no, 'to_alipay_dict'):
                params['org_cert_no'] = self.org_cert_no.to_alipay_dict()
            else:
                params['org_cert_no'] = self.org_cert_no
        if self.org_cert_type:
            if hasattr(self.org_cert_type, 'to_alipay_dict'):
                params['org_cert_type'] = self.org_cert_type.to_alipay_dict()
            else:
                params['org_cert_type'] = self.org_cert_type
        if self.org_expired_date:
            if hasattr(self.org_expired_date, 'to_alipay_dict'):
                params['org_expired_date'] = self.org_expired_date.to_alipay_dict()
            else:
                params['org_expired_date'] = self.org_expired_date
        if self.org_name:
            if hasattr(self.org_name, 'to_alipay_dict'):
                params['org_name'] = self.org_name.to_alipay_dict()
            else:
                params['org_name'] = self.org_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantEntryOrgInfo()
        if 'expired_date_is_long_term' in d:
            o.expired_date_is_long_term = d['expired_date_is_long_term']
        if 'merchant_type' in d:
            o.merchant_type = d['merchant_type']
        if 'org_address' in d:
            o.org_address = d['org_address']
        if 'org_business_scope' in d:
            o.org_business_scope = d['org_business_scope']
        if 'org_cert_image' in d:
            o.org_cert_image = d['org_cert_image']
        if 'org_cert_no' in d:
            o.org_cert_no = d['org_cert_no']
        if 'org_cert_type' in d:
            o.org_cert_type = d['org_cert_type']
        if 'org_expired_date' in d:
            o.org_expired_date = d['org_expired_date']
        if 'org_name' in d:
            o.org_name = d['org_name']
        return o


