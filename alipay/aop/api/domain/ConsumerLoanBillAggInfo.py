#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsumerLoanBillAggInfo(object):

    def __init__(self):
        self._current_repay_amount = None
        self._expanditure_publish_date = None
        self._expire_days = None
        self._last_total_principal_amount = None
        self._next_repay_amount = None
        self._next_repay_date = None
        self._repay_date = None
        self._special_account = None
        self._status = None

    @property
    def current_repay_amount(self):
        return self._current_repay_amount

    @current_repay_amount.setter
    def current_repay_amount(self, value):
        self._current_repay_amount = value
    @property
    def expanditure_publish_date(self):
        return self._expanditure_publish_date

    @expanditure_publish_date.setter
    def expanditure_publish_date(self, value):
        self._expanditure_publish_date = value
    @property
    def expire_days(self):
        return self._expire_days

    @expire_days.setter
    def expire_days(self, value):
        self._expire_days = value
    @property
    def last_total_principal_amount(self):
        return self._last_total_principal_amount

    @last_total_principal_amount.setter
    def last_total_principal_amount(self, value):
        self._last_total_principal_amount = value
    @property
    def next_repay_amount(self):
        return self._next_repay_amount

    @next_repay_amount.setter
    def next_repay_amount(self, value):
        self._next_repay_amount = value
    @property
    def next_repay_date(self):
        return self._next_repay_date

    @next_repay_date.setter
    def next_repay_date(self, value):
        self._next_repay_date = value
    @property
    def repay_date(self):
        return self._repay_date

    @repay_date.setter
    def repay_date(self, value):
        self._repay_date = value
    @property
    def special_account(self):
        return self._special_account

    @special_account.setter
    def special_account(self, value):
        self._special_account = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_repay_amount:
            if hasattr(self.current_repay_amount, 'to_alipay_dict'):
                params['current_repay_amount'] = self.current_repay_amount.to_alipay_dict()
            else:
                params['current_repay_amount'] = self.current_repay_amount
        if self.expanditure_publish_date:
            if hasattr(self.expanditure_publish_date, 'to_alipay_dict'):
                params['expanditure_publish_date'] = self.expanditure_publish_date.to_alipay_dict()
            else:
                params['expanditure_publish_date'] = self.expanditure_publish_date
        if self.expire_days:
            if hasattr(self.expire_days, 'to_alipay_dict'):
                params['expire_days'] = self.expire_days.to_alipay_dict()
            else:
                params['expire_days'] = self.expire_days
        if self.last_total_principal_amount:
            if hasattr(self.last_total_principal_amount, 'to_alipay_dict'):
                params['last_total_principal_amount'] = self.last_total_principal_amount.to_alipay_dict()
            else:
                params['last_total_principal_amount'] = self.last_total_principal_amount
        if self.next_repay_amount:
            if hasattr(self.next_repay_amount, 'to_alipay_dict'):
                params['next_repay_amount'] = self.next_repay_amount.to_alipay_dict()
            else:
                params['next_repay_amount'] = self.next_repay_amount
        if self.next_repay_date:
            if hasattr(self.next_repay_date, 'to_alipay_dict'):
                params['next_repay_date'] = self.next_repay_date.to_alipay_dict()
            else:
                params['next_repay_date'] = self.next_repay_date
        if self.repay_date:
            if hasattr(self.repay_date, 'to_alipay_dict'):
                params['repay_date'] = self.repay_date.to_alipay_dict()
            else:
                params['repay_date'] = self.repay_date
        if self.special_account:
            if hasattr(self.special_account, 'to_alipay_dict'):
                params['special_account'] = self.special_account.to_alipay_dict()
            else:
                params['special_account'] = self.special_account
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsumerLoanBillAggInfo()
        if 'current_repay_amount' in d:
            o.current_repay_amount = d['current_repay_amount']
        if 'expanditure_publish_date' in d:
            o.expanditure_publish_date = d['expanditure_publish_date']
        if 'expire_days' in d:
            o.expire_days = d['expire_days']
        if 'last_total_principal_amount' in d:
            o.last_total_principal_amount = d['last_total_principal_amount']
        if 'next_repay_amount' in d:
            o.next_repay_amount = d['next_repay_amount']
        if 'next_repay_date' in d:
            o.next_repay_date = d['next_repay_date']
        if 'repay_date' in d:
            o.repay_date = d['repay_date']
        if 'special_account' in d:
            o.special_account = d['special_account']
        if 'status' in d:
            o.status = d['status']
        return o


