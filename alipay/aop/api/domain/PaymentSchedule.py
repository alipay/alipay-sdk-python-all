#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaymentSchedule(object):

    def __init__(self):
        self._date = None
        self._repaid_interest_total = None
        self._repaid_penalty_total = None
        self._repaid_principal_total = None
        self._start_date = None
        self._term = None
        self._unpaid_interest_total = None
        self._unpaid_penalty_total = None
        self._unpaid_principal_total = None

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def repaid_interest_total(self):
        return self._repaid_interest_total

    @repaid_interest_total.setter
    def repaid_interest_total(self, value):
        self._repaid_interest_total = value
    @property
    def repaid_penalty_total(self):
        return self._repaid_penalty_total

    @repaid_penalty_total.setter
    def repaid_penalty_total(self, value):
        self._repaid_penalty_total = value
    @property
    def repaid_principal_total(self):
        return self._repaid_principal_total

    @repaid_principal_total.setter
    def repaid_principal_total(self, value):
        self._repaid_principal_total = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, value):
        self._term = value
    @property
    def unpaid_interest_total(self):
        return self._unpaid_interest_total

    @unpaid_interest_total.setter
    def unpaid_interest_total(self, value):
        self._unpaid_interest_total = value
    @property
    def unpaid_penalty_total(self):
        return self._unpaid_penalty_total

    @unpaid_penalty_total.setter
    def unpaid_penalty_total(self, value):
        self._unpaid_penalty_total = value
    @property
    def unpaid_principal_total(self):
        return self._unpaid_principal_total

    @unpaid_principal_total.setter
    def unpaid_principal_total(self, value):
        self._unpaid_principal_total = value


    def to_alipay_dict(self):
        params = dict()
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.repaid_interest_total:
            if hasattr(self.repaid_interest_total, 'to_alipay_dict'):
                params['repaid_interest_total'] = self.repaid_interest_total.to_alipay_dict()
            else:
                params['repaid_interest_total'] = self.repaid_interest_total
        if self.repaid_penalty_total:
            if hasattr(self.repaid_penalty_total, 'to_alipay_dict'):
                params['repaid_penalty_total'] = self.repaid_penalty_total.to_alipay_dict()
            else:
                params['repaid_penalty_total'] = self.repaid_penalty_total
        if self.repaid_principal_total:
            if hasattr(self.repaid_principal_total, 'to_alipay_dict'):
                params['repaid_principal_total'] = self.repaid_principal_total.to_alipay_dict()
            else:
                params['repaid_principal_total'] = self.repaid_principal_total
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.term:
            if hasattr(self.term, 'to_alipay_dict'):
                params['term'] = self.term.to_alipay_dict()
            else:
                params['term'] = self.term
        if self.unpaid_interest_total:
            if hasattr(self.unpaid_interest_total, 'to_alipay_dict'):
                params['unpaid_interest_total'] = self.unpaid_interest_total.to_alipay_dict()
            else:
                params['unpaid_interest_total'] = self.unpaid_interest_total
        if self.unpaid_penalty_total:
            if hasattr(self.unpaid_penalty_total, 'to_alipay_dict'):
                params['unpaid_penalty_total'] = self.unpaid_penalty_total.to_alipay_dict()
            else:
                params['unpaid_penalty_total'] = self.unpaid_penalty_total
        if self.unpaid_principal_total:
            if hasattr(self.unpaid_principal_total, 'to_alipay_dict'):
                params['unpaid_principal_total'] = self.unpaid_principal_total.to_alipay_dict()
            else:
                params['unpaid_principal_total'] = self.unpaid_principal_total
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentSchedule()
        if 'date' in d:
            o.date = d['date']
        if 'repaid_interest_total' in d:
            o.repaid_interest_total = d['repaid_interest_total']
        if 'repaid_penalty_total' in d:
            o.repaid_penalty_total = d['repaid_penalty_total']
        if 'repaid_principal_total' in d:
            o.repaid_principal_total = d['repaid_principal_total']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'term' in d:
            o.term = d['term']
        if 'unpaid_interest_total' in d:
            o.unpaid_interest_total = d['unpaid_interest_total']
        if 'unpaid_penalty_total' in d:
            o.unpaid_penalty_total = d['unpaid_penalty_total']
        if 'unpaid_principal_total' in d:
            o.unpaid_principal_total = d['unpaid_principal_total']
        return o


