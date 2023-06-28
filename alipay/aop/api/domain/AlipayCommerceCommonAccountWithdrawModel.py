#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCommonAccountWithdrawModel(object):

    def __init__(self):
        self._account_book_id = None
        self._amount = None
        self._out_biz_no = None
        self._sign_user_id = None
        self._sign_user_open_id = None

    @property
    def account_book_id(self):
        return self._account_book_id

    @account_book_id.setter
    def account_book_id(self, value):
        self._account_book_id = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def sign_user_id(self):
        return self._sign_user_id

    @sign_user_id.setter
    def sign_user_id(self, value):
        self._sign_user_id = value
    @property
    def sign_user_open_id(self):
        return self._sign_user_open_id

    @sign_user_open_id.setter
    def sign_user_open_id(self, value):
        self._sign_user_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_book_id:
            if hasattr(self.account_book_id, 'to_alipay_dict'):
                params['account_book_id'] = self.account_book_id.to_alipay_dict()
            else:
                params['account_book_id'] = self.account_book_id
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.sign_user_id:
            if hasattr(self.sign_user_id, 'to_alipay_dict'):
                params['sign_user_id'] = self.sign_user_id.to_alipay_dict()
            else:
                params['sign_user_id'] = self.sign_user_id
        if self.sign_user_open_id:
            if hasattr(self.sign_user_open_id, 'to_alipay_dict'):
                params['sign_user_open_id'] = self.sign_user_open_id.to_alipay_dict()
            else:
                params['sign_user_open_id'] = self.sign_user_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCommonAccountWithdrawModel()
        if 'account_book_id' in d:
            o.account_book_id = d['account_book_id']
        if 'amount' in d:
            o.amount = d['amount']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'sign_user_id' in d:
            o.sign_user_id = d['sign_user_id']
        if 'sign_user_open_id' in d:
            o.sign_user_open_id = d['sign_user_open_id']
        return o


