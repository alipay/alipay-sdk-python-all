#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LoanTerm import LoanTerm


class AlipayPcreditLoanBudgetQueryModel(object):

    def __init__(self):
        self._daily_risk_int_rate = None
        self._loan_amt = None
        self._loan_term = None
        self._out_request_no = None
        self._repay_day = None
        self._repay_mode = None

    @property
    def daily_risk_int_rate(self):
        return self._daily_risk_int_rate

    @daily_risk_int_rate.setter
    def daily_risk_int_rate(self, value):
        self._daily_risk_int_rate = value
    @property
    def loan_amt(self):
        return self._loan_amt

    @loan_amt.setter
    def loan_amt(self, value):
        self._loan_amt = value
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
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def repay_day(self):
        return self._repay_day

    @repay_day.setter
    def repay_day(self, value):
        self._repay_day = value
    @property
    def repay_mode(self):
        return self._repay_mode

    @repay_mode.setter
    def repay_mode(self, value):
        self._repay_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.daily_risk_int_rate:
            if hasattr(self.daily_risk_int_rate, 'to_alipay_dict'):
                params['daily_risk_int_rate'] = self.daily_risk_int_rate.to_alipay_dict()
            else:
                params['daily_risk_int_rate'] = self.daily_risk_int_rate
        if self.loan_amt:
            if hasattr(self.loan_amt, 'to_alipay_dict'):
                params['loan_amt'] = self.loan_amt.to_alipay_dict()
            else:
                params['loan_amt'] = self.loan_amt
        if self.loan_term:
            if hasattr(self.loan_term, 'to_alipay_dict'):
                params['loan_term'] = self.loan_term.to_alipay_dict()
            else:
                params['loan_term'] = self.loan_term
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.repay_day:
            if hasattr(self.repay_day, 'to_alipay_dict'):
                params['repay_day'] = self.repay_day.to_alipay_dict()
            else:
                params['repay_day'] = self.repay_day
        if self.repay_mode:
            if hasattr(self.repay_mode, 'to_alipay_dict'):
                params['repay_mode'] = self.repay_mode.to_alipay_dict()
            else:
                params['repay_mode'] = self.repay_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditLoanBudgetQueryModel()
        if 'daily_risk_int_rate' in d:
            o.daily_risk_int_rate = d['daily_risk_int_rate']
        if 'loan_amt' in d:
            o.loan_amt = d['loan_amt']
        if 'loan_term' in d:
            o.loan_term = d['loan_term']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'repay_day' in d:
            o.repay_day = d['repay_day']
        if 'repay_mode' in d:
            o.repay_mode = d['repay_mode']
        return o


