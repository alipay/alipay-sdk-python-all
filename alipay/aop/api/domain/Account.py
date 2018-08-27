#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Account(object):

    def __init__(self):
        self._account_ext = None
        self._account_name = None
        self._account_no = None
        self._account_type = None

    @property
    def account_ext(self):
        return self._account_ext

    @account_ext.setter
    def account_ext(self, value):
        self._account_ext = value
    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_ext:
            if hasattr(self.account_ext, 'to_alipay_dict'):
                params['account_ext'] = self.account_ext.to_alipay_dict()
            else:
                params['account_ext'] = self.account_ext
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Account()
        if 'account_ext' in d:
            o.account_ext = d['account_ext']
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'account_type' in d:
            o.account_type = d['account_type']
        return o


