#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LoanTerm import LoanTerm


class AlipayPcreditLoanLoanApplyModel(object):

    def __init__(self):
        self._apply_amt = None
        self._back_url = None
        self._loan_purpose = None
        self._loan_term = None
        self._out_biz_no = None
        self._out_request_no = None
        self._repay_mode = None

    @property
    def apply_amt(self):
        return self._apply_amt

    @apply_amt.setter
    def apply_amt(self, value):
        self._apply_amt = value
    @property
    def back_url(self):
        return self._back_url

    @back_url.setter
    def back_url(self, value):
        self._back_url = value
    @property
    def loan_purpose(self):
        return self._loan_purpose

    @loan_purpose.setter
    def loan_purpose(self, value):
        self._loan_purpose = value
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
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def repay_mode(self):
        return self._repay_mode

    @repay_mode.setter
    def repay_mode(self, value):
        self._repay_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_amt:
            if hasattr(self.apply_amt, 'to_alipay_dict'):
                params['apply_amt'] = self.apply_amt.to_alipay_dict()
            else:
                params['apply_amt'] = self.apply_amt
        if self.back_url:
            if hasattr(self.back_url, 'to_alipay_dict'):
                params['back_url'] = self.back_url.to_alipay_dict()
            else:
                params['back_url'] = self.back_url
        if self.loan_purpose:
            if hasattr(self.loan_purpose, 'to_alipay_dict'):
                params['loan_purpose'] = self.loan_purpose.to_alipay_dict()
            else:
                params['loan_purpose'] = self.loan_purpose
        if self.loan_term:
            if hasattr(self.loan_term, 'to_alipay_dict'):
                params['loan_term'] = self.loan_term.to_alipay_dict()
            else:
                params['loan_term'] = self.loan_term
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
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
        o = AlipayPcreditLoanLoanApplyModel()
        if 'apply_amt' in d:
            o.apply_amt = d['apply_amt']
        if 'back_url' in d:
            o.back_url = d['back_url']
        if 'loan_purpose' in d:
            o.loan_purpose = d['loan_purpose']
        if 'loan_term' in d:
            o.loan_term = d['loan_term']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'repay_mode' in d:
            o.repay_mode = d['repay_mode']
        return o


