#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAccountInstfundWithdrawApplyModel(object):

    def __init__(self):
        self._bank_card_name = None
        self._bank_card_no = None
        self._bank_code = None
        self._debit_account_no = None
        self._debit_amount = None
        self._debit_currency = None
        self._debit_user_id = None
        self._memo = None
        self._out_biz_no = None

    @property
    def bank_card_name(self):
        return self._bank_card_name

    @bank_card_name.setter
    def bank_card_name(self, value):
        self._bank_card_name = value
    @property
    def bank_card_no(self):
        return self._bank_card_no

    @bank_card_no.setter
    def bank_card_no(self, value):
        self._bank_card_no = value
    @property
    def bank_code(self):
        return self._bank_code

    @bank_code.setter
    def bank_code(self, value):
        self._bank_code = value
    @property
    def debit_account_no(self):
        return self._debit_account_no

    @debit_account_no.setter
    def debit_account_no(self, value):
        self._debit_account_no = value
    @property
    def debit_amount(self):
        return self._debit_amount

    @debit_amount.setter
    def debit_amount(self, value):
        self._debit_amount = value
    @property
    def debit_currency(self):
        return self._debit_currency

    @debit_currency.setter
    def debit_currency(self, value):
        self._debit_currency = value
    @property
    def debit_user_id(self):
        return self._debit_user_id

    @debit_user_id.setter
    def debit_user_id(self, value):
        self._debit_user_id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_card_name:
            if hasattr(self.bank_card_name, 'to_alipay_dict'):
                params['bank_card_name'] = self.bank_card_name.to_alipay_dict()
            else:
                params['bank_card_name'] = self.bank_card_name
        if self.bank_card_no:
            if hasattr(self.bank_card_no, 'to_alipay_dict'):
                params['bank_card_no'] = self.bank_card_no.to_alipay_dict()
            else:
                params['bank_card_no'] = self.bank_card_no
        if self.bank_code:
            if hasattr(self.bank_code, 'to_alipay_dict'):
                params['bank_code'] = self.bank_code.to_alipay_dict()
            else:
                params['bank_code'] = self.bank_code
        if self.debit_account_no:
            if hasattr(self.debit_account_no, 'to_alipay_dict'):
                params['debit_account_no'] = self.debit_account_no.to_alipay_dict()
            else:
                params['debit_account_no'] = self.debit_account_no
        if self.debit_amount:
            if hasattr(self.debit_amount, 'to_alipay_dict'):
                params['debit_amount'] = self.debit_amount.to_alipay_dict()
            else:
                params['debit_amount'] = self.debit_amount
        if self.debit_currency:
            if hasattr(self.debit_currency, 'to_alipay_dict'):
                params['debit_currency'] = self.debit_currency.to_alipay_dict()
            else:
                params['debit_currency'] = self.debit_currency
        if self.debit_user_id:
            if hasattr(self.debit_user_id, 'to_alipay_dict'):
                params['debit_user_id'] = self.debit_user_id.to_alipay_dict()
            else:
                params['debit_user_id'] = self.debit_user_id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAccountInstfundWithdrawApplyModel()
        if 'bank_card_name' in d:
            o.bank_card_name = d['bank_card_name']
        if 'bank_card_no' in d:
            o.bank_card_no = d['bank_card_no']
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        if 'debit_account_no' in d:
            o.debit_account_no = d['debit_account_no']
        if 'debit_amount' in d:
            o.debit_amount = d['debit_amount']
        if 'debit_currency' in d:
            o.debit_currency = d['debit_currency']
        if 'debit_user_id' in d:
            o.debit_user_id = d['debit_user_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


