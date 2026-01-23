#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PolicyAccountInfoModel(object):

    def __init__(self):
        self._account_type = None
        self._alipay_account = None
        self._bank_account_city = None
        self._bank_account_city_id = None
        self._bank_account_name = None
        self._bank_account_province = None
        self._bank_account_province_id = None
        self._bank_branch_name = None
        self._bank_card_account = None
        self._bank_inst_code = None
        self._bank_name = None

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def alipay_account(self):
        return self._alipay_account

    @alipay_account.setter
    def alipay_account(self, value):
        self._alipay_account = value
    @property
    def bank_account_city(self):
        return self._bank_account_city

    @bank_account_city.setter
    def bank_account_city(self, value):
        self._bank_account_city = value
    @property
    def bank_account_city_id(self):
        return self._bank_account_city_id

    @bank_account_city_id.setter
    def bank_account_city_id(self, value):
        self._bank_account_city_id = value
    @property
    def bank_account_name(self):
        return self._bank_account_name

    @bank_account_name.setter
    def bank_account_name(self, value):
        self._bank_account_name = value
    @property
    def bank_account_province(self):
        return self._bank_account_province

    @bank_account_province.setter
    def bank_account_province(self, value):
        self._bank_account_province = value
    @property
    def bank_account_province_id(self):
        return self._bank_account_province_id

    @bank_account_province_id.setter
    def bank_account_province_id(self, value):
        self._bank_account_province_id = value
    @property
    def bank_branch_name(self):
        return self._bank_branch_name

    @bank_branch_name.setter
    def bank_branch_name(self, value):
        self._bank_branch_name = value
    @property
    def bank_card_account(self):
        return self._bank_card_account

    @bank_card_account.setter
    def bank_card_account(self, value):
        self._bank_card_account = value
    @property
    def bank_inst_code(self):
        return self._bank_inst_code

    @bank_inst_code.setter
    def bank_inst_code(self, value):
        self._bank_inst_code = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.alipay_account:
            if hasattr(self.alipay_account, 'to_alipay_dict'):
                params['alipay_account'] = self.alipay_account.to_alipay_dict()
            else:
                params['alipay_account'] = self.alipay_account
        if self.bank_account_city:
            if hasattr(self.bank_account_city, 'to_alipay_dict'):
                params['bank_account_city'] = self.bank_account_city.to_alipay_dict()
            else:
                params['bank_account_city'] = self.bank_account_city
        if self.bank_account_city_id:
            if hasattr(self.bank_account_city_id, 'to_alipay_dict'):
                params['bank_account_city_id'] = self.bank_account_city_id.to_alipay_dict()
            else:
                params['bank_account_city_id'] = self.bank_account_city_id
        if self.bank_account_name:
            if hasattr(self.bank_account_name, 'to_alipay_dict'):
                params['bank_account_name'] = self.bank_account_name.to_alipay_dict()
            else:
                params['bank_account_name'] = self.bank_account_name
        if self.bank_account_province:
            if hasattr(self.bank_account_province, 'to_alipay_dict'):
                params['bank_account_province'] = self.bank_account_province.to_alipay_dict()
            else:
                params['bank_account_province'] = self.bank_account_province
        if self.bank_account_province_id:
            if hasattr(self.bank_account_province_id, 'to_alipay_dict'):
                params['bank_account_province_id'] = self.bank_account_province_id.to_alipay_dict()
            else:
                params['bank_account_province_id'] = self.bank_account_province_id
        if self.bank_branch_name:
            if hasattr(self.bank_branch_name, 'to_alipay_dict'):
                params['bank_branch_name'] = self.bank_branch_name.to_alipay_dict()
            else:
                params['bank_branch_name'] = self.bank_branch_name
        if self.bank_card_account:
            if hasattr(self.bank_card_account, 'to_alipay_dict'):
                params['bank_card_account'] = self.bank_card_account.to_alipay_dict()
            else:
                params['bank_card_account'] = self.bank_card_account
        if self.bank_inst_code:
            if hasattr(self.bank_inst_code, 'to_alipay_dict'):
                params['bank_inst_code'] = self.bank_inst_code.to_alipay_dict()
            else:
                params['bank_inst_code'] = self.bank_inst_code
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PolicyAccountInfoModel()
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'alipay_account' in d:
            o.alipay_account = d['alipay_account']
        if 'bank_account_city' in d:
            o.bank_account_city = d['bank_account_city']
        if 'bank_account_city_id' in d:
            o.bank_account_city_id = d['bank_account_city_id']
        if 'bank_account_name' in d:
            o.bank_account_name = d['bank_account_name']
        if 'bank_account_province' in d:
            o.bank_account_province = d['bank_account_province']
        if 'bank_account_province_id' in d:
            o.bank_account_province_id = d['bank_account_province_id']
        if 'bank_branch_name' in d:
            o.bank_branch_name = d['bank_branch_name']
        if 'bank_card_account' in d:
            o.bank_card_account = d['bank_card_account']
        if 'bank_inst_code' in d:
            o.bank_inst_code = d['bank_inst_code']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        return o


