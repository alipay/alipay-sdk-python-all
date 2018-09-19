#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LoanScheme(object):

    def __init__(self):
        self._credit_expire_date = None
        self._credit_lmt_amt = None
        self._credit_no = None
        self._credit_source = None
        self._credit_start_date = None
        self._int_rate = None
        self._loan_policy_code = None
        self._loan_term = None
        self._loan_term_unit = None
        self._loanable_amt = None
        self._repay_day = None
        self._repay_mode = None
        self._sale_pd_code = None
        self._sale_pd_version = None

    @property
    def credit_expire_date(self):
        return self._credit_expire_date

    @credit_expire_date.setter
    def credit_expire_date(self, value):
        self._credit_expire_date = value
    @property
    def credit_lmt_amt(self):
        return self._credit_lmt_amt

    @credit_lmt_amt.setter
    def credit_lmt_amt(self, value):
        self._credit_lmt_amt = value
    @property
    def credit_no(self):
        return self._credit_no

    @credit_no.setter
    def credit_no(self, value):
        self._credit_no = value
    @property
    def credit_source(self):
        return self._credit_source

    @credit_source.setter
    def credit_source(self, value):
        self._credit_source = value
    @property
    def credit_start_date(self):
        return self._credit_start_date

    @credit_start_date.setter
    def credit_start_date(self, value):
        self._credit_start_date = value
    @property
    def int_rate(self):
        return self._int_rate

    @int_rate.setter
    def int_rate(self, value):
        self._int_rate = value
    @property
    def loan_policy_code(self):
        return self._loan_policy_code

    @loan_policy_code.setter
    def loan_policy_code(self, value):
        self._loan_policy_code = value
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
    def loanable_amt(self):
        return self._loanable_amt

    @loanable_amt.setter
    def loanable_amt(self, value):
        self._loanable_amt = value
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
    @property
    def sale_pd_code(self):
        return self._sale_pd_code

    @sale_pd_code.setter
    def sale_pd_code(self, value):
        self._sale_pd_code = value
    @property
    def sale_pd_version(self):
        return self._sale_pd_version

    @sale_pd_version.setter
    def sale_pd_version(self, value):
        self._sale_pd_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_expire_date:
            if hasattr(self.credit_expire_date, 'to_alipay_dict'):
                params['credit_expire_date'] = self.credit_expire_date.to_alipay_dict()
            else:
                params['credit_expire_date'] = self.credit_expire_date
        if self.credit_lmt_amt:
            if hasattr(self.credit_lmt_amt, 'to_alipay_dict'):
                params['credit_lmt_amt'] = self.credit_lmt_amt.to_alipay_dict()
            else:
                params['credit_lmt_amt'] = self.credit_lmt_amt
        if self.credit_no:
            if hasattr(self.credit_no, 'to_alipay_dict'):
                params['credit_no'] = self.credit_no.to_alipay_dict()
            else:
                params['credit_no'] = self.credit_no
        if self.credit_source:
            if hasattr(self.credit_source, 'to_alipay_dict'):
                params['credit_source'] = self.credit_source.to_alipay_dict()
            else:
                params['credit_source'] = self.credit_source
        if self.credit_start_date:
            if hasattr(self.credit_start_date, 'to_alipay_dict'):
                params['credit_start_date'] = self.credit_start_date.to_alipay_dict()
            else:
                params['credit_start_date'] = self.credit_start_date
        if self.int_rate:
            if hasattr(self.int_rate, 'to_alipay_dict'):
                params['int_rate'] = self.int_rate.to_alipay_dict()
            else:
                params['int_rate'] = self.int_rate
        if self.loan_policy_code:
            if hasattr(self.loan_policy_code, 'to_alipay_dict'):
                params['loan_policy_code'] = self.loan_policy_code.to_alipay_dict()
            else:
                params['loan_policy_code'] = self.loan_policy_code
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
        if self.loanable_amt:
            if hasattr(self.loanable_amt, 'to_alipay_dict'):
                params['loanable_amt'] = self.loanable_amt.to_alipay_dict()
            else:
                params['loanable_amt'] = self.loanable_amt
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
        if self.sale_pd_code:
            if hasattr(self.sale_pd_code, 'to_alipay_dict'):
                params['sale_pd_code'] = self.sale_pd_code.to_alipay_dict()
            else:
                params['sale_pd_code'] = self.sale_pd_code
        if self.sale_pd_version:
            if hasattr(self.sale_pd_version, 'to_alipay_dict'):
                params['sale_pd_version'] = self.sale_pd_version.to_alipay_dict()
            else:
                params['sale_pd_version'] = self.sale_pd_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LoanScheme()
        if 'credit_expire_date' in d:
            o.credit_expire_date = d['credit_expire_date']
        if 'credit_lmt_amt' in d:
            o.credit_lmt_amt = d['credit_lmt_amt']
        if 'credit_no' in d:
            o.credit_no = d['credit_no']
        if 'credit_source' in d:
            o.credit_source = d['credit_source']
        if 'credit_start_date' in d:
            o.credit_start_date = d['credit_start_date']
        if 'int_rate' in d:
            o.int_rate = d['int_rate']
        if 'loan_policy_code' in d:
            o.loan_policy_code = d['loan_policy_code']
        if 'loan_term' in d:
            o.loan_term = d['loan_term']
        if 'loan_term_unit' in d:
            o.loan_term_unit = d['loan_term_unit']
        if 'loanable_amt' in d:
            o.loanable_amt = d['loanable_amt']
        if 'repay_day' in d:
            o.repay_day = d['repay_day']
        if 'repay_mode' in d:
            o.repay_mode = d['repay_mode']
        if 'sale_pd_code' in d:
            o.sale_pd_code = d['sale_pd_code']
        if 'sale_pd_version' in d:
            o.sale_pd_version = d['sale_pd_version']
        return o


