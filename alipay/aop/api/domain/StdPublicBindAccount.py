#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StdPublicBindAccount(object):

    def __init__(self):
        self._agreement_id = None
        self._app_id = None
        self._bind_account_no = None
        self._display_name = None
        self._from_user_id = None
        self._real_name = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def app_id(self):
        return self._app_id

    @app_id.setter
    def app_id(self, value):
        self._app_id = value
    @property
    def bind_account_no(self):
        return self._bind_account_no

    @bind_account_no.setter
    def bind_account_no(self, value):
        self._bind_account_no = value
    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        self._display_name = value
    @property
    def from_user_id(self):
        return self._from_user_id

    @from_user_id.setter
    def from_user_id(self, value):
        self._from_user_id = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_id:
            if hasattr(self.agreement_id, 'to_alipay_dict'):
                params['agreement_id'] = self.agreement_id.to_alipay_dict()
            else:
                params['agreement_id'] = self.agreement_id
        if self.app_id:
            if hasattr(self.app_id, 'to_alipay_dict'):
                params['app_id'] = self.app_id.to_alipay_dict()
            else:
                params['app_id'] = self.app_id
        if self.bind_account_no:
            if hasattr(self.bind_account_no, 'to_alipay_dict'):
                params['bind_account_no'] = self.bind_account_no.to_alipay_dict()
            else:
                params['bind_account_no'] = self.bind_account_no
        if self.display_name:
            if hasattr(self.display_name, 'to_alipay_dict'):
                params['display_name'] = self.display_name.to_alipay_dict()
            else:
                params['display_name'] = self.display_name
        if self.from_user_id:
            if hasattr(self.from_user_id, 'to_alipay_dict'):
                params['from_user_id'] = self.from_user_id.to_alipay_dict()
            else:
                params['from_user_id'] = self.from_user_id
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = self.real_name.to_alipay_dict()
            else:
                params['real_name'] = self.real_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StdPublicBindAccount()
        if 'agreement_id' in d:
            o.agreement_id = d['agreement_id']
        if 'app_id' in d:
            o.app_id = d['app_id']
        if 'bind_account_no' in d:
            o.bind_account_no = d['bind_account_no']
        if 'display_name' in d:
            o.display_name = d['display_name']
        if 'from_user_id' in d:
            o.from_user_id = d['from_user_id']
        if 'real_name' in d:
            o.real_name = d['real_name']
        return o


