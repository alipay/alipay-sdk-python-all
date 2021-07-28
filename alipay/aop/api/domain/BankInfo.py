#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BankInfo(object):

    def __init__(self):
        self._account_issue_entity_id = None
        self._account_issue_entity_name = None
        self._account_name = None
        self._account_no = None
        self._bank_code = None

    @property
    def account_issue_entity_id(self):
        return self._account_issue_entity_id

    @account_issue_entity_id.setter
    def account_issue_entity_id(self, value):
        self._account_issue_entity_id = value
    @property
    def account_issue_entity_name(self):
        return self._account_issue_entity_name

    @account_issue_entity_name.setter
    def account_issue_entity_name(self, value):
        self._account_issue_entity_name = value
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
    def bank_code(self):
        return self._bank_code

    @bank_code.setter
    def bank_code(self, value):
        self._bank_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_issue_entity_id:
            if hasattr(self.account_issue_entity_id, 'to_alipay_dict'):
                params['account_issue_entity_id'] = self.account_issue_entity_id.to_alipay_dict()
            else:
                params['account_issue_entity_id'] = self.account_issue_entity_id
        if self.account_issue_entity_name:
            if hasattr(self.account_issue_entity_name, 'to_alipay_dict'):
                params['account_issue_entity_name'] = self.account_issue_entity_name.to_alipay_dict()
            else:
                params['account_issue_entity_name'] = self.account_issue_entity_name
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
        if self.bank_code:
            if hasattr(self.bank_code, 'to_alipay_dict'):
                params['bank_code'] = self.bank_code.to_alipay_dict()
            else:
                params['bank_code'] = self.bank_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BankInfo()
        if 'account_issue_entity_id' in d:
            o.account_issue_entity_id = d['account_issue_entity_id']
        if 'account_issue_entity_name' in d:
            o.account_issue_entity_name = d['account_issue_entity_name']
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        return o


