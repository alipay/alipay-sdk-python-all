#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BalanceAccountDetail(object):

    def __init__(self):
        self._acs = None
        self._bank = None

    @property
    def acs(self):
        return self._acs

    @acs.setter
    def acs(self, value):
        self._acs = value
    @property
    def bank(self):
        return self._bank

    @bank.setter
    def bank(self, value):
        self._bank = value


    def to_alipay_dict(self):
        params = dict()
        if self.acs:
            if hasattr(self.acs, 'to_alipay_dict'):
                params['acs'] = self.acs.to_alipay_dict()
            else:
                params['acs'] = self.acs
        if self.bank:
            if hasattr(self.bank, 'to_alipay_dict'):
                params['bank'] = self.bank.to_alipay_dict()
            else:
                params['bank'] = self.bank
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BalanceAccountDetail()
        if 'acs' in d:
            o.acs = d['acs']
        if 'bank' in d:
            o.bank = d['bank']
        return o


