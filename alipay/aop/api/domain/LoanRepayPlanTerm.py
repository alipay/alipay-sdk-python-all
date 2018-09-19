#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LoanMoneyTypeAmt import LoanMoneyTypeAmt
from alipay.aop.api.domain.LoanMoneyTypeAmt import LoanMoneyTypeAmt
from alipay.aop.api.domain.LoanMoneyTypeAmt import LoanMoneyTypeAmt


class LoanRepayPlanTerm(object):

    def __init__(self):
        self._current_term = None
        self._paid_amt = None
        self._remain_amt = None
        self._status = None
        self._term_end_date = None
        self._term_no = None
        self._term_start_date = None
        self._total_amt = None

    @property
    def current_term(self):
        return self._current_term

    @current_term.setter
    def current_term(self, value):
        self._current_term = value
    @property
    def paid_amt(self):
        return self._paid_amt

    @paid_amt.setter
    def paid_amt(self, value):
        if isinstance(value, LoanMoneyTypeAmt):
            self._paid_amt = value
        else:
            self._paid_amt = LoanMoneyTypeAmt.from_alipay_dict(value)
    @property
    def remain_amt(self):
        return self._remain_amt

    @remain_amt.setter
    def remain_amt(self, value):
        if isinstance(value, LoanMoneyTypeAmt):
            self._remain_amt = value
        else:
            self._remain_amt = LoanMoneyTypeAmt.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def term_end_date(self):
        return self._term_end_date

    @term_end_date.setter
    def term_end_date(self, value):
        self._term_end_date = value
    @property
    def term_no(self):
        return self._term_no

    @term_no.setter
    def term_no(self, value):
        self._term_no = value
    @property
    def term_start_date(self):
        return self._term_start_date

    @term_start_date.setter
    def term_start_date(self, value):
        self._term_start_date = value
    @property
    def total_amt(self):
        return self._total_amt

    @total_amt.setter
    def total_amt(self, value):
        if isinstance(value, LoanMoneyTypeAmt):
            self._total_amt = value
        else:
            self._total_amt = LoanMoneyTypeAmt.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.current_term:
            if hasattr(self.current_term, 'to_alipay_dict'):
                params['current_term'] = self.current_term.to_alipay_dict()
            else:
                params['current_term'] = self.current_term
        if self.paid_amt:
            if hasattr(self.paid_amt, 'to_alipay_dict'):
                params['paid_amt'] = self.paid_amt.to_alipay_dict()
            else:
                params['paid_amt'] = self.paid_amt
        if self.remain_amt:
            if hasattr(self.remain_amt, 'to_alipay_dict'):
                params['remain_amt'] = self.remain_amt.to_alipay_dict()
            else:
                params['remain_amt'] = self.remain_amt
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.term_end_date:
            if hasattr(self.term_end_date, 'to_alipay_dict'):
                params['term_end_date'] = self.term_end_date.to_alipay_dict()
            else:
                params['term_end_date'] = self.term_end_date
        if self.term_no:
            if hasattr(self.term_no, 'to_alipay_dict'):
                params['term_no'] = self.term_no.to_alipay_dict()
            else:
                params['term_no'] = self.term_no
        if self.term_start_date:
            if hasattr(self.term_start_date, 'to_alipay_dict'):
                params['term_start_date'] = self.term_start_date.to_alipay_dict()
            else:
                params['term_start_date'] = self.term_start_date
        if self.total_amt:
            if hasattr(self.total_amt, 'to_alipay_dict'):
                params['total_amt'] = self.total_amt.to_alipay_dict()
            else:
                params['total_amt'] = self.total_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LoanRepayPlanTerm()
        if 'current_term' in d:
            o.current_term = d['current_term']
        if 'paid_amt' in d:
            o.paid_amt = d['paid_amt']
        if 'remain_amt' in d:
            o.remain_amt = d['remain_amt']
        if 'status' in d:
            o.status = d['status']
        if 'term_end_date' in d:
            o.term_end_date = d['term_end_date']
        if 'term_no' in d:
            o.term_no = d['term_no']
        if 'term_start_date' in d:
            o.term_start_date = d['term_start_date']
        if 'total_amt' in d:
            o.total_amt = d['total_amt']
        return o


