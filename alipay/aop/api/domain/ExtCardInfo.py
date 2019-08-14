#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExtCardInfo(object):

    def __init__(self):
        self._bank_acc_name = None
        self._card_bank = None
        self._card_branch = None
        self._card_deposit = None
        self._card_location = None
        self._card_no = None
        self._status = None

    @property
    def bank_acc_name(self):
        return self._bank_acc_name

    @bank_acc_name.setter
    def bank_acc_name(self, value):
        self._bank_acc_name = value
    @property
    def card_bank(self):
        return self._card_bank

    @card_bank.setter
    def card_bank(self, value):
        self._card_bank = value
    @property
    def card_branch(self):
        return self._card_branch

    @card_branch.setter
    def card_branch(self, value):
        self._card_branch = value
    @property
    def card_deposit(self):
        return self._card_deposit

    @card_deposit.setter
    def card_deposit(self, value):
        self._card_deposit = value
    @property
    def card_location(self):
        return self._card_location

    @card_location.setter
    def card_location(self, value):
        self._card_location = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_acc_name:
            if hasattr(self.bank_acc_name, 'to_alipay_dict'):
                params['bank_acc_name'] = self.bank_acc_name.to_alipay_dict()
            else:
                params['bank_acc_name'] = self.bank_acc_name
        if self.card_bank:
            if hasattr(self.card_bank, 'to_alipay_dict'):
                params['card_bank'] = self.card_bank.to_alipay_dict()
            else:
                params['card_bank'] = self.card_bank
        if self.card_branch:
            if hasattr(self.card_branch, 'to_alipay_dict'):
                params['card_branch'] = self.card_branch.to_alipay_dict()
            else:
                params['card_branch'] = self.card_branch
        if self.card_deposit:
            if hasattr(self.card_deposit, 'to_alipay_dict'):
                params['card_deposit'] = self.card_deposit.to_alipay_dict()
            else:
                params['card_deposit'] = self.card_deposit
        if self.card_location:
            if hasattr(self.card_location, 'to_alipay_dict'):
                params['card_location'] = self.card_location.to_alipay_dict()
            else:
                params['card_location'] = self.card_location
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
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
        o = ExtCardInfo()
        if 'bank_acc_name' in d:
            o.bank_acc_name = d['bank_acc_name']
        if 'card_bank' in d:
            o.card_bank = d['card_bank']
        if 'card_branch' in d:
            o.card_branch = d['card_branch']
        if 'card_deposit' in d:
            o.card_deposit = d['card_deposit']
        if 'card_location' in d:
            o.card_location = d['card_location']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'status' in d:
            o.status = d['status']
        return o


