#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TrustAccountInfo(object):

    def __init__(self):
        self._account_name = None
        self._account_no = None
        self._account_type = None
        self._bank_branch_code = None
        self._bank_branch_name = None
        self._bank_name = None
        self._personal_acc = None

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
    @property
    def bank_branch_code(self):
        return self._bank_branch_code

    @bank_branch_code.setter
    def bank_branch_code(self, value):
        self._bank_branch_code = value
    @property
    def bank_branch_name(self):
        return self._bank_branch_name

    @bank_branch_name.setter
    def bank_branch_name(self, value):
        self._bank_branch_name = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def personal_acc(self):
        return self._personal_acc

    @personal_acc.setter
    def personal_acc(self, value):
        self._personal_acc = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.bank_branch_code:
            if hasattr(self.bank_branch_code, 'to_alipay_dict'):
                params['bank_branch_code'] = self.bank_branch_code.to_alipay_dict()
            else:
                params['bank_branch_code'] = self.bank_branch_code
        if self.bank_branch_name:
            if hasattr(self.bank_branch_name, 'to_alipay_dict'):
                params['bank_branch_name'] = self.bank_branch_name.to_alipay_dict()
            else:
                params['bank_branch_name'] = self.bank_branch_name
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.personal_acc:
            if hasattr(self.personal_acc, 'to_alipay_dict'):
                params['personal_acc'] = self.personal_acc.to_alipay_dict()
            else:
                params['personal_acc'] = self.personal_acc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TrustAccountInfo()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'bank_branch_code' in d:
            o.bank_branch_code = d['bank_branch_code']
        if 'bank_branch_name' in d:
            o.bank_branch_name = d['bank_branch_name']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'personal_acc' in d:
            o.personal_acc = d['personal_acc']
        return o


