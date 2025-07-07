#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccountBaselDTO(object):

    def __init__(self):
        self._account_id = None
        self._account_name = None
        self._account_status = None
        self._agreement_no = None
        self._available_balance = None
        self._freeze_balance = None
        self._profit_status = None
        self._yesterday_profit = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_status(self):
        return self._account_status

    @account_status.setter
    def account_status(self, value):
        self._account_status = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def available_balance(self):
        return self._available_balance

    @available_balance.setter
    def available_balance(self, value):
        self._available_balance = value
    @property
    def freeze_balance(self):
        return self._freeze_balance

    @freeze_balance.setter
    def freeze_balance(self, value):
        self._freeze_balance = value
    @property
    def profit_status(self):
        return self._profit_status

    @profit_status.setter
    def profit_status(self, value):
        self._profit_status = value
    @property
    def yesterday_profit(self):
        return self._yesterday_profit

    @yesterday_profit.setter
    def yesterday_profit(self, value):
        self._yesterday_profit = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_status:
            if hasattr(self.account_status, 'to_alipay_dict'):
                params['account_status'] = self.account_status.to_alipay_dict()
            else:
                params['account_status'] = self.account_status
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.available_balance:
            if hasattr(self.available_balance, 'to_alipay_dict'):
                params['available_balance'] = self.available_balance.to_alipay_dict()
            else:
                params['available_balance'] = self.available_balance
        if self.freeze_balance:
            if hasattr(self.freeze_balance, 'to_alipay_dict'):
                params['freeze_balance'] = self.freeze_balance.to_alipay_dict()
            else:
                params['freeze_balance'] = self.freeze_balance
        if self.profit_status:
            if hasattr(self.profit_status, 'to_alipay_dict'):
                params['profit_status'] = self.profit_status.to_alipay_dict()
            else:
                params['profit_status'] = self.profit_status
        if self.yesterday_profit:
            if hasattr(self.yesterday_profit, 'to_alipay_dict'):
                params['yesterday_profit'] = self.yesterday_profit.to_alipay_dict()
            else:
                params['yesterday_profit'] = self.yesterday_profit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccountBaselDTO()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_status' in d:
            o.account_status = d['account_status']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'available_balance' in d:
            o.available_balance = d['available_balance']
        if 'freeze_balance' in d:
            o.freeze_balance = d['freeze_balance']
        if 'profit_status' in d:
            o.profit_status = d['profit_status']
        if 'yesterday_profit' in d:
            o.yesterday_profit = d['yesterday_profit']
        return o


