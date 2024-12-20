#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InstallmentVO(object):

    def __init__(self):
        self._accounting_date = None
        self._installment_end_date = None
        self._installment_no = None
        self._installment_start_date = None
        self._institution_loan_apply_no = None
        self._institution_loan_no = None
        self._loan_amount = None
        self._loan_apply_no = None
        self._loan_end_date = None
        self._loan_start_date = None
        self._repayment_method = None
        self._status = None
        self._total_installment_no = None
        self._unpaid_interest = None
        self._unpaid_penalty = None
        self._unpaid_principal = None
        self._unpaid_total_amount = None

    @property
    def accounting_date(self):
        return self._accounting_date

    @accounting_date.setter
    def accounting_date(self, value):
        self._accounting_date = value
    @property
    def installment_end_date(self):
        return self._installment_end_date

    @installment_end_date.setter
    def installment_end_date(self, value):
        self._installment_end_date = value
    @property
    def installment_no(self):
        return self._installment_no

    @installment_no.setter
    def installment_no(self, value):
        self._installment_no = value
    @property
    def installment_start_date(self):
        return self._installment_start_date

    @installment_start_date.setter
    def installment_start_date(self, value):
        self._installment_start_date = value
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
    def total_installment_no(self):
        return self._total_installment_no

    @total_installment_no.setter
    def total_installment_no(self, value):
        self._total_installment_no = value
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
    @property
    def unpaid_total_amount(self):
        return self._unpaid_total_amount

    @unpaid_total_amount.setter
    def unpaid_total_amount(self, value):
        self._unpaid_total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.accounting_date:
            if hasattr(self.accounting_date, 'to_alipay_dict'):
                params['accounting_date'] = self.accounting_date.to_alipay_dict()
            else:
                params['accounting_date'] = self.accounting_date
        if self.installment_end_date:
            if hasattr(self.installment_end_date, 'to_alipay_dict'):
                params['installment_end_date'] = self.installment_end_date.to_alipay_dict()
            else:
                params['installment_end_date'] = self.installment_end_date
        if self.installment_no:
            if hasattr(self.installment_no, 'to_alipay_dict'):
                params['installment_no'] = self.installment_no.to_alipay_dict()
            else:
                params['installment_no'] = self.installment_no
        if self.installment_start_date:
            if hasattr(self.installment_start_date, 'to_alipay_dict'):
                params['installment_start_date'] = self.installment_start_date.to_alipay_dict()
            else:
                params['installment_start_date'] = self.installment_start_date
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
        if self.total_installment_no:
            if hasattr(self.total_installment_no, 'to_alipay_dict'):
                params['total_installment_no'] = self.total_installment_no.to_alipay_dict()
            else:
                params['total_installment_no'] = self.total_installment_no
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
        if self.unpaid_total_amount:
            if hasattr(self.unpaid_total_amount, 'to_alipay_dict'):
                params['unpaid_total_amount'] = self.unpaid_total_amount.to_alipay_dict()
            else:
                params['unpaid_total_amount'] = self.unpaid_total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstallmentVO()
        if 'accounting_date' in d:
            o.accounting_date = d['accounting_date']
        if 'installment_end_date' in d:
            o.installment_end_date = d['installment_end_date']
        if 'installment_no' in d:
            o.installment_no = d['installment_no']
        if 'installment_start_date' in d:
            o.installment_start_date = d['installment_start_date']
        if 'institution_loan_apply_no' in d:
            o.institution_loan_apply_no = d['institution_loan_apply_no']
        if 'institution_loan_no' in d:
            o.institution_loan_no = d['institution_loan_no']
        if 'loan_amount' in d:
            o.loan_amount = d['loan_amount']
        if 'loan_apply_no' in d:
            o.loan_apply_no = d['loan_apply_no']
        if 'loan_end_date' in d:
            o.loan_end_date = d['loan_end_date']
        if 'loan_start_date' in d:
            o.loan_start_date = d['loan_start_date']
        if 'repayment_method' in d:
            o.repayment_method = d['repayment_method']
        if 'status' in d:
            o.status = d['status']
        if 'total_installment_no' in d:
            o.total_installment_no = d['total_installment_no']
        if 'unpaid_interest' in d:
            o.unpaid_interest = d['unpaid_interest']
        if 'unpaid_penalty' in d:
            o.unpaid_penalty = d['unpaid_penalty']
        if 'unpaid_principal' in d:
            o.unpaid_principal = d['unpaid_principal']
        if 'unpaid_total_amount' in d:
            o.unpaid_total_amount = d['unpaid_total_amount']
        return o


