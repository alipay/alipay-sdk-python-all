#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcoDetailLoanInfo(object):

    def __init__(self):
        self._loan_amount = None
        self._memo = None
        self._trans_no = None
        self._trans_type = None

    @property
    def loan_amount(self):
        return self._loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        self._loan_amount = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def trans_no(self):
        return self._trans_no

    @trans_no.setter
    def trans_no(self, value):
        self._trans_no = value
    @property
    def trans_type(self):
        return self._trans_type

    @trans_type.setter
    def trans_type(self, value):
        self._trans_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.loan_amount:
            if hasattr(self.loan_amount, 'to_alipay_dict'):
                params['loan_amount'] = self.loan_amount.to_alipay_dict()
            else:
                params['loan_amount'] = self.loan_amount
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.trans_no:
            if hasattr(self.trans_no, 'to_alipay_dict'):
                params['trans_no'] = self.trans_no.to_alipay_dict()
            else:
                params['trans_no'] = self.trans_no
        if self.trans_type:
            if hasattr(self.trans_type, 'to_alipay_dict'):
                params['trans_type'] = self.trans_type.to_alipay_dict()
            else:
                params['trans_type'] = self.trans_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcoDetailLoanInfo()
        if 'loan_amount' in d:
            o.loan_amount = d['loan_amount']
        if 'memo' in d:
            o.memo = d['memo']
        if 'trans_no' in d:
            o.trans_no = d['trans_no']
        if 'trans_type' in d:
            o.trans_type = d['trans_type']
        return o


