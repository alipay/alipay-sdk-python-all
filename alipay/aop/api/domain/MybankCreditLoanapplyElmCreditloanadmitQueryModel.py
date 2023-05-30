#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoanapplyElmCreditloanadmitQueryModel(object):

    def __init__(self):
        self._mybk_auth_scene_code = None
        self._mybk_auth_token = None
        self._open_id = None
        self._site = None
        self._site_user_id = None

    @property
    def mybk_auth_scene_code(self):
        return self._mybk_auth_scene_code

    @mybk_auth_scene_code.setter
    def mybk_auth_scene_code(self, value):
        self._mybk_auth_scene_code = value
    @property
    def mybk_auth_token(self):
        return self._mybk_auth_token

    @mybk_auth_token.setter
    def mybk_auth_token(self, value):
        self._mybk_auth_token = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
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
        if self.mybk_auth_scene_code:
            if hasattr(self.mybk_auth_scene_code, 'to_alipay_dict'):
                params['mybk_auth_scene_code'] = self.mybk_auth_scene_code.to_alipay_dict()
            else:
                params['mybk_auth_scene_code'] = self.mybk_auth_scene_code
        if self.mybk_auth_token:
            if hasattr(self.mybk_auth_token, 'to_alipay_dict'):
                params['mybk_auth_token'] = self.mybk_auth_token.to_alipay_dict()
            else:
                params['mybk_auth_token'] = self.mybk_auth_token
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        o = MybankCreditLoanapplyElmCreditloanadmitQueryModel()
        if 'mybk_auth_scene_code' in d:
            o.mybk_auth_scene_code = d['mybk_auth_scene_code']
        if 'mybk_auth_token' in d:
            o.mybk_auth_token = d['mybk_auth_token']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'site' in d:
            o.site = d['site']
        if 'site_user_id' in d:
            o.site_user_id = d['site_user_id']
        return o


