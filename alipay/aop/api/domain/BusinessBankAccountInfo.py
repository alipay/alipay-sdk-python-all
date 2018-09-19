#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessBankAccountInfo(object):

    def __init__(self):
        self._business_bank_account_name = None
        self._business_bank_card_no = None
        self._business_bank_name = None
        self._business_bank_sub = None

    @property
    def business_bank_account_name(self):
        return self._business_bank_account_name

    @business_bank_account_name.setter
    def business_bank_account_name(self, value):
        self._business_bank_account_name = value
    @property
    def business_bank_card_no(self):
        return self._business_bank_card_no

    @business_bank_card_no.setter
    def business_bank_card_no(self, value):
        self._business_bank_card_no = value
    @property
    def business_bank_name(self):
        return self._business_bank_name

    @business_bank_name.setter
    def business_bank_name(self, value):
        self._business_bank_name = value
    @property
    def business_bank_sub(self):
        return self._business_bank_sub

    @business_bank_sub.setter
    def business_bank_sub(self, value):
        self._business_bank_sub = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_bank_account_name:
            if hasattr(self.business_bank_account_name, 'to_alipay_dict'):
                params['business_bank_account_name'] = self.business_bank_account_name.to_alipay_dict()
            else:
                params['business_bank_account_name'] = self.business_bank_account_name
        if self.business_bank_card_no:
            if hasattr(self.business_bank_card_no, 'to_alipay_dict'):
                params['business_bank_card_no'] = self.business_bank_card_no.to_alipay_dict()
            else:
                params['business_bank_card_no'] = self.business_bank_card_no
        if self.business_bank_name:
            if hasattr(self.business_bank_name, 'to_alipay_dict'):
                params['business_bank_name'] = self.business_bank_name.to_alipay_dict()
            else:
                params['business_bank_name'] = self.business_bank_name
        if self.business_bank_sub:
            if hasattr(self.business_bank_sub, 'to_alipay_dict'):
                params['business_bank_sub'] = self.business_bank_sub.to_alipay_dict()
            else:
                params['business_bank_sub'] = self.business_bank_sub
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessBankAccountInfo()
        if 'business_bank_account_name' in d:
            o.business_bank_account_name = d['business_bank_account_name']
        if 'business_bank_card_no' in d:
            o.business_bank_card_no = d['business_bank_card_no']
        if 'business_bank_name' in d:
            o.business_bank_name = d['business_bank_name']
        if 'business_bank_sub' in d:
            o.business_bank_sub = d['business_bank_sub']
        return o


