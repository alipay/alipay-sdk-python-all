#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalmgmtHrhealthEntryUserInitializeModel(object):

    def __init__(self):
        self._account = None
        self._data_key = None
        self._form_no = None
        self._password = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def data_key(self):
        return self._data_key

    @data_key.setter
    def data_key(self, value):
        self._data_key = value
    @property
    def form_no(self):
        return self._form_no

    @form_no.setter
    def form_no(self, value):
        self._form_no = value
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.data_key:
            if hasattr(self.data_key, 'to_alipay_dict'):
                params['data_key'] = self.data_key.to_alipay_dict()
            else:
                params['data_key'] = self.data_key
        if self.form_no:
            if hasattr(self.form_no, 'to_alipay_dict'):
                params['form_no'] = self.form_no.to_alipay_dict()
            else:
                params['form_no'] = self.form_no
        if self.password:
            if hasattr(self.password, 'to_alipay_dict'):
                params['password'] = self.password.to_alipay_dict()
            else:
                params['password'] = self.password
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtHrhealthEntryUserInitializeModel()
        if 'account' in d:
            o.account = d['account']
        if 'data_key' in d:
            o.data_key = d['data_key']
        if 'form_no' in d:
            o.form_no = d['form_no']
        if 'password' in d:
            o.password = d['password']
        return o


