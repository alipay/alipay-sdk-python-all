#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HonorLoanRecordDTO(object):

    def __init__(self):
        self._apply_date = None
        self._apply_no = None
        self._apply_time = None
        self._loan_amount = None
        self._out_order_no = None
        self._status = None
        self._total_term = None

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
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def loan_amount(self):
        return self._loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        self._loan_amount = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def total_term(self):
        return self._total_term

    @total_term.setter
    def total_term(self, value):
        self._total_term = value


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
        if self.apply_time:
            if hasattr(self.apply_time, 'to_alipay_dict'):
                params['apply_time'] = self.apply_time.to_alipay_dict()
            else:
                params['apply_time'] = self.apply_time
        if self.loan_amount:
            if hasattr(self.loan_amount, 'to_alipay_dict'):
                params['loan_amount'] = self.loan_amount.to_alipay_dict()
            else:
                params['loan_amount'] = self.loan_amount
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.total_term:
            if hasattr(self.total_term, 'to_alipay_dict'):
                params['total_term'] = self.total_term.to_alipay_dict()
            else:
                params['total_term'] = self.total_term
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HonorLoanRecordDTO()
        if 'apply_date' in d:
            o.apply_date = d['apply_date']
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'loan_amount' in d:
            o.loan_amount = d['loan_amount']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'status' in d:
            o.status = d['status']
        if 'total_term' in d:
            o.total_term = d['total_term']
        return o


