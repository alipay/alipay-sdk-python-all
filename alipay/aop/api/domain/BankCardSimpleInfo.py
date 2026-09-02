#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BankCardSimpleInfo(object):

    def __init__(self):
        self._bank_card_code = None
        self._bank_card_name = None
        self._bank_card_no = None

    @property
    def bank_card_code(self):
        return self._bank_card_code

    @bank_card_code.setter
    def bank_card_code(self, value):
        self._bank_card_code = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.bank_card_code:
            if hasattr(self.bank_card_code, 'to_alipay_dict'):
                params['bank_card_code'] = self.bank_card_code.to_alipay_dict()
            else:
                params['bank_card_code'] = self.bank_card_code
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BankCardSimpleInfo()
        if 'bank_card_code' in d:
            o.bank_card_code = d['bank_card_code']
        if 'bank_card_name' in d:
            o.bank_card_name = d['bank_card_name']
        if 'bank_card_no' in d:
            o.bank_card_no = d['bank_card_no']
        return o


