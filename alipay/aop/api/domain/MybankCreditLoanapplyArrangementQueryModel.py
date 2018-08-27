#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoanapplyArrangementQueryModel(object):

    def __init__(self):
        self._ar_pd_code = None
        self._ip_id = None
        self._ip_role_id = None
        self._site = None
        self._site_user_id = None

    @property
    def ar_pd_code(self):
        return self._ar_pd_code

    @ar_pd_code.setter
    def ar_pd_code(self, value):
        self._ar_pd_code = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        self._site = value
    @property
    def site_user_id(self):
        return self._site_user_id

    @site_user_id.setter
    def site_user_id(self, value):
        self._site_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ar_pd_code:
            if hasattr(self.ar_pd_code, 'to_alipay_dict'):
                params['ar_pd_code'] = self.ar_pd_code.to_alipay_dict()
            else:
                params['ar_pd_code'] = self.ar_pd_code
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.site:
            if hasattr(self.site, 'to_alipay_dict'):
                params['site'] = self.site.to_alipay_dict()
            else:
                params['site'] = self.site
        if self.site_user_id:
            if hasattr(self.site_user_id, 'to_alipay_dict'):
                params['site_user_id'] = self.site_user_id.to_alipay_dict()
            else:
                params['site_user_id'] = self.site_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoanapplyArrangementQueryModel()
        if 'ar_pd_code' in d:
            o.ar_pd_code = d['ar_pd_code']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'site' in d:
            o.site = d['site']
        if 'site_user_id' in d:
            o.site_user_id = d['site_user_id']
        return o


