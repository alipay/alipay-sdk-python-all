#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditUserSitememberEnterpriseMatchModel(object):

    def __init__(self):
        self._business_reg_no = None
        self._company_name = None
        self._site = None
        self._site_login_id = None
        self._social_credit_code = None

    @property
    def business_reg_no(self):
        return self._business_reg_no

    @business_reg_no.setter
    def business_reg_no(self, value):
        self._business_reg_no = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        self._site = value
    @property
    def site_login_id(self):
        return self._site_login_id

    @site_login_id.setter
    def site_login_id(self, value):
        self._site_login_id = value
    @property
    def social_credit_code(self):
        return self._social_credit_code

    @social_credit_code.setter
    def social_credit_code(self, value):
        self._social_credit_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_reg_no:
            if hasattr(self.business_reg_no, 'to_alipay_dict'):
                params['business_reg_no'] = self.business_reg_no.to_alipay_dict()
            else:
                params['business_reg_no'] = self.business_reg_no
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.site:
            if hasattr(self.site, 'to_alipay_dict'):
                params['site'] = self.site.to_alipay_dict()
            else:
                params['site'] = self.site
        if self.site_login_id:
            if hasattr(self.site_login_id, 'to_alipay_dict'):
                params['site_login_id'] = self.site_login_id.to_alipay_dict()
            else:
                params['site_login_id'] = self.site_login_id
        if self.social_credit_code:
            if hasattr(self.social_credit_code, 'to_alipay_dict'):
                params['social_credit_code'] = self.social_credit_code.to_alipay_dict()
            else:
                params['social_credit_code'] = self.social_credit_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditUserSitememberEnterpriseMatchModel()
        if 'business_reg_no' in d:
            o.business_reg_no = d['business_reg_no']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'site' in d:
            o.site = d['site']
        if 'site_login_id' in d:
            o.site_login_id = d['site_login_id']
        if 'social_credit_code' in d:
            o.social_credit_code = d['social_credit_code']
        return o


