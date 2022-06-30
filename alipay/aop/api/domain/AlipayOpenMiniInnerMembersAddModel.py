#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerMembersAddModel(object):

    def __init__(self):
        self._app_origin = None
        self._domain_account = None
        self._login_id = None
        self._mini_app_id = None
        self._type = None

    @property
    def app_origin(self):
        return self._app_origin

    @app_origin.setter
    def app_origin(self, value):
        self._app_origin = value
    @property
    def domain_account(self):
        return self._domain_account

    @domain_account.setter
    def domain_account(self, value):
        self._domain_account = value
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_origin:
            if hasattr(self.app_origin, 'to_alipay_dict'):
                params['app_origin'] = self.app_origin.to_alipay_dict()
            else:
                params['app_origin'] = self.app_origin
        if self.domain_account:
            if hasattr(self.domain_account, 'to_alipay_dict'):
                params['domain_account'] = self.domain_account.to_alipay_dict()
            else:
                params['domain_account'] = self.domain_account
        if self.login_id:
            if hasattr(self.login_id, 'to_alipay_dict'):
                params['login_id'] = self.login_id.to_alipay_dict()
            else:
                params['login_id'] = self.login_id
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerMembersAddModel()
        if 'app_origin' in d:
            o.app_origin = d['app_origin']
        if 'domain_account' in d:
            o.domain_account = d['domain_account']
        if 'login_id' in d:
            o.login_id = d['login_id']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'type' in d:
            o.type = d['type']
        return o


