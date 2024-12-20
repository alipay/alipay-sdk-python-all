#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GrantBankCard(object):

    def __init__(self):
        self._bank_card_id = None
        self._bank_code = None
        self._bank_name = None
        self._show_card_no = None

    @property
    def bank_card_id(self):
        return self._bank_card_id

    @bank_card_id.setter
    def bank_card_id(self, value):
        self._bank_card_id = value
    @property
    def bank_code(self):
        return self._bank_code

    @bank_code.setter
    def bank_code(self, value):
        self._bank_code = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def show_card_no(self):
        return self._show_card_no

    @show_card_no.setter
    def show_card_no(self, value):
        self._show_card_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_card_id:
            if hasattr(self.bank_card_id, 'to_alipay_dict'):
                params['bank_card_id'] = self.bank_card_id.to_alipay_dict()
            else:
                params['bank_card_id'] = self.bank_card_id
        if self.bank_code:
            if hasattr(self.bank_code, 'to_alipay_dict'):
                params['bank_code'] = self.bank_code.to_alipay_dict()
            else:
                params['bank_code'] = self.bank_code
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.show_card_no:
            if hasattr(self.show_card_no, 'to_alipay_dict'):
                params['show_card_no'] = self.show_card_no.to_alipay_dict()
            else:
                params['show_card_no'] = self.show_card_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GrantBankCard()
        if 'bank_card_id' in d:
            o.bank_card_id = d['bank_card_id']
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'show_card_no' in d:
            o.show_card_no = d['show_card_no']
        return o


