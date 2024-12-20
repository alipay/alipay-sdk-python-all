#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentPayBankInfo(object):

    def __init__(self):
        self._rent_acct_name = None
        self._rent_bank_code = None
        self._rent_bank_name = None
        self._rent_card_num = None

    @property
    def rent_acct_name(self):
        return self._rent_acct_name

    @rent_acct_name.setter
    def rent_acct_name(self, value):
        self._rent_acct_name = value
    @property
    def rent_bank_code(self):
        return self._rent_bank_code

    @rent_bank_code.setter
    def rent_bank_code(self, value):
        self._rent_bank_code = value
    @property
    def rent_bank_name(self):
        return self._rent_bank_name

    @rent_bank_name.setter
    def rent_bank_name(self, value):
        self._rent_bank_name = value
    @property
    def rent_card_num(self):
        return self._rent_card_num

    @rent_card_num.setter
    def rent_card_num(self, value):
        self._rent_card_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.rent_acct_name:
            if hasattr(self.rent_acct_name, 'to_alipay_dict'):
                params['rent_acct_name'] = self.rent_acct_name.to_alipay_dict()
            else:
                params['rent_acct_name'] = self.rent_acct_name
        if self.rent_bank_code:
            if hasattr(self.rent_bank_code, 'to_alipay_dict'):
                params['rent_bank_code'] = self.rent_bank_code.to_alipay_dict()
            else:
                params['rent_bank_code'] = self.rent_bank_code
        if self.rent_bank_name:
            if hasattr(self.rent_bank_name, 'to_alipay_dict'):
                params['rent_bank_name'] = self.rent_bank_name.to_alipay_dict()
            else:
                params['rent_bank_name'] = self.rent_bank_name
        if self.rent_card_num:
            if hasattr(self.rent_card_num, 'to_alipay_dict'):
                params['rent_card_num'] = self.rent_card_num.to_alipay_dict()
            else:
                params['rent_card_num'] = self.rent_card_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentPayBankInfo()
        if 'rent_acct_name' in d:
            o.rent_acct_name = d['rent_acct_name']
        if 'rent_bank_code' in d:
            o.rent_bank_code = d['rent_bank_code']
        if 'rent_bank_name' in d:
            o.rent_bank_name = d['rent_bank_name']
        if 'rent_card_num' in d:
            o.rent_card_num = d['rent_card_num']
        return o


