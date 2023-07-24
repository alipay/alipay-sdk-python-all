#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IncomeDistributionTransInInfo(object):

    def __init__(self):
        self._allocate_rate = None
        self._bank_branch_code = None
        self._bank_branch_name = None
        self._digit_currency_inst = None
        self._trans_in_account_no = None
        self._trans_in_account_type = None
        self._trans_in_cert_no = None
        self._trans_in_cert_type = None
        self._trans_in_name = None

    @property
    def allocate_rate(self):
        return self._allocate_rate

    @allocate_rate.setter
    def allocate_rate(self, value):
        self._allocate_rate = value
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
    def digit_currency_inst(self):
        return self._digit_currency_inst

    @digit_currency_inst.setter
    def digit_currency_inst(self, value):
        self._digit_currency_inst = value
    @property
    def trans_in_account_no(self):
        return self._trans_in_account_no

    @trans_in_account_no.setter
    def trans_in_account_no(self, value):
        self._trans_in_account_no = value
    @property
    def trans_in_account_type(self):
        return self._trans_in_account_type

    @trans_in_account_type.setter
    def trans_in_account_type(self, value):
        self._trans_in_account_type = value
    @property
    def trans_in_cert_no(self):
        return self._trans_in_cert_no

    @trans_in_cert_no.setter
    def trans_in_cert_no(self, value):
        self._trans_in_cert_no = value
    @property
    def trans_in_cert_type(self):
        return self._trans_in_cert_type

    @trans_in_cert_type.setter
    def trans_in_cert_type(self, value):
        self._trans_in_cert_type = value
    @property
    def trans_in_name(self):
        return self._trans_in_name

    @trans_in_name.setter
    def trans_in_name(self, value):
        self._trans_in_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.allocate_rate:
            if hasattr(self.allocate_rate, 'to_alipay_dict'):
                params['allocate_rate'] = self.allocate_rate.to_alipay_dict()
            else:
                params['allocate_rate'] = self.allocate_rate
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
        if self.digit_currency_inst:
            if hasattr(self.digit_currency_inst, 'to_alipay_dict'):
                params['digit_currency_inst'] = self.digit_currency_inst.to_alipay_dict()
            else:
                params['digit_currency_inst'] = self.digit_currency_inst
        if self.trans_in_account_no:
            if hasattr(self.trans_in_account_no, 'to_alipay_dict'):
                params['trans_in_account_no'] = self.trans_in_account_no.to_alipay_dict()
            else:
                params['trans_in_account_no'] = self.trans_in_account_no
        if self.trans_in_account_type:
            if hasattr(self.trans_in_account_type, 'to_alipay_dict'):
                params['trans_in_account_type'] = self.trans_in_account_type.to_alipay_dict()
            else:
                params['trans_in_account_type'] = self.trans_in_account_type
        if self.trans_in_cert_no:
            if hasattr(self.trans_in_cert_no, 'to_alipay_dict'):
                params['trans_in_cert_no'] = self.trans_in_cert_no.to_alipay_dict()
            else:
                params['trans_in_cert_no'] = self.trans_in_cert_no
        if self.trans_in_cert_type:
            if hasattr(self.trans_in_cert_type, 'to_alipay_dict'):
                params['trans_in_cert_type'] = self.trans_in_cert_type.to_alipay_dict()
            else:
                params['trans_in_cert_type'] = self.trans_in_cert_type
        if self.trans_in_name:
            if hasattr(self.trans_in_name, 'to_alipay_dict'):
                params['trans_in_name'] = self.trans_in_name.to_alipay_dict()
            else:
                params['trans_in_name'] = self.trans_in_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IncomeDistributionTransInInfo()
        if 'allocate_rate' in d:
            o.allocate_rate = d['allocate_rate']
        if 'bank_branch_code' in d:
            o.bank_branch_code = d['bank_branch_code']
        if 'bank_branch_name' in d:
            o.bank_branch_name = d['bank_branch_name']
        if 'digit_currency_inst' in d:
            o.digit_currency_inst = d['digit_currency_inst']
        if 'trans_in_account_no' in d:
            o.trans_in_account_no = d['trans_in_account_no']
        if 'trans_in_account_type' in d:
            o.trans_in_account_type = d['trans_in_account_type']
        if 'trans_in_cert_no' in d:
            o.trans_in_cert_no = d['trans_in_cert_no']
        if 'trans_in_cert_type' in d:
            o.trans_in_cert_type = d['trans_in_cert_type']
        if 'trans_in_name' in d:
            o.trans_in_name = d['trans_in_name']
        return o


