#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LoanApply(object):

    def __init__(self):
        self._apply_date = None
        self._apply_no = None
        self._bank_name = None
        self._capital_limit = None
        self._disburse_date = None
        self._due_date = None
        self._is_delinquent = None
        self._load_status = None
        self._loan_amount = None
        self._loan_cont_no = None
        self._loan_cont_rate = None
        self._out_biz_no = None

    @property
    def apply_date(self):
        return self._apply_date

    @apply_date.setter
    def apply_date(self, value):
        self._apply_date = value
    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def capital_limit(self):
        return self._capital_limit

    @capital_limit.setter
    def capital_limit(self, value):
        self._capital_limit = value
    @property
    def disburse_date(self):
        return self._disburse_date

    @disburse_date.setter
    def disburse_date(self, value):
        self._disburse_date = value
    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        self._due_date = value
    @property
    def is_delinquent(self):
        return self._is_delinquent

    @is_delinquent.setter
    def is_delinquent(self, value):
        self._is_delinquent = value
    @property
    def load_status(self):
        return self._load_status

    @load_status.setter
    def load_status(self, value):
        self._load_status = value
    @property
    def loan_amount(self):
        return self._loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        self._loan_amount = value
    @property
    def loan_cont_no(self):
        return self._loan_cont_no

    @loan_cont_no.setter
    def loan_cont_no(self, value):
        self._loan_cont_no = value
    @property
    def loan_cont_rate(self):
        return self._loan_cont_rate

    @loan_cont_rate.setter
    def loan_cont_rate(self, value):
        self._loan_cont_rate = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_date:
            if hasattr(self.apply_date, 'to_alipay_dict'):
                params['apply_date'] = self.apply_date.to_alipay_dict()
            else:
                params['apply_date'] = self.apply_date
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.capital_limit:
            if hasattr(self.capital_limit, 'to_alipay_dict'):
                params['capital_limit'] = self.capital_limit.to_alipay_dict()
            else:
                params['capital_limit'] = self.capital_limit
        if self.disburse_date:
            if hasattr(self.disburse_date, 'to_alipay_dict'):
                params['disburse_date'] = self.disburse_date.to_alipay_dict()
            else:
                params['disburse_date'] = self.disburse_date
        if self.due_date:
            if hasattr(self.due_date, 'to_alipay_dict'):
                params['due_date'] = self.due_date.to_alipay_dict()
            else:
                params['due_date'] = self.due_date
        if self.is_delinquent:
            if hasattr(self.is_delinquent, 'to_alipay_dict'):
                params['is_delinquent'] = self.is_delinquent.to_alipay_dict()
            else:
                params['is_delinquent'] = self.is_delinquent
        if self.load_status:
            if hasattr(self.load_status, 'to_alipay_dict'):
                params['load_status'] = self.load_status.to_alipay_dict()
            else:
                params['load_status'] = self.load_status
        if self.loan_amount:
            if hasattr(self.loan_amount, 'to_alipay_dict'):
                params['loan_amount'] = self.loan_amount.to_alipay_dict()
            else:
                params['loan_amount'] = self.loan_amount
        if self.loan_cont_no:
            if hasattr(self.loan_cont_no, 'to_alipay_dict'):
                params['loan_cont_no'] = self.loan_cont_no.to_alipay_dict()
            else:
                params['loan_cont_no'] = self.loan_cont_no
        if self.loan_cont_rate:
            if hasattr(self.loan_cont_rate, 'to_alipay_dict'):
                params['loan_cont_rate'] = self.loan_cont_rate.to_alipay_dict()
            else:
                params['loan_cont_rate'] = self.loan_cont_rate
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LoanApply()
        if 'apply_date' in d:
            o.apply_date = d['apply_date']
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'capital_limit' in d:
            o.capital_limit = d['capital_limit']
        if 'disburse_date' in d:
            o.disburse_date = d['disburse_date']
        if 'due_date' in d:
            o.due_date = d['due_date']
        if 'is_delinquent' in d:
            o.is_delinquent = d['is_delinquent']
        if 'load_status' in d:
            o.load_status = d['load_status']
        if 'loan_amount' in d:
            o.loan_amount = d['loan_amount']
        if 'loan_cont_no' in d:
            o.loan_cont_no = d['loan_cont_no']
        if 'loan_cont_rate' in d:
            o.loan_cont_rate = d['loan_cont_rate']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


