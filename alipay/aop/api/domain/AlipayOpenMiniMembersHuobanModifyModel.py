#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniMembersHuobanModifyModel(object):

    def __init__(self):
        self._domain_account = None
        self._login_id = None
        self._old_login_id = None
        self._operate_app_id = None
        self._type = None

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
    def old_login_id(self):
        return self._old_login_id

    @old_login_id.setter
    def old_login_id(self, value):
        self._old_login_id = value
    @property
    def operate_app_id(self):
        return self._operate_app_id

    @operate_app_id.setter
    def operate_app_id(self, value):
        self._operate_app_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.old_login_id:
            if hasattr(self.old_login_id, 'to_alipay_dict'):
                params['old_login_id'] = self.old_login_id.to_alipay_dict()
            else:
                params['old_login_id'] = self.old_login_id
        if self.operate_app_id:
            if hasattr(self.operate_app_id, 'to_alipay_dict'):
                params['operate_app_id'] = self.operate_app_id.to_alipay_dict()
            else:
                params['operate_app_id'] = self.operate_app_id
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
        o = AlipayOpenMiniMembersHuobanModifyModel()
        if 'domain_account' in d:
            o.domain_account = d['domain_account']
        if 'login_id' in d:
            o.login_id = d['login_id']
        if 'old_login_id' in d:
            o.old_login_id = d['old_login_id']
        if 'operate_app_id' in d:
            o.operate_app_id = d['operate_app_id']
        if 'type' in d:
            o.type = d['type']
        return o


