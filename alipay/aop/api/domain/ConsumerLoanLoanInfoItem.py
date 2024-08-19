#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsumerLoanLoanInfoItem(object):

    def __init__(self):
        self._allowed_pay_off_early = None
        self._last_insurance_amount = None
        self._last_interest_amount = None
        self._last_penalty_interest_amount = None
        self._last_period_count = None
        self._last_principal_amount = None
        self._loan_amount = None
        self._loan_date = None
        self._loan_id = None
        self._repay_method = None
        self._select_type = None
        self._status = None

    @property
    def allowed_pay_off_early(self):
        return self._allowed_pay_off_early

    @allowed_pay_off_early.setter
    def allowed_pay_off_early(self, value):
        self._allowed_pay_off_early = value
    @property
    def last_insurance_amount(self):
        return self._last_insurance_amount

    @last_insurance_amount.setter
    def last_insurance_amount(self, value):
        self._last_insurance_amount = value
    @property
    def last_interest_amount(self):
        return self._last_interest_amount

    @last_interest_amount.setter
    def last_interest_amount(self, value):
        self._last_interest_amount = value
    @property
    def last_penalty_interest_amount(self):
        return self._last_penalty_interest_amount

    @last_penalty_interest_amount.setter
    def last_penalty_interest_amount(self, value):
        self._last_penalty_interest_amount = value
    @property
    def last_period_count(self):
        return self._last_period_count

    @last_period_count.setter
    def last_period_count(self, value):
        self._last_period_count = value
    @property
    def last_principal_amount(self):
        return self._last_principal_amount

    @last_principal_amount.setter
    def last_principal_amount(self, value):
        self._last_principal_amount = value
    @property
    def loan_amount(self):
        return self._loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        self._loan_amount = value
    @property
    def loan_date(self):
        return self._loan_date

    @loan_date.setter
    def loan_date(self, value):
        self._loan_date = value
    @property
    def loan_id(self):
        return self._loan_id

    @loan_id.setter
    def loan_id(self, value):
        self._loan_id = value
    @property
    def repay_method(self):
        return self._repay_method

    @repay_method.setter
    def repay_method(self, value):
        self._repay_method = value
    @property
    def select_type(self):
        return self._select_type

    @select_type.setter
    def select_type(self, value):
        self._select_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.allowed_pay_off_early:
            if hasattr(self.allowed_pay_off_early, 'to_alipay_dict'):
                params['allowed_pay_off_early'] = self.allowed_pay_off_early.to_alipay_dict()
            else:
                params['allowed_pay_off_early'] = self.allowed_pay_off_early
        if self.last_insurance_amount:
            if hasattr(self.last_insurance_amount, 'to_alipay_dict'):
                params['last_insurance_amount'] = self.last_insurance_amount.to_alipay_dict()
            else:
                params['last_insurance_amount'] = self.last_insurance_amount
        if self.last_interest_amount:
            if hasattr(self.last_interest_amount, 'to_alipay_dict'):
                params['last_interest_amount'] = self.last_interest_amount.to_alipay_dict()
            else:
                params['last_interest_amount'] = self.last_interest_amount
        if self.last_penalty_interest_amount:
            if hasattr(self.last_penalty_interest_amount, 'to_alipay_dict'):
                params['last_penalty_interest_amount'] = self.last_penalty_interest_amount.to_alipay_dict()
            else:
                params['last_penalty_interest_amount'] = self.last_penalty_interest_amount
        if self.last_period_count:
            if hasattr(self.last_period_count, 'to_alipay_dict'):
                params['last_period_count'] = self.last_period_count.to_alipay_dict()
            else:
                params['last_period_count'] = self.last_period_count
        if self.last_principal_amount:
            if hasattr(self.last_principal_amount, 'to_alipay_dict'):
                params['last_principal_amount'] = self.last_principal_amount.to_alipay_dict()
            else:
                params['last_principal_amount'] = self.last_principal_amount
        if self.loan_amount:
            if hasattr(self.loan_amount, 'to_alipay_dict'):
                params['loan_amount'] = self.loan_amount.to_alipay_dict()
            else:
                params['loan_amount'] = self.loan_amount
        if self.loan_date:
            if hasattr(self.loan_date, 'to_alipay_dict'):
                params['loan_date'] = self.loan_date.to_alipay_dict()
            else:
                params['loan_date'] = self.loan_date
        if self.loan_id:
            if hasattr(self.loan_id, 'to_alipay_dict'):
                params['loan_id'] = self.loan_id.to_alipay_dict()
            else:
                params['loan_id'] = self.loan_id
        if self.repay_method:
            if hasattr(self.repay_method, 'to_alipay_dict'):
                params['repay_method'] = self.repay_method.to_alipay_dict()
            else:
                params['repay_method'] = self.repay_method
        if self.select_type:
            if hasattr(self.select_type, 'to_alipay_dict'):
                params['select_type'] = self.select_type.to_alipay_dict()
            else:
                params['select_type'] = self.select_type
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
        o = ConsumerLoanLoanInfoItem()
        if 'allowed_pay_off_early' in d:
            o.allowed_pay_off_early = d['allowed_pay_off_early']
        if 'last_insurance_amount' in d:
            o.last_insurance_amount = d['last_insurance_amount']
        if 'last_interest_amount' in d:
            o.last_interest_amount = d['last_interest_amount']
        if 'last_penalty_interest_amount' in d:
            o.last_penalty_interest_amount = d['last_penalty_interest_amount']
        if 'last_period_count' in d:
            o.last_period_count = d['last_period_count']
        if 'last_principal_amount' in d:
            o.last_principal_amount = d['last_principal_amount']
        if 'loan_amount' in d:
            o.loan_amount = d['loan_amount']
        if 'loan_date' in d:
            o.loan_date = d['loan_date']
        if 'loan_id' in d:
            o.loan_id = d['loan_id']
        if 'repay_method' in d:
            o.repay_method = d['repay_method']
        if 'select_type' in d:
            o.select_type = d['select_type']
        if 'status' in d:
            o.status = d['status']
        return o


