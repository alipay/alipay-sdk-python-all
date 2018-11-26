#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LoanTerm import LoanTerm


class BaseLoanApplyVO(object):

    def __init__(self):
        self._apply_amt = None
        self._apply_date = None
        self._apply_receipt_no = None
        self._loan_term = None
        self._status = None

    @property
    def apply_amt(self):
        return self._apply_amt

    @apply_amt.setter
    def apply_amt(self, value):
        self._apply_amt = value
    @property
    def apply_date(self):
        return self._apply_date

    @apply_date.setter
    def apply_date(self, value):
        self._apply_date = value
    @property
    def apply_receipt_no(self):
        return self._apply_receipt_no

    @apply_receipt_no.setter
    def apply_receipt_no(self, value):
        self._apply_receipt_no = value
    @property
    def loan_term(self):
        return self._loan_term

    @loan_term.setter
    def loan_term(self, value):
        if isinstance(value, LoanTerm):
            self._loan_term = value
        else:
            self._loan_term = LoanTerm.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_amt:
            if hasattr(self.apply_amt, 'to_alipay_dict'):
                params['apply_amt'] = self.apply_amt.to_alipay_dict()
            else:
                params['apply_amt'] = self.apply_amt
        if self.apply_date:
            if hasattr(self.apply_date, 'to_alipay_dict'):
                params['apply_date'] = self.apply_date.to_alipay_dict()
            else:
                params['apply_date'] = self.apply_date
        if self.apply_receipt_no:
            if hasattr(self.apply_receipt_no, 'to_alipay_dict'):
                params['apply_receipt_no'] = self.apply_receipt_no.to_alipay_dict()
            else:
                params['apply_receipt_no'] = self.apply_receipt_no
        if self.loan_term:
            if hasattr(self.loan_term, 'to_alipay_dict'):
                params['loan_term'] = self.loan_term.to_alipay_dict()
            else:
                params['loan_term'] = self.loan_term
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
        o = BaseLoanApplyVO()
        if 'apply_amt' in d:
            o.apply_amt = d['apply_amt']
        if 'apply_date' in d:
            o.apply_date = d['apply_date']
        if 'apply_receipt_no' in d:
            o.apply_receipt_no = d['apply_receipt_no']
        if 'loan_term' in d:
            o.loan_term = d['loan_term']
        if 'status' in d:
            o.status = d['status']
        return o


