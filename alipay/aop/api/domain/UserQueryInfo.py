#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserQueryInfo(object):

    def __init__(self):
        self._account = None
        self._open_id = None
        self._phone = None
        self._user_id = None
        self._virtual_uid = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def virtual_uid(self):
        return self._virtual_uid

    @virtual_uid.setter
    def virtual_uid(self, value):
        self._virtual_uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.virtual_uid:
            if hasattr(self.virtual_uid, 'to_alipay_dict'):
                params['virtual_uid'] = self.virtual_uid.to_alipay_dict()
            else:
                params['virtual_uid'] = self.virtual_uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserQueryInfo()
        if 'account' in d:
            o.account = d['account']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'phone' in d:
            o.phone = d['phone']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'virtual_uid' in d:
            o.virtual_uid = d['virtual_uid']
        return o


