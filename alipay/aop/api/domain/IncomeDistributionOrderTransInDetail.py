#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IncomeDistributionOrderTransInDetail(object):

    def __init__(self):
        self._amount = None
        self._trans_in_account_no = None
        self._trans_in_account_type = None
        self._trans_in_name = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def trans_in_account_no(self):
        return self._trans_in_account_no

    @trans_in_account_no.setter
    def trans_in_account_no(self, value):
        self._trans_in_account_no = value
    @property
    def trans_in_account_type(self):
        return self._trans_in_account_type

    @trans_in_account_type.setter
    def trans_in_account_type(self, value):
        self._trans_in_account_type = value
    @property
    def trans_in_name(self):
        return self._trans_in_name

    @trans_in_name.setter
    def trans_in_name(self, value):
        self._trans_in_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.trans_in_account_no:
            if hasattr(self.trans_in_account_no, 'to_alipay_dict'):
                params['trans_in_account_no'] = self.trans_in_account_no.to_alipay_dict()
            else:
                params['trans_in_account_no'] = self.trans_in_account_no
        if self.trans_in_account_type:
            if hasattr(self.trans_in_account_type, 'to_alipay_dict'):
                params['trans_in_account_type'] = self.trans_in_account_type.to_alipay_dict()
            else:
                params['trans_in_account_type'] = self.trans_in_account_type
        if self.trans_in_name:
            if hasattr(self.trans_in_name, 'to_alipay_dict'):
                params['trans_in_name'] = self.trans_in_name.to_alipay_dict()
            else:
                params['trans_in_name'] = self.trans_in_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IncomeDistributionOrderTransInDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'trans_in_account_no' in d:
            o.trans_in_account_no = d['trans_in_account_no']
        if 'trans_in_account_type' in d:
            o.trans_in_account_type = d['trans_in_account_type']
        if 'trans_in_name' in d:
            o.trans_in_name = d['trans_in_name']
        return o


