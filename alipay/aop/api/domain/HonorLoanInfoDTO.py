#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HonorLoanInfoDTO(object):

    def __init__(self):
        self._apr = None
        self._bank_card_id = None
        self._coupon_no = None
        self._day_rate = None
        self._effective_date = None
        self._loan_amount = None
        self._loan_time = None
        self._loan_use = None
        self._repay_method = None
        self._total_term = None

    @property
    def apr(self):
        return self._apr

    @apr.setter
    def apr(self, value):
        self._apr = value
    @property
    def bank_card_id(self):
        return self._bank_card_id

    @bank_card_id.setter
    def bank_card_id(self, value):
        self._bank_card_id = value
    @property
    def coupon_no(self):
        return self._coupon_no

    @coupon_no.setter
    def coupon_no(self, value):
        self._coupon_no = value
    @property
    def day_rate(self):
        return self._day_rate

    @day_rate.setter
    def day_rate(self, value):
        self._day_rate = value
    @property
    def effective_date(self):
        return self._effective_date

    @effective_date.setter
    def effective_date(self, value):
        self._effective_date = value
    @property
    def loan_amount(self):
        return self._loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        self._loan_amount = value
    @property
    def loan_time(self):
        return self._loan_time

    @loan_time.setter
    def loan_time(self, value):
        self._loan_time = value
    @property
    def loan_use(self):
        return self._loan_use

    @loan_use.setter
    def loan_use(self, value):
        self._loan_use = value
    @property
    def repay_method(self):
        return self._repay_method

    @repay_method.setter
    def repay_method(self, value):
        self._repay_method = value
    @property
    def total_term(self):
        return self._total_term

    @total_term.setter
    def total_term(self, value):
        self._total_term = value


    def to_alipay_dict(self):
        params = dict()
        if self.apr:
            if hasattr(self.apr, 'to_alipay_dict'):
                params['apr'] = self.apr.to_alipay_dict()
            else:
                params['apr'] = self.apr
        if self.bank_card_id:
            if hasattr(self.bank_card_id, 'to_alipay_dict'):
                params['bank_card_id'] = self.bank_card_id.to_alipay_dict()
            else:
                params['bank_card_id'] = self.bank_card_id
        if self.coupon_no:
            if hasattr(self.coupon_no, 'to_alipay_dict'):
                params['coupon_no'] = self.coupon_no.to_alipay_dict()
            else:
                params['coupon_no'] = self.coupon_no
        if self.day_rate:
            if hasattr(self.day_rate, 'to_alipay_dict'):
                params['day_rate'] = self.day_rate.to_alipay_dict()
            else:
                params['day_rate'] = self.day_rate
        if self.effective_date:
            if hasattr(self.effective_date, 'to_alipay_dict'):
                params['effective_date'] = self.effective_date.to_alipay_dict()
            else:
                params['effective_date'] = self.effective_date
        if self.loan_amount:
            if hasattr(self.loan_amount, 'to_alipay_dict'):
                params['loan_amount'] = self.loan_amount.to_alipay_dict()
            else:
                params['loan_amount'] = self.loan_amount
        if self.loan_time:
            if hasattr(self.loan_time, 'to_alipay_dict'):
                params['loan_time'] = self.loan_time.to_alipay_dict()
            else:
                params['loan_time'] = self.loan_time
        if self.loan_use:
            if hasattr(self.loan_use, 'to_alipay_dict'):
                params['loan_use'] = self.loan_use.to_alipay_dict()
            else:
                params['loan_use'] = self.loan_use
        if self.repay_method:
            if hasattr(self.repay_method, 'to_alipay_dict'):
                params['repay_method'] = self.repay_method.to_alipay_dict()
            else:
                params['repay_method'] = self.repay_method
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
        o = HonorLoanInfoDTO()
        if 'apr' in d:
            o.apr = d['apr']
        if 'bank_card_id' in d:
            o.bank_card_id = d['bank_card_id']
        if 'coupon_no' in d:
            o.coupon_no = d['coupon_no']
        if 'day_rate' in d:
            o.day_rate = d['day_rate']
        if 'effective_date' in d:
            o.effective_date = d['effective_date']
        if 'loan_amount' in d:
            o.loan_amount = d['loan_amount']
        if 'loan_time' in d:
            o.loan_time = d['loan_time']
        if 'loan_use' in d:
            o.loan_use = d['loan_use']
        if 'repay_method' in d:
            o.repay_method = d['repay_method']
        if 'total_term' in d:
            o.total_term = d['total_term']
        return o


