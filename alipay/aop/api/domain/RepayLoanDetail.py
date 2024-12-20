#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RepayLoanDetail(object):

    def __init__(self):
        self._institution_loan_apply_no = None
        self._institution_loan_no = None
        self._loan_apply_no = None
        self._repaid_interest = None
        self._repaid_penalty = None
        self._repaid_principal = None
        self._repaid_time = None
        self._repaid_total_amount = None
        self._repay_detail_no = None

    @property
    def institution_loan_apply_no(self):
        return self._institution_loan_apply_no

    @institution_loan_apply_no.setter
    def institution_loan_apply_no(self, value):
        self._institution_loan_apply_no = value
    @property
    def institution_loan_no(self):
        return self._institution_loan_no

    @institution_loan_no.setter
    def institution_loan_no(self, value):
        self._institution_loan_no = value
    @property
    def loan_apply_no(self):
        return self._loan_apply_no

    @loan_apply_no.setter
    def loan_apply_no(self, value):
        self._loan_apply_no = value
    @property
    def repaid_interest(self):
        return self._repaid_interest

    @repaid_interest.setter
    def repaid_interest(self, value):
        self._repaid_interest = value
    @property
    def repaid_penalty(self):
        return self._repaid_penalty

    @repaid_penalty.setter
    def repaid_penalty(self, value):
        self._repaid_penalty = value
    @property
    def repaid_principal(self):
        return self._repaid_principal

    @repaid_principal.setter
    def repaid_principal(self, value):
        self._repaid_principal = value
    @property
    def repaid_time(self):
        return self._repaid_time

    @repaid_time.setter
    def repaid_time(self, value):
        self._repaid_time = value
    @property
    def repaid_total_amount(self):
        return self._repaid_total_amount

    @repaid_total_amount.setter
    def repaid_total_amount(self, value):
        self._repaid_total_amount = value
    @property
    def repay_detail_no(self):
        return self._repay_detail_no

    @repay_detail_no.setter
    def repay_detail_no(self, value):
        self._repay_detail_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.institution_loan_apply_no:
            if hasattr(self.institution_loan_apply_no, 'to_alipay_dict'):
                params['institution_loan_apply_no'] = self.institution_loan_apply_no.to_alipay_dict()
            else:
                params['institution_loan_apply_no'] = self.institution_loan_apply_no
        if self.institution_loan_no:
            if hasattr(self.institution_loan_no, 'to_alipay_dict'):
                params['institution_loan_no'] = self.institution_loan_no.to_alipay_dict()
            else:
                params['institution_loan_no'] = self.institution_loan_no
        if self.loan_apply_no:
            if hasattr(self.loan_apply_no, 'to_alipay_dict'):
                params['loan_apply_no'] = self.loan_apply_no.to_alipay_dict()
            else:
                params['loan_apply_no'] = self.loan_apply_no
        if self.repaid_interest:
            if hasattr(self.repaid_interest, 'to_alipay_dict'):
                params['repaid_interest'] = self.repaid_interest.to_alipay_dict()
            else:
                params['repaid_interest'] = self.repaid_interest
        if self.repaid_penalty:
            if hasattr(self.repaid_penalty, 'to_alipay_dict'):
                params['repaid_penalty'] = self.repaid_penalty.to_alipay_dict()
            else:
                params['repaid_penalty'] = self.repaid_penalty
        if self.repaid_principal:
            if hasattr(self.repaid_principal, 'to_alipay_dict'):
                params['repaid_principal'] = self.repaid_principal.to_alipay_dict()
            else:
                params['repaid_principal'] = self.repaid_principal
        if self.repaid_time:
            if hasattr(self.repaid_time, 'to_alipay_dict'):
                params['repaid_time'] = self.repaid_time.to_alipay_dict()
            else:
                params['repaid_time'] = self.repaid_time
        if self.repaid_total_amount:
            if hasattr(self.repaid_total_amount, 'to_alipay_dict'):
                params['repaid_total_amount'] = self.repaid_total_amount.to_alipay_dict()
            else:
                params['repaid_total_amount'] = self.repaid_total_amount
        if self.repay_detail_no:
            if hasattr(self.repay_detail_no, 'to_alipay_dict'):
                params['repay_detail_no'] = self.repay_detail_no.to_alipay_dict()
            else:
                params['repay_detail_no'] = self.repay_detail_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RepayLoanDetail()
        if 'institution_loan_apply_no' in d:
            o.institution_loan_apply_no = d['institution_loan_apply_no']
        if 'institution_loan_no' in d:
            o.institution_loan_no = d['institution_loan_no']
        if 'loan_apply_no' in d:
            o.loan_apply_no = d['loan_apply_no']
        if 'repaid_interest' in d:
            o.repaid_interest = d['repaid_interest']
        if 'repaid_penalty' in d:
            o.repaid_penalty = d['repaid_penalty']
        if 'repaid_principal' in d:
            o.repaid_principal = d['repaid_principal']
        if 'repaid_time' in d:
            o.repaid_time = d['repaid_time']
        if 'repaid_total_amount' in d:
            o.repaid_total_amount = d['repaid_total_amount']
        if 'repay_detail_no' in d:
            o.repay_detail_no = d['repay_detail_no']
        return o


