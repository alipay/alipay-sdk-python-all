#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbasePassaccountNameModifyModel(object):

    def __init__(self):
        self._account_type = None
        self._new_account_name = None
        self._passport_id = None

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def new_account_name(self):
        return self._new_account_name

    @new_account_name.setter
    def new_account_name(self, value):
        self._new_account_name = value
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.new_account_name:
            if hasattr(self.new_account_name, 'to_alipay_dict'):
                params['new_account_name'] = self.new_account_name.to_alipay_dict()
            else:
                params['new_account_name'] = self.new_account_name
        if self.passport_id:
            if hasattr(self.passport_id, 'to_alipay_dict'):
                params['passport_id'] = self.passport_id.to_alipay_dict()
            else:
                params['passport_id'] = self.passport_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbasePassaccountNameModifyModel()
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'new_account_name' in d:
            o.new_account_name = d['new_account_name']
        if 'passport_id' in d:
            o.passport_id = d['passport_id']
        return o


