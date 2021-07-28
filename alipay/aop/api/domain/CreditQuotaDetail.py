#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditQuotaDetail(object):

    def __init__(self):
        self._credit_term = None
        self._credit_term_unit = None
        self._end_date = None
        self._loan_quota_type = None
        self._quota_amount = None
        self._quota_amount_currency = None
        self._start_date = None

    @property
    def credit_term(self):
        return self._credit_term

    @credit_term.setter
    def credit_term(self, value):
        self._credit_term = value
    @property
    def credit_term_unit(self):
        return self._credit_term_unit

    @credit_term_unit.setter
    def credit_term_unit(self, value):
        self._credit_term_unit = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def loan_quota_type(self):
        return self._loan_quota_type

    @loan_quota_type.setter
    def loan_quota_type(self, value):
        self._loan_quota_type = value
    @property
    def quota_amount(self):
        return self._quota_amount

    @quota_amount.setter
    def quota_amount(self, value):
        self._quota_amount = value
    @property
    def quota_amount_currency(self):
        return self._quota_amount_currency

    @quota_amount_currency.setter
    def quota_amount_currency(self, value):
        self._quota_amount_currency = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_term:
            if hasattr(self.credit_term, 'to_alipay_dict'):
                params['credit_term'] = self.credit_term.to_alipay_dict()
            else:
                params['credit_term'] = self.credit_term
        if self.credit_term_unit:
            if hasattr(self.credit_term_unit, 'to_alipay_dict'):
                params['credit_term_unit'] = self.credit_term_unit.to_alipay_dict()
            else:
                params['credit_term_unit'] = self.credit_term_unit
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.loan_quota_type:
            if hasattr(self.loan_quota_type, 'to_alipay_dict'):
                params['loan_quota_type'] = self.loan_quota_type.to_alipay_dict()
            else:
                params['loan_quota_type'] = self.loan_quota_type
        if self.quota_amount:
            if hasattr(self.quota_amount, 'to_alipay_dict'):
                params['quota_amount'] = self.quota_amount.to_alipay_dict()
            else:
                params['quota_amount'] = self.quota_amount
        if self.quota_amount_currency:
            if hasattr(self.quota_amount_currency, 'to_alipay_dict'):
                params['quota_amount_currency'] = self.quota_amount_currency.to_alipay_dict()
            else:
                params['quota_amount_currency'] = self.quota_amount_currency
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditQuotaDetail()
        if 'credit_term' in d:
            o.credit_term = d['credit_term']
        if 'credit_term_unit' in d:
            o.credit_term_unit = d['credit_term_unit']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'loan_quota_type' in d:
            o.loan_quota_type = d['loan_quota_type']
        if 'quota_amount' in d:
            o.quota_amount = d['quota_amount']
        if 'quota_amount_currency' in d:
            o.quota_amount_currency = d['quota_amount_currency']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


