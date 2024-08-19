#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsumerLoanLoanRepayPlanInfoItem(object):

    def __init__(self):
        self._insurance_amount = None
        self._interest_amount = None
        self._penalty_interest_amount = None
        self._period_number = None
        self._principal_amount = None
        self._repay_amount = None
        self._repay_date = None
        self._status = None

    @property
    def insurance_amount(self):
        return self._insurance_amount

    @insurance_amount.setter
    def insurance_amount(self, value):
        self._insurance_amount = value
    @property
    def interest_amount(self):
        return self._interest_amount

    @interest_amount.setter
    def interest_amount(self, value):
        self._interest_amount = value
    @property
    def penalty_interest_amount(self):
        return self._penalty_interest_amount

    @penalty_interest_amount.setter
    def penalty_interest_amount(self, value):
        self._penalty_interest_amount = value
    @property
    def period_number(self):
        return self._period_number

    @period_number.setter
    def period_number(self, value):
        self._period_number = value
    @property
    def principal_amount(self):
        return self._principal_amount

    @principal_amount.setter
    def principal_amount(self, value):
        self._principal_amount = value
    @property
    def repay_amount(self):
        return self._repay_amount

    @repay_amount.setter
    def repay_amount(self, value):
        self._repay_amount = value
    @property
    def repay_date(self):
        return self._repay_date

    @repay_date.setter
    def repay_date(self, value):
        self._repay_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.insurance_amount:
            if hasattr(self.insurance_amount, 'to_alipay_dict'):
                params['insurance_amount'] = self.insurance_amount.to_alipay_dict()
            else:
                params['insurance_amount'] = self.insurance_amount
        if self.interest_amount:
            if hasattr(self.interest_amount, 'to_alipay_dict'):
                params['interest_amount'] = self.interest_amount.to_alipay_dict()
            else:
                params['interest_amount'] = self.interest_amount
        if self.penalty_interest_amount:
            if hasattr(self.penalty_interest_amount, 'to_alipay_dict'):
                params['penalty_interest_amount'] = self.penalty_interest_amount.to_alipay_dict()
            else:
                params['penalty_interest_amount'] = self.penalty_interest_amount
        if self.period_number:
            if hasattr(self.period_number, 'to_alipay_dict'):
                params['period_number'] = self.period_number.to_alipay_dict()
            else:
                params['period_number'] = self.period_number
        if self.principal_amount:
            if hasattr(self.principal_amount, 'to_alipay_dict'):
                params['principal_amount'] = self.principal_amount.to_alipay_dict()
            else:
                params['principal_amount'] = self.principal_amount
        if self.repay_amount:
            if hasattr(self.repay_amount, 'to_alipay_dict'):
                params['repay_amount'] = self.repay_amount.to_alipay_dict()
            else:
                params['repay_amount'] = self.repay_amount
        if self.repay_date:
            if hasattr(self.repay_date, 'to_alipay_dict'):
                params['repay_date'] = self.repay_date.to_alipay_dict()
            else:
                params['repay_date'] = self.repay_date
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
        o = ConsumerLoanLoanRepayPlanInfoItem()
        if 'insurance_amount' in d:
            o.insurance_amount = d['insurance_amount']
        if 'interest_amount' in d:
            o.interest_amount = d['interest_amount']
        if 'penalty_interest_amount' in d:
            o.penalty_interest_amount = d['penalty_interest_amount']
        if 'period_number' in d:
            o.period_number = d['period_number']
        if 'principal_amount' in d:
            o.principal_amount = d['principal_amount']
        if 'repay_amount' in d:
            o.repay_amount = d['repay_amount']
        if 'repay_date' in d:
            o.repay_date = d['repay_date']
        if 'status' in d:
            o.status = d['status']
        return o


