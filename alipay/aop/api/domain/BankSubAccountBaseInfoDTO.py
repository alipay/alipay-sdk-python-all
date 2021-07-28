#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BankSubAccountBaseInfoDTO(object):

    def __init__(self):
        self._account_no = None
        self._account_no_4_credit_transfer = None
        self._country_code = None
        self._currency = None
        self._global_account_name = None
        self._global_bank_name = None
        self._global_branch_name = None
        self._global_sub_bank_name = None
        self._local_account_name = None
        self._local_bank_name = None
        self._local_bank_name_4_transfer = None
        self._local_branch_name = None
        self._local_sub_bank_name = None
        self._out_fin_inst_abbreviation = None
        self._sub_account_no = None
        self._treasury_biz_type = None
        self._treasury_biz_type_name = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def account_no_4_credit_transfer(self):
        return self._account_no_4_credit_transfer

    @account_no_4_credit_transfer.setter
    def account_no_4_credit_transfer(self, value):
        self._account_no_4_credit_transfer = value
    @property
    def country_code(self):
        return self._country_code

    @country_code.setter
    def country_code(self, value):
        self._country_code = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def global_account_name(self):
        return self._global_account_name

    @global_account_name.setter
    def global_account_name(self, value):
        self._global_account_name = value
    @property
    def global_bank_name(self):
        return self._global_bank_name

    @global_bank_name.setter
    def global_bank_name(self, value):
        self._global_bank_name = value
    @property
    def global_branch_name(self):
        return self._global_branch_name

    @global_branch_name.setter
    def global_branch_name(self, value):
        self._global_branch_name = value
    @property
    def global_sub_bank_name(self):
        return self._global_sub_bank_name

    @global_sub_bank_name.setter
    def global_sub_bank_name(self, value):
        self._global_sub_bank_name = value
    @property
    def local_account_name(self):
        return self._local_account_name

    @local_account_name.setter
    def local_account_name(self, value):
        self._local_account_name = value
    @property
    def local_bank_name(self):
        return self._local_bank_name

    @local_bank_name.setter
    def local_bank_name(self, value):
        self._local_bank_name = value
    @property
    def local_bank_name_4_transfer(self):
        return self._local_bank_name_4_transfer

    @local_bank_name_4_transfer.setter
    def local_bank_name_4_transfer(self, value):
        self._local_bank_name_4_transfer = value
    @property
    def local_branch_name(self):
        return self._local_branch_name

    @local_branch_name.setter
    def local_branch_name(self, value):
        self._local_branch_name = value
    @property
    def local_sub_bank_name(self):
        return self._local_sub_bank_name

    @local_sub_bank_name.setter
    def local_sub_bank_name(self, value):
        self._local_sub_bank_name = value
    @property
    def out_fin_inst_abbreviation(self):
        return self._out_fin_inst_abbreviation

    @out_fin_inst_abbreviation.setter
    def out_fin_inst_abbreviation(self, value):
        self._out_fin_inst_abbreviation = value
    @property
    def sub_account_no(self):
        return self._sub_account_no

    @sub_account_no.setter
    def sub_account_no(self, value):
        self._sub_account_no = value
    @property
    def treasury_biz_type(self):
        return self._treasury_biz_type

    @treasury_biz_type.setter
    def treasury_biz_type(self, value):
        self._treasury_biz_type = value
    @property
    def treasury_biz_type_name(self):
        return self._treasury_biz_type_name

    @treasury_biz_type_name.setter
    def treasury_biz_type_name(self, value):
        self._treasury_biz_type_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.account_no_4_credit_transfer:
            if hasattr(self.account_no_4_credit_transfer, 'to_alipay_dict'):
                params['account_no_4_credit_transfer'] = self.account_no_4_credit_transfer.to_alipay_dict()
            else:
                params['account_no_4_credit_transfer'] = self.account_no_4_credit_transfer
        if self.country_code:
            if hasattr(self.country_code, 'to_alipay_dict'):
                params['country_code'] = self.country_code.to_alipay_dict()
            else:
                params['country_code'] = self.country_code
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.global_account_name:
            if hasattr(self.global_account_name, 'to_alipay_dict'):
                params['global_account_name'] = self.global_account_name.to_alipay_dict()
            else:
                params['global_account_name'] = self.global_account_name
        if self.global_bank_name:
            if hasattr(self.global_bank_name, 'to_alipay_dict'):
                params['global_bank_name'] = self.global_bank_name.to_alipay_dict()
            else:
                params['global_bank_name'] = self.global_bank_name
        if self.global_branch_name:
            if hasattr(self.global_branch_name, 'to_alipay_dict'):
                params['global_branch_name'] = self.global_branch_name.to_alipay_dict()
            else:
                params['global_branch_name'] = self.global_branch_name
        if self.global_sub_bank_name:
            if hasattr(self.global_sub_bank_name, 'to_alipay_dict'):
                params['global_sub_bank_name'] = self.global_sub_bank_name.to_alipay_dict()
            else:
                params['global_sub_bank_name'] = self.global_sub_bank_name
        if self.local_account_name:
            if hasattr(self.local_account_name, 'to_alipay_dict'):
                params['local_account_name'] = self.local_account_name.to_alipay_dict()
            else:
                params['local_account_name'] = self.local_account_name
        if self.local_bank_name:
            if hasattr(self.local_bank_name, 'to_alipay_dict'):
                params['local_bank_name'] = self.local_bank_name.to_alipay_dict()
            else:
                params['local_bank_name'] = self.local_bank_name
        if self.local_bank_name_4_transfer:
            if hasattr(self.local_bank_name_4_transfer, 'to_alipay_dict'):
                params['local_bank_name_4_transfer'] = self.local_bank_name_4_transfer.to_alipay_dict()
            else:
                params['local_bank_name_4_transfer'] = self.local_bank_name_4_transfer
        if self.local_branch_name:
            if hasattr(self.local_branch_name, 'to_alipay_dict'):
                params['local_branch_name'] = self.local_branch_name.to_alipay_dict()
            else:
                params['local_branch_name'] = self.local_branch_name
        if self.local_sub_bank_name:
            if hasattr(self.local_sub_bank_name, 'to_alipay_dict'):
                params['local_sub_bank_name'] = self.local_sub_bank_name.to_alipay_dict()
            else:
                params['local_sub_bank_name'] = self.local_sub_bank_name
        if self.out_fin_inst_abbreviation:
            if hasattr(self.out_fin_inst_abbreviation, 'to_alipay_dict'):
                params['out_fin_inst_abbreviation'] = self.out_fin_inst_abbreviation.to_alipay_dict()
            else:
                params['out_fin_inst_abbreviation'] = self.out_fin_inst_abbreviation
        if self.sub_account_no:
            if hasattr(self.sub_account_no, 'to_alipay_dict'):
                params['sub_account_no'] = self.sub_account_no.to_alipay_dict()
            else:
                params['sub_account_no'] = self.sub_account_no
        if self.treasury_biz_type:
            if hasattr(self.treasury_biz_type, 'to_alipay_dict'):
                params['treasury_biz_type'] = self.treasury_biz_type.to_alipay_dict()
            else:
                params['treasury_biz_type'] = self.treasury_biz_type
        if self.treasury_biz_type_name:
            if hasattr(self.treasury_biz_type_name, 'to_alipay_dict'):
                params['treasury_biz_type_name'] = self.treasury_biz_type_name.to_alipay_dict()
            else:
                params['treasury_biz_type_name'] = self.treasury_biz_type_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BankSubAccountBaseInfoDTO()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'account_no_4_credit_transfer' in d:
            o.account_no_4_credit_transfer = d['account_no_4_credit_transfer']
        if 'country_code' in d:
            o.country_code = d['country_code']
        if 'currency' in d:
            o.currency = d['currency']
        if 'global_account_name' in d:
            o.global_account_name = d['global_account_name']
        if 'global_bank_name' in d:
            o.global_bank_name = d['global_bank_name']
        if 'global_branch_name' in d:
            o.global_branch_name = d['global_branch_name']
        if 'global_sub_bank_name' in d:
            o.global_sub_bank_name = d['global_sub_bank_name']
        if 'local_account_name' in d:
            o.local_account_name = d['local_account_name']
        if 'local_bank_name' in d:
            o.local_bank_name = d['local_bank_name']
        if 'local_bank_name_4_transfer' in d:
            o.local_bank_name_4_transfer = d['local_bank_name_4_transfer']
        if 'local_branch_name' in d:
            o.local_branch_name = d['local_branch_name']
        if 'local_sub_bank_name' in d:
            o.local_sub_bank_name = d['local_sub_bank_name']
        if 'out_fin_inst_abbreviation' in d:
            o.out_fin_inst_abbreviation = d['out_fin_inst_abbreviation']
        if 'sub_account_no' in d:
            o.sub_account_no = d['sub_account_no']
        if 'treasury_biz_type' in d:
            o.treasury_biz_type = d['treasury_biz_type']
        if 'treasury_biz_type_name' in d:
            o.treasury_biz_type_name = d['treasury_biz_type_name']
        return o


