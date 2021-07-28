#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LargeInfiniteCardInfo(object):

    def __init__(self):
        self._account_balance = None
        self._bank_account_name = None
        self._bank_account_no = None
        self._bank_branch = None
        self._bank_branch_code = None
        self._bank_name = None
        self._open_place = None

    @property
    def account_balance(self):
        return self._account_balance

    @account_balance.setter
    def account_balance(self, value):
        self._account_balance = value
    @property
    def bank_account_name(self):
        return self._bank_account_name

    @bank_account_name.setter
    def bank_account_name(self, value):
        self._bank_account_name = value
    @property
    def bank_account_no(self):
        return self._bank_account_no

    @bank_account_no.setter
    def bank_account_no(self, value):
        self._bank_account_no = value
    @property
    def bank_branch(self):
        return self._bank_branch

    @bank_branch.setter
    def bank_branch(self, value):
        self._bank_branch = value
    @property
    def bank_branch_code(self):
        return self._bank_branch_code

    @bank_branch_code.setter
    def bank_branch_code(self, value):
        self._bank_branch_code = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def open_place(self):
        return self._open_place

    @open_place.setter
    def open_place(self, value):
        self._open_place = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_balance:
            if hasattr(self.account_balance, 'to_alipay_dict'):
                params['account_balance'] = self.account_balance.to_alipay_dict()
            else:
                params['account_balance'] = self.account_balance
        if self.bank_account_name:
            if hasattr(self.bank_account_name, 'to_alipay_dict'):
                params['bank_account_name'] = self.bank_account_name.to_alipay_dict()
            else:
                params['bank_account_name'] = self.bank_account_name
        if self.bank_account_no:
            if hasattr(self.bank_account_no, 'to_alipay_dict'):
                params['bank_account_no'] = self.bank_account_no.to_alipay_dict()
            else:
                params['bank_account_no'] = self.bank_account_no
        if self.bank_branch:
            if hasattr(self.bank_branch, 'to_alipay_dict'):
                params['bank_branch'] = self.bank_branch.to_alipay_dict()
            else:
                params['bank_branch'] = self.bank_branch
        if self.bank_branch_code:
            if hasattr(self.bank_branch_code, 'to_alipay_dict'):
                params['bank_branch_code'] = self.bank_branch_code.to_alipay_dict()
            else:
                params['bank_branch_code'] = self.bank_branch_code
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.open_place:
            if hasattr(self.open_place, 'to_alipay_dict'):
                params['open_place'] = self.open_place.to_alipay_dict()
            else:
                params['open_place'] = self.open_place
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LargeInfiniteCardInfo()
        if 'account_balance' in d:
            o.account_balance = d['account_balance']
        if 'bank_account_name' in d:
            o.bank_account_name = d['bank_account_name']
        if 'bank_account_no' in d:
            o.bank_account_no = d['bank_account_no']
        if 'bank_branch' in d:
            o.bank_branch = d['bank_branch']
        if 'bank_branch_code' in d:
            o.bank_branch_code = d['bank_branch_code']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'open_place' in d:
            o.open_place = d['open_place']
        return o


