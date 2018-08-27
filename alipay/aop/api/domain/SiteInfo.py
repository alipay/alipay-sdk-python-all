#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SiteInfo(object):

    def __init__(self):
        self._account = None
        self._password = None
        self._site_name = None
        self._site_type = None
        self._site_url = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
    @property
    def site_name(self):
        return self._site_name

    @site_name.setter
    def site_name(self, value):
        self._site_name = value
    @property
    def site_type(self):
        return self._site_type

    @site_type.setter
    def site_type(self, value):
        self._site_type = value
    @property
    def site_url(self):
        return self._site_url

    @site_url.setter
    def site_url(self, value):
        self._site_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.password:
            if hasattr(self.password, 'to_alipay_dict'):
                params['password'] = self.password.to_alipay_dict()
            else:
                params['password'] = self.password
        if self.site_name:
            if hasattr(self.site_name, 'to_alipay_dict'):
                params['site_name'] = self.site_name.to_alipay_dict()
            else:
                params['site_name'] = self.site_name
        if self.site_type:
            if hasattr(self.site_type, 'to_alipay_dict'):
                params['site_type'] = self.site_type.to_alipay_dict()
            else:
                params['site_type'] = self.site_type
        if self.site_url:
            if hasattr(self.site_url, 'to_alipay_dict'):
                params['site_url'] = self.site_url.to_alipay_dict()
            else:
                params['site_url'] = self.site_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SiteInfo()
        if 'account' in d:
            o.account = d['account']
        if 'password' in d:
            o.password = d['password']
        if 'site_name' in d:
            o.site_name = d['site_name']
        if 'site_type' in d:
            o.site_type = d['site_type']
        if 'site_url' in d:
            o.site_url = d['site_url']
        return o


