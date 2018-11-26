#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BankCardInfo(object):

    def __init__(self):
        self._bank_branch_name = None
        self._card_name = None
        self._card_no = None

    @property
    def bank_branch_name(self):
        return self._bank_branch_name

    @bank_branch_name.setter
    def bank_branch_name(self, value):
        self._bank_branch_name = value
    @property
    def card_name(self):
        return self._card_name

    @card_name.setter
    def card_name(self, value):
        self._card_name = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_branch_name:
            if hasattr(self.bank_branch_name, 'to_alipay_dict'):
                params['bank_branch_name'] = self.bank_branch_name.to_alipay_dict()
            else:
                params['bank_branch_name'] = self.bank_branch_name
        if self.card_name:
            if hasattr(self.card_name, 'to_alipay_dict'):
                params['card_name'] = self.card_name.to_alipay_dict()
            else:
                params['card_name'] = self.card_name
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BankCardInfo()
        if 'bank_branch_name' in d:
            o.bank_branch_name = d['bank_branch_name']
        if 'card_name' in d:
            o.card_name = d['card_name']
        if 'card_no' in d:
            o.card_no = d['card_no']
        return o


