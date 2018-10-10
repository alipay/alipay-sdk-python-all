#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BankcardExtInfo(object):

    def __init__(self):
        self._account_type = None
        self._bank_code = None
        self._inst_branch_name = None
        self._inst_city = None
        self._inst_name = None
        self._inst_province = None

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
    def inst_branch_name(self):
        return self._inst_branch_name

    @inst_branch_name.setter
    def inst_branch_name(self, value):
        self._inst_branch_name = value
    @property
    def inst_city(self):
        return self._inst_city

    @inst_city.setter
    def inst_city(self, value):
        self._inst_city = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def inst_province(self):
        return self._inst_province

    @inst_province.setter
    def inst_province(self, value):
        self._inst_province = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.inst_branch_name:
            if hasattr(self.inst_branch_name, 'to_alipay_dict'):
                params['inst_branch_name'] = self.inst_branch_name.to_alipay_dict()
            else:
                params['inst_branch_name'] = self.inst_branch_name
        if self.inst_city:
            if hasattr(self.inst_city, 'to_alipay_dict'):
                params['inst_city'] = self.inst_city.to_alipay_dict()
            else:
                params['inst_city'] = self.inst_city
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        if self.inst_province:
            if hasattr(self.inst_province, 'to_alipay_dict'):
                params['inst_province'] = self.inst_province.to_alipay_dict()
            else:
                params['inst_province'] = self.inst_province
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BankcardExtInfo()
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        if 'inst_branch_name' in d:
            o.inst_branch_name = d['inst_branch_name']
        if 'inst_city' in d:
            o.inst_city = d['inst_city']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        if 'inst_province' in d:
            o.inst_province = d['inst_province']
        return o


