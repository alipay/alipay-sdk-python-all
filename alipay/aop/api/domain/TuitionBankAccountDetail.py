#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TuitionUserName import TuitionUserName
from alipay.aop.api.domain.TuitionAddress import TuitionAddress


class TuitionBankAccountDetail(object):

    def __init__(self):
        self._bank_account_no = None
        self._bank_bic = None
        self._bank_name = None
        self._holder_account_name = None
        self._holder_address = None
        self._routing_number = None

    @property
    def bank_account_no(self):
        return self._bank_account_no

    @bank_account_no.setter
    def bank_account_no(self, value):
        self._bank_account_no = value
    @property
    def bank_bic(self):
        return self._bank_bic

    @bank_bic.setter
    def bank_bic(self, value):
        self._bank_bic = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def holder_account_name(self):
        return self._holder_account_name

    @holder_account_name.setter
    def holder_account_name(self, value):
        if isinstance(value, TuitionUserName):
            self._holder_account_name = value
        else:
            self._holder_account_name = TuitionUserName.from_alipay_dict(value)
    @property
    def holder_address(self):
        return self._holder_address

    @holder_address.setter
    def holder_address(self, value):
        if isinstance(value, TuitionAddress):
            self._holder_address = value
        else:
            self._holder_address = TuitionAddress.from_alipay_dict(value)
    @property
    def routing_number(self):
        return self._routing_number

    @routing_number.setter
    def routing_number(self, value):
        self._routing_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_account_no:
            if hasattr(self.bank_account_no, 'to_alipay_dict'):
                params['bank_account_no'] = self.bank_account_no.to_alipay_dict()
            else:
                params['bank_account_no'] = self.bank_account_no
        if self.bank_bic:
            if hasattr(self.bank_bic, 'to_alipay_dict'):
                params['bank_bic'] = self.bank_bic.to_alipay_dict()
            else:
                params['bank_bic'] = self.bank_bic
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.holder_account_name:
            if hasattr(self.holder_account_name, 'to_alipay_dict'):
                params['holder_account_name'] = self.holder_account_name.to_alipay_dict()
            else:
                params['holder_account_name'] = self.holder_account_name
        if self.holder_address:
            if hasattr(self.holder_address, 'to_alipay_dict'):
                params['holder_address'] = self.holder_address.to_alipay_dict()
            else:
                params['holder_address'] = self.holder_address
        if self.routing_number:
            if hasattr(self.routing_number, 'to_alipay_dict'):
                params['routing_number'] = self.routing_number.to_alipay_dict()
            else:
                params['routing_number'] = self.routing_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TuitionBankAccountDetail()
        if 'bank_account_no' in d:
            o.bank_account_no = d['bank_account_no']
        if 'bank_bic' in d:
            o.bank_bic = d['bank_bic']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'holder_account_name' in d:
            o.holder_account_name = d['holder_account_name']
        if 'holder_address' in d:
            o.holder_address = d['holder_address']
        if 'routing_number' in d:
            o.routing_number = d['routing_number']
        return o


