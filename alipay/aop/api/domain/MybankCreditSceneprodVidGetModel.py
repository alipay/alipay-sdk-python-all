#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditSceneprodVidGetModel(object):

    def __init__(self):
        self._alipay_version = None
        self._meta_info = None
        self._org_code = None
        self._site = None
        self._site_user_id = None
        self._verify_type = None

    @property
    def alipay_version(self):
        return self._alipay_version

    @alipay_version.setter
    def alipay_version(self, value):
        self._alipay_version = value
    @property
    def meta_info(self):
        return self._meta_info

    @meta_info.setter
    def meta_info(self, value):
        self._meta_info = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
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
    @property
    def verify_type(self):
        return self._verify_type

    @verify_type.setter
    def verify_type(self, value):
        self._verify_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_version:
            if hasattr(self.alipay_version, 'to_alipay_dict'):
                params['alipay_version'] = self.alipay_version.to_alipay_dict()
            else:
                params['alipay_version'] = self.alipay_version
        if self.meta_info:
            if hasattr(self.meta_info, 'to_alipay_dict'):
                params['meta_info'] = self.meta_info.to_alipay_dict()
            else:
                params['meta_info'] = self.meta_info
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
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
        if self.verify_type:
            if hasattr(self.verify_type, 'to_alipay_dict'):
                params['verify_type'] = self.verify_type.to_alipay_dict()
            else:
                params['verify_type'] = self.verify_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSceneprodVidGetModel()
        if 'alipay_version' in d:
            o.alipay_version = d['alipay_version']
        if 'meta_info' in d:
            o.meta_info = d['meta_info']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'site' in d:
            o.site = d['site']
        if 'site_user_id' in d:
            o.site_user_id = d['site_user_id']
        if 'verify_type' in d:
            o.verify_type = d['verify_type']
        return o


