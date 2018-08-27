#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SettleCardInfo(object):

    def __init__(self):
        self._account_branch_name = None
        self._account_holder_name = None
        self._account_inst_city = None
        self._account_inst_id = None
        self._account_inst_name = None
        self._account_inst_province = None
        self._account_no = None
        self._account_type = None
        self._bank_code = None
        self._usage_type = None

    @property
    def account_branch_name(self):
        return self._account_branch_name

    @account_branch_name.setter
    def account_branch_name(self, value):
        self._account_branch_name = value
    @property
    def account_holder_name(self):
        return self._account_holder_name

    @account_holder_name.setter
    def account_holder_name(self, value):
        self._account_holder_name = value
    @property
    def account_inst_city(self):
        return self._account_inst_city

    @account_inst_city.setter
    def account_inst_city(self, value):
        self._account_inst_city = value
    @property
    def account_inst_id(self):
        return self._account_inst_id

    @account_inst_id.setter
    def account_inst_id(self, value):
        self._account_inst_id = value
    @property
    def account_inst_name(self):
        return self._account_inst_name

    @account_inst_name.setter
    def account_inst_name(self, value):
        self._account_inst_name = value
    @property
    def account_inst_province(self):
        return self._account_inst_province

    @account_inst_province.setter
    def account_inst_province(self, value):
        self._account_inst_province = value
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
    def usage_type(self):
        return self._usage_type

    @usage_type.setter
    def usage_type(self, value):
        self._usage_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_branch_name:
            if hasattr(self.account_branch_name, 'to_alipay_dict'):
                params['account_branch_name'] = self.account_branch_name.to_alipay_dict()
            else:
                params['account_branch_name'] = self.account_branch_name
        if self.account_holder_name:
            if hasattr(self.account_holder_name, 'to_alipay_dict'):
                params['account_holder_name'] = self.account_holder_name.to_alipay_dict()
            else:
                params['account_holder_name'] = self.account_holder_name
        if self.account_inst_city:
            if hasattr(self.account_inst_city, 'to_alipay_dict'):
                params['account_inst_city'] = self.account_inst_city.to_alipay_dict()
            else:
                params['account_inst_city'] = self.account_inst_city
        if self.account_inst_id:
            if hasattr(self.account_inst_id, 'to_alipay_dict'):
                params['account_inst_id'] = self.account_inst_id.to_alipay_dict()
            else:
                params['account_inst_id'] = self.account_inst_id
        if self.account_inst_name:
            if hasattr(self.account_inst_name, 'to_alipay_dict'):
                params['account_inst_name'] = self.account_inst_name.to_alipay_dict()
            else:
                params['account_inst_name'] = self.account_inst_name
        if self.account_inst_province:
            if hasattr(self.account_inst_province, 'to_alipay_dict'):
                params['account_inst_province'] = self.account_inst_province.to_alipay_dict()
            else:
                params['account_inst_province'] = self.account_inst_province
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
        if self.usage_type:
            if hasattr(self.usage_type, 'to_alipay_dict'):
                params['usage_type'] = self.usage_type.to_alipay_dict()
            else:
                params['usage_type'] = self.usage_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SettleCardInfo()
        if 'account_branch_name' in d:
            o.account_branch_name = d['account_branch_name']
        if 'account_holder_name' in d:
            o.account_holder_name = d['account_holder_name']
        if 'account_inst_city' in d:
            o.account_inst_city = d['account_inst_city']
        if 'account_inst_id' in d:
            o.account_inst_id = d['account_inst_id']
        if 'account_inst_name' in d:
            o.account_inst_name = d['account_inst_name']
        if 'account_inst_province' in d:
            o.account_inst_province = d['account_inst_province']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        if 'usage_type' in d:
            o.usage_type = d['usage_type']
        return o


