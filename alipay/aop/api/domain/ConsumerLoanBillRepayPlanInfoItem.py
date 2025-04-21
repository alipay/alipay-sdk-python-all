#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsumerLoanBillRepayPlanInfoItem(object):

    def __init__(self):
        self._bill_id = None
        self._loan_id = None
        self._period_no = None
        self._repay_amount = None
        self._repay_date = None
        self._status = None

    @property
    def bill_id(self):
        return self._bill_id

    @bill_id.setter
    def bill_id(self, value):
        self._bill_id = value
    @property
    def loan_id(self):
        return self._loan_id

    @loan_id.setter
    def loan_id(self, value):
        self._loan_id = value
    @property
    def period_no(self):
        return self._period_no

    @period_no.setter
    def period_no(self, value):
        self._period_no = value
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
        if self.bill_id:
            if hasattr(self.bill_id, 'to_alipay_dict'):
                params['bill_id'] = self.bill_id.to_alipay_dict()
            else:
                params['bill_id'] = self.bill_id
        if self.loan_id:
            if hasattr(self.loan_id, 'to_alipay_dict'):
                params['loan_id'] = self.loan_id.to_alipay_dict()
            else:
                params['loan_id'] = self.loan_id
        if self.period_no:
            if hasattr(self.period_no, 'to_alipay_dict'):
                params['period_no'] = self.period_no.to_alipay_dict()
            else:
                params['period_no'] = self.period_no
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
        o = ConsumerLoanBillRepayPlanInfoItem()
        if 'bill_id' in d:
            o.bill_id = d['bill_id']
        if 'loan_id' in d:
            o.loan_id = d['loan_id']
        if 'period_no' in d:
            o.period_no = d['period_no']
        if 'repay_amount' in d:
            o.repay_amount = d['repay_amount']
        if 'repay_date' in d:
            o.repay_date = d['repay_date']
        if 'status' in d:
            o.status = d['status']
        return o


