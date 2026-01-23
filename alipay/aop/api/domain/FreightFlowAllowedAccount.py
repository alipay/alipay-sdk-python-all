#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FreightFlowAllowedAccount(object):

    def __init__(self):
        self._allowed_account_name = None
        self._allowed_account_no = None
        self._allowed_account_type = None
        self._expire_date = None

    @property
    def allowed_account_name(self):
        return self._allowed_account_name

    @allowed_account_name.setter
    def allowed_account_name(self, value):
        self._allowed_account_name = value
    @property
    def allowed_account_no(self):
        return self._allowed_account_no

    @allowed_account_no.setter
    def allowed_account_no(self, value):
        self._allowed_account_no = value
    @property
    def allowed_account_type(self):
        return self._allowed_account_type

    @allowed_account_type.setter
    def allowed_account_type(self, value):
        self._allowed_account_type = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.allowed_account_name:
            if hasattr(self.allowed_account_name, 'to_alipay_dict'):
                params['allowed_account_name'] = self.allowed_account_name.to_alipay_dict()
            else:
                params['allowed_account_name'] = self.allowed_account_name
        if self.allowed_account_no:
            if hasattr(self.allowed_account_no, 'to_alipay_dict'):
                params['allowed_account_no'] = self.allowed_account_no.to_alipay_dict()
            else:
                params['allowed_account_no'] = self.allowed_account_no
        if self.allowed_account_type:
            if hasattr(self.allowed_account_type, 'to_alipay_dict'):
                params['allowed_account_type'] = self.allowed_account_type.to_alipay_dict()
            else:
                params['allowed_account_type'] = self.allowed_account_type
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FreightFlowAllowedAccount()
        if 'allowed_account_name' in d:
            o.allowed_account_name = d['allowed_account_name']
        if 'allowed_account_no' in d:
            o.allowed_account_no = d['allowed_account_no']
        if 'allowed_account_type' in d:
            o.allowed_account_type = d['allowed_account_type']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        return o


