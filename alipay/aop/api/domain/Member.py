#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Member(object):

    def __init__(self):
        self._ip_id = None
        self._ip_role_id = None
        self._site = None
        self._site_login_id = None
        self._site_user_id = None
        self._use_type = None

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
    def site_login_id(self):
        return self._site_login_id

    @site_login_id.setter
    def site_login_id(self, value):
        self._site_login_id = value
    @property
    def site_user_id(self):
        return self._site_user_id

    @site_user_id.setter
    def site_user_id(self, value):
        self._site_user_id = value
    @property
    def use_type(self):
        return self._use_type

    @use_type.setter
    def use_type(self, value):
        self._use_type = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.site_login_id:
            if hasattr(self.site_login_id, 'to_alipay_dict'):
                params['site_login_id'] = self.site_login_id.to_alipay_dict()
            else:
                params['site_login_id'] = self.site_login_id
        if self.site_user_id:
            if hasattr(self.site_user_id, 'to_alipay_dict'):
                params['site_user_id'] = self.site_user_id.to_alipay_dict()
            else:
                params['site_user_id'] = self.site_user_id
        if self.use_type:
            if hasattr(self.use_type, 'to_alipay_dict'):
                params['use_type'] = self.use_type.to_alipay_dict()
            else:
                params['use_type'] = self.use_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Member()
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'site' in d:
            o.site = d['site']
        if 'site_login_id' in d:
            o.site_login_id = d['site_login_id']
        if 'site_user_id' in d:
            o.site_user_id = d['site_user_id']
        if 'use_type' in d:
            o.use_type = d['use_type']
        return o


