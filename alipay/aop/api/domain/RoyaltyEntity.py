#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RoyaltyEntity(object):

    def __init__(self):
        self._account = None
        self._account_open_id = None
        self._bind_login_name = None
        self._login_name = None
        self._memo = None
        self._name = None
        self._type = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def account_open_id(self):
        return self._account_open_id

    @account_open_id.setter
    def account_open_id(self, value):
        self._account_open_id = value
    @property
    def bind_login_name(self):
        return self._bind_login_name

    @bind_login_name.setter
    def bind_login_name(self, value):
        self._bind_login_name = value
    @property
    def login_name(self):
        return self._login_name

    @login_name.setter
    def login_name(self, value):
        self._login_name = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.account_open_id:
            if hasattr(self.account_open_id, 'to_alipay_dict'):
                params['account_open_id'] = self.account_open_id.to_alipay_dict()
            else:
                params['account_open_id'] = self.account_open_id
        if self.bind_login_name:
            if hasattr(self.bind_login_name, 'to_alipay_dict'):
                params['bind_login_name'] = self.bind_login_name.to_alipay_dict()
            else:
                params['bind_login_name'] = self.bind_login_name
        if self.login_name:
            if hasattr(self.login_name, 'to_alipay_dict'):
                params['login_name'] = self.login_name.to_alipay_dict()
            else:
                params['login_name'] = self.login_name
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
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
        o = RoyaltyEntity()
        if 'account' in d:
            o.account = d['account']
        if 'account_open_id' in d:
            o.account_open_id = d['account_open_id']
        if 'bind_login_name' in d:
            o.bind_login_name = d['bind_login_name']
        if 'login_name' in d:
            o.login_name = d['login_name']
        if 'memo' in d:
            o.memo = d['memo']
        if 'name' in d:
            o.name = d['name']
        if 'type' in d:
            o.type = d['type']
        return o


