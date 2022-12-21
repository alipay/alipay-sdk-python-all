#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardSubAccountResult(object):

    def __init__(self):
        self._account_belong = None
        self._account_no = None
        self._amount = None
        self._batch_id = None
        self._denomination = None
        self._effective_date = None
        self._recharge_no = None
        self._sub_account_no = None
        self._user_id = None
        self._validate_date = None

    @property
    def account_belong(self):
        return self._account_belong

    @account_belong.setter
    def account_belong(self, value):
        self._account_belong = value
    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def denomination(self):
        return self._denomination

    @denomination.setter
    def denomination(self, value):
        self._denomination = value
    @property
    def effective_date(self):
        return self._effective_date

    @effective_date.setter
    def effective_date(self, value):
        self._effective_date = value
    @property
    def recharge_no(self):
        return self._recharge_no

    @recharge_no.setter
    def recharge_no(self, value):
        self._recharge_no = value
    @property
    def sub_account_no(self):
        return self._sub_account_no

    @sub_account_no.setter
    def sub_account_no(self, value):
        self._sub_account_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def validate_date(self):
        return self._validate_date

    @validate_date.setter
    def validate_date(self, value):
        self._validate_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_belong:
            if hasattr(self.account_belong, 'to_alipay_dict'):
                params['account_belong'] = self.account_belong.to_alipay_dict()
            else:
                params['account_belong'] = self.account_belong
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        if self.denomination:
            if hasattr(self.denomination, 'to_alipay_dict'):
                params['denomination'] = self.denomination.to_alipay_dict()
            else:
                params['denomination'] = self.denomination
        if self.effective_date:
            if hasattr(self.effective_date, 'to_alipay_dict'):
                params['effective_date'] = self.effective_date.to_alipay_dict()
            else:
                params['effective_date'] = self.effective_date
        if self.recharge_no:
            if hasattr(self.recharge_no, 'to_alipay_dict'):
                params['recharge_no'] = self.recharge_no.to_alipay_dict()
            else:
                params['recharge_no'] = self.recharge_no
        if self.sub_account_no:
            if hasattr(self.sub_account_no, 'to_alipay_dict'):
                params['sub_account_no'] = self.sub_account_no.to_alipay_dict()
            else:
                params['sub_account_no'] = self.sub_account_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.validate_date:
            if hasattr(self.validate_date, 'to_alipay_dict'):
                params['validate_date'] = self.validate_date.to_alipay_dict()
            else:
                params['validate_date'] = self.validate_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardSubAccountResult()
        if 'account_belong' in d:
            o.account_belong = d['account_belong']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'amount' in d:
            o.amount = d['amount']
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'denomination' in d:
            o.denomination = d['denomination']
        if 'effective_date' in d:
            o.effective_date = d['effective_date']
        if 'recharge_no' in d:
            o.recharge_no = d['recharge_no']
        if 'sub_account_no' in d:
            o.sub_account_no = d['sub_account_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'validate_date' in d:
            o.validate_date = d['validate_date']
        return o


