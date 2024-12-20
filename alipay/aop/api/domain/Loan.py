#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Loan(object):

    def __init__(self):
        self._institution_loan_apply_no = None
        self._institution_loan_no = None
        self._interest_rate = None
        self._loan_amount = None
        self._loan_apply_no = None
        self._loan_end_date = None
        self._loan_start_date = None
        self._loan_term = None
        self._loan_term_unit = None
        self._repayment_day = None
        self._repayment_method = None
        self._status = None
        self._unpaid_installment_count = None
        self._unpaid_interest = None
        self._unpaid_penalty = None
        self._unpaid_principal = None

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
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        self._interest_rate = value
    @property
    def loan_amount(self):
        return self._loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        self._loan_amount = value
    @property
    def loan_apply_no(self):
        return self._loan_apply_no

    @loan_apply_no.setter
    def loan_apply_no(self, value):
        self._loan_apply_no = value
    @property
    def loan_end_date(self):
        return self._loan_end_date

    @loan_end_date.setter
    def loan_end_date(self, value):
        self._loan_end_date = value
    @property
    def loan_start_date(self):
        return self._loan_start_date

    @loan_start_date.setter
    def loan_start_date(self, value):
        self._loan_start_date = value
    @property
    def loan_term(self):
        return self._loan_term

    @loan_term.setter
    def loan_term(self, value):
        self._loan_term = value
    @property
    def loan_term_unit(self):
        return self._loan_term_unit

    @loan_term_unit.setter
    def loan_term_unit(self, value):
        self._loan_term_unit = value
    @property
    def repayment_day(self):
        return self._repayment_day

    @repayment_day.setter
    def repayment_day(self, value):
        self._repayment_day = value
    @property
    def repayment_method(self):
        return self._repayment_method

    @repayment_method.setter
    def repayment_method(self, value):
        self._repayment_method = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def unpaid_installment_count(self):
        return self._unpaid_installment_count

    @unpaid_installment_count.setter
    def unpaid_installment_count(self, value):
        self._unpaid_installment_count = value
    @property
    def unpaid_interest(self):
        return self._unpaid_interest

    @unpaid_interest.setter
    def unpaid_interest(self, value):
        self._unpaid_interest = value
    @property
    def unpaid_penalty(self):
        return self._unpaid_penalty

    @unpaid_penalty.setter
    def unpaid_penalty(self, value):
        self._unpaid_penalty = value
    @property
    def unpaid_principal(self):
        return self._unpaid_principal

    @unpaid_principal.setter
    def unpaid_principal(self, value):
        self._unpaid_principal = value


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
        if self.interest_rate:
            if hasattr(self.interest_rate, 'to_alipay_dict'):
                params['interest_rate'] = self.interest_rate.to_alipay_dict()
            else:
                params['interest_rate'] = self.interest_rate
        if self.loan_amount:
            if hasattr(self.loan_amount, 'to_alipay_dict'):
                params['loan_amount'] = self.loan_amount.to_alipay_dict()
            else:
                params['loan_amount'] = self.loan_amount
        if self.loan_apply_no:
            if hasattr(self.loan_apply_no, 'to_alipay_dict'):
                params['loan_apply_no'] = self.loan_apply_no.to_alipay_dict()
            else:
                params['loan_apply_no'] = self.loan_apply_no
        if self.loan_end_date:
            if hasattr(self.loan_end_date, 'to_alipay_dict'):
                params['loan_end_date'] = self.loan_end_date.to_alipay_dict()
            else:
                params['loan_end_date'] = self.loan_end_date
        if self.loan_start_date:
            if hasattr(self.loan_start_date, 'to_alipay_dict'):
                params['loan_start_date'] = self.loan_start_date.to_alipay_dict()
            else:
                params['loan_start_date'] = self.loan_start_date
        if self.loan_term:
            if hasattr(self.loan_term, 'to_alipay_dict'):
                params['loan_term'] = self.loan_term.to_alipay_dict()
            else:
                params['loan_term'] = self.loan_term
        if self.loan_term_unit:
            if hasattr(self.loan_term_unit, 'to_alipay_dict'):
                params['loan_term_unit'] = self.loan_term_unit.to_alipay_dict()
            else:
                params['loan_term_unit'] = self.loan_term_unit
        if self.repayment_day:
            if hasattr(self.repayment_day, 'to_alipay_dict'):
                params['repayment_day'] = self.repayment_day.to_alipay_dict()
            else:
                params['repayment_day'] = self.repayment_day
        if self.repayment_method:
            if hasattr(self.repayment_method, 'to_alipay_dict'):
                params['repayment_method'] = self.repayment_method.to_alipay_dict()
            else:
                params['repayment_method'] = self.repayment_method
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.unpaid_installment_count:
            if hasattr(self.unpaid_installment_count, 'to_alipay_dict'):
                params['unpaid_installment_count'] = self.unpaid_installment_count.to_alipay_dict()
            else:
                params['unpaid_installment_count'] = self.unpaid_installment_count
        if self.unpaid_interest:
            if hasattr(self.unpaid_interest, 'to_alipay_dict'):
                params['unpaid_interest'] = self.unpaid_interest.to_alipay_dict()
            else:
                params['unpaid_interest'] = self.unpaid_interest
        if self.unpaid_penalty:
            if hasattr(self.unpaid_penalty, 'to_alipay_dict'):
                params['unpaid_penalty'] = self.unpaid_penalty.to_alipay_dict()
            else:
                params['unpaid_penalty'] = self.unpaid_penalty
        if self.unpaid_principal:
            if hasattr(self.unpaid_principal, 'to_alipay_dict'):
                params['unpaid_principal'] = self.unpaid_principal.to_alipay_dict()
            else:
                params['unpaid_principal'] = self.unpaid_principal
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Loan()
        if 'institution_loan_apply_no' in d:
            o.institution_loan_apply_no = d['institution_loan_apply_no']
        if 'institution_loan_no' in d:
            o.institution_loan_no = d['institution_loan_no']
        if 'interest_rate' in d:
            o.interest_rate = d['interest_rate']
        if 'loan_amount' in d:
            o.loan_amount = d['loan_amount']
        if 'loan_apply_no' in d:
            o.loan_apply_no = d['loan_apply_no']
        if 'loan_end_date' in d:
            o.loan_end_date = d['loan_end_date']
        if 'loan_start_date' in d:
            o.loan_start_date = d['loan_start_date']
        if 'loan_term' in d:
            o.loan_term = d['loan_term']
        if 'loan_term_unit' in d:
            o.loan_term_unit = d['loan_term_unit']
        if 'repayment_day' in d:
            o.repayment_day = d['repayment_day']
        if 'repayment_method' in d:
            o.repayment_method = d['repayment_method']
        if 'status' in d:
            o.status = d['status']
        if 'unpaid_installment_count' in d:
            o.unpaid_installment_count = d['unpaid_installment_count']
        if 'unpaid_interest' in d:
            o.unpaid_interest = d['unpaid_interest']
        if 'unpaid_penalty' in d:
            o.unpaid_penalty = d['unpaid_penalty']
        if 'unpaid_principal' in d:
            o.unpaid_principal = d['unpaid_principal']
        return o


