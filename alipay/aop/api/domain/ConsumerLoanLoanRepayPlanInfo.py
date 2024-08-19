#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConsumerLoanLoanRepayPlanInfoItem import ConsumerLoanLoanRepayPlanInfoItem


class ConsumerLoanLoanRepayPlanInfo(object):

    def __init__(self):
        self._last_period_count = None
        self._last_principal_amount = None
        self._loan_amount = None
        self._loan_date = None
        self._loan_id = None
        self._repay_method = None
        self._repay_plan_record = None
        self._total_period_count = None

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
    def repay_plan_record(self):
        return self._repay_plan_record

    @repay_plan_record.setter
    def repay_plan_record(self, value):
        if isinstance(value, list):
            self._repay_plan_record = list()
            for i in value:
                if isinstance(i, ConsumerLoanLoanRepayPlanInfoItem):
                    self._repay_plan_record.append(i)
                else:
                    self._repay_plan_record.append(ConsumerLoanLoanRepayPlanInfoItem.from_alipay_dict(i))
    @property
    def total_period_count(self):
        return self._total_period_count

    @total_period_count.setter
    def total_period_count(self, value):
        self._total_period_count = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.repay_plan_record:
            if isinstance(self.repay_plan_record, list):
                for i in range(0, len(self.repay_plan_record)):
                    element = self.repay_plan_record[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.repay_plan_record[i] = element.to_alipay_dict()
            if hasattr(self.repay_plan_record, 'to_alipay_dict'):
                params['repay_plan_record'] = self.repay_plan_record.to_alipay_dict()
            else:
                params['repay_plan_record'] = self.repay_plan_record
        if self.total_period_count:
            if hasattr(self.total_period_count, 'to_alipay_dict'):
                params['total_period_count'] = self.total_period_count.to_alipay_dict()
            else:
                params['total_period_count'] = self.total_period_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsumerLoanLoanRepayPlanInfo()
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
        if 'repay_plan_record' in d:
            o.repay_plan_record = d['repay_plan_record']
        if 'total_period_count' in d:
            o.total_period_count = d['total_period_count']
        return o


