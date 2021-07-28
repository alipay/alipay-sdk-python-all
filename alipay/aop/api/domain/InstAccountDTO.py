#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InstAccountDTO(object):

    def __init__(self):
        self._account_name = None
        self._account_no = None
        self._account_type = None
        self._bank_code = None
        self._biz_param = None
        self._currency = None
        self._org_unit = None
        self._user_id = None

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
    def bank_code(self):
        return self._bank_code

    @bank_code.setter
    def bank_code(self, value):
        self._bank_code = value
    @property
    def biz_param(self):
        return self._biz_param

    @biz_param.setter
    def biz_param(self, value):
        self._biz_param = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def org_unit(self):
        return self._org_unit

    @org_unit.setter
    def org_unit(self, value):
        self._org_unit = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


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
        if self.bank_code:
            if hasattr(self.bank_code, 'to_alipay_dict'):
                params['bank_code'] = self.bank_code.to_alipay_dict()
            else:
                params['bank_code'] = self.bank_code
        if self.biz_param:
            if hasattr(self.biz_param, 'to_alipay_dict'):
                params['biz_param'] = self.biz_param.to_alipay_dict()
            else:
                params['biz_param'] = self.biz_param
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.org_unit:
            if hasattr(self.org_unit, 'to_alipay_dict'):
                params['org_unit'] = self.org_unit.to_alipay_dict()
            else:
                params['org_unit'] = self.org_unit
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstAccountDTO()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        if 'biz_param' in d:
            o.biz_param = d['biz_param']
        if 'currency' in d:
            o.currency = d['currency']
        if 'org_unit' in d:
            o.org_unit = d['org_unit']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


