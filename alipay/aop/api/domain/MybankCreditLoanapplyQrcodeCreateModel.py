#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoanapplyQrcodeCreateModel(object):

    def __init__(self):
        self._bank_card_category = None
        self._beneficiary_account = None
        self._beneficiary_name = None
        self._deposit_bank = None
        self._deposit_bank_cnaps_code = None
        self._head_bank_cnaps_code = None
        self._invalid_date = None
        self._order_amt = None
        self._order_no = None

    @property
    def bank_card_category(self):
        return self._bank_card_category

    @bank_card_category.setter
    def bank_card_category(self, value):
        self._bank_card_category = value
    @property
    def beneficiary_account(self):
        return self._beneficiary_account

    @beneficiary_account.setter
    def beneficiary_account(self, value):
        self._beneficiary_account = value
    @property
    def beneficiary_name(self):
        return self._beneficiary_name

    @beneficiary_name.setter
    def beneficiary_name(self, value):
        self._beneficiary_name = value
    @property
    def deposit_bank(self):
        return self._deposit_bank

    @deposit_bank.setter
    def deposit_bank(self, value):
        self._deposit_bank = value
    @property
    def deposit_bank_cnaps_code(self):
        return self._deposit_bank_cnaps_code

    @deposit_bank_cnaps_code.setter
    def deposit_bank_cnaps_code(self, value):
        self._deposit_bank_cnaps_code = value
    @property
    def head_bank_cnaps_code(self):
        return self._head_bank_cnaps_code

    @head_bank_cnaps_code.setter
    def head_bank_cnaps_code(self, value):
        self._head_bank_cnaps_code = value
    @property
    def invalid_date(self):
        return self._invalid_date

    @invalid_date.setter
    def invalid_date(self, value):
        self._invalid_date = value
    @property
    def order_amt(self):
        return self._order_amt

    @order_amt.setter
    def order_amt(self, value):
        self._order_amt = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_card_category:
            if hasattr(self.bank_card_category, 'to_alipay_dict'):
                params['bank_card_category'] = self.bank_card_category.to_alipay_dict()
            else:
                params['bank_card_category'] = self.bank_card_category
        if self.beneficiary_account:
            if hasattr(self.beneficiary_account, 'to_alipay_dict'):
                params['beneficiary_account'] = self.beneficiary_account.to_alipay_dict()
            else:
                params['beneficiary_account'] = self.beneficiary_account
        if self.beneficiary_name:
            if hasattr(self.beneficiary_name, 'to_alipay_dict'):
                params['beneficiary_name'] = self.beneficiary_name.to_alipay_dict()
            else:
                params['beneficiary_name'] = self.beneficiary_name
        if self.deposit_bank:
            if hasattr(self.deposit_bank, 'to_alipay_dict'):
                params['deposit_bank'] = self.deposit_bank.to_alipay_dict()
            else:
                params['deposit_bank'] = self.deposit_bank
        if self.deposit_bank_cnaps_code:
            if hasattr(self.deposit_bank_cnaps_code, 'to_alipay_dict'):
                params['deposit_bank_cnaps_code'] = self.deposit_bank_cnaps_code.to_alipay_dict()
            else:
                params['deposit_bank_cnaps_code'] = self.deposit_bank_cnaps_code
        if self.head_bank_cnaps_code:
            if hasattr(self.head_bank_cnaps_code, 'to_alipay_dict'):
                params['head_bank_cnaps_code'] = self.head_bank_cnaps_code.to_alipay_dict()
            else:
                params['head_bank_cnaps_code'] = self.head_bank_cnaps_code
        if self.invalid_date:
            if hasattr(self.invalid_date, 'to_alipay_dict'):
                params['invalid_date'] = self.invalid_date.to_alipay_dict()
            else:
                params['invalid_date'] = self.invalid_date
        if self.order_amt:
            if hasattr(self.order_amt, 'to_alipay_dict'):
                params['order_amt'] = self.order_amt.to_alipay_dict()
            else:
                params['order_amt'] = self.order_amt
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoanapplyQrcodeCreateModel()
        if 'bank_card_category' in d:
            o.bank_card_category = d['bank_card_category']
        if 'beneficiary_account' in d:
            o.beneficiary_account = d['beneficiary_account']
        if 'beneficiary_name' in d:
            o.beneficiary_name = d['beneficiary_name']
        if 'deposit_bank' in d:
            o.deposit_bank = d['deposit_bank']
        if 'deposit_bank_cnaps_code' in d:
            o.deposit_bank_cnaps_code = d['deposit_bank_cnaps_code']
        if 'head_bank_cnaps_code' in d:
            o.head_bank_cnaps_code = d['head_bank_cnaps_code']
        if 'invalid_date' in d:
            o.invalid_date = d['invalid_date']
        if 'order_amt' in d:
            o.order_amt = d['order_amt']
        if 'order_no' in d:
            o.order_no = d['order_no']
        return o


