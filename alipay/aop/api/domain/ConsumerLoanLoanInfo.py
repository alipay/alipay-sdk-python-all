#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConsumerLoanLoanInfoItem import ConsumerLoanLoanInfoItem


class ConsumerLoanLoanInfo(object):

    def __init__(self):
        self._last_principal_amount = None
        self._last_total_principal_amount = None
        self._loan_info = None
        self._total_loan_count = None

    @property
    def last_principal_amount(self):
        return self._last_principal_amount

    @last_principal_amount.setter
    def last_principal_amount(self, value):
        self._last_principal_amount = value
    @property
    def last_total_principal_amount(self):
        return self._last_total_principal_amount

    @last_total_principal_amount.setter
    def last_total_principal_amount(self, value):
        self._last_total_principal_amount = value
    @property
    def loan_info(self):
        return self._loan_info

    @loan_info.setter
    def loan_info(self, value):
        if isinstance(value, list):
            self._loan_info = list()
            for i in value:
                if isinstance(i, ConsumerLoanLoanInfoItem):
                    self._loan_info.append(i)
                else:
                    self._loan_info.append(ConsumerLoanLoanInfoItem.from_alipay_dict(i))
    @property
    def total_loan_count(self):
        return self._total_loan_count

    @total_loan_count.setter
    def total_loan_count(self, value):
        self._total_loan_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.last_principal_amount:
            if hasattr(self.last_principal_amount, 'to_alipay_dict'):
                params['last_principal_amount'] = self.last_principal_amount.to_alipay_dict()
            else:
                params['last_principal_amount'] = self.last_principal_amount
        if self.last_total_principal_amount:
            if hasattr(self.last_total_principal_amount, 'to_alipay_dict'):
                params['last_total_principal_amount'] = self.last_total_principal_amount.to_alipay_dict()
            else:
                params['last_total_principal_amount'] = self.last_total_principal_amount
        if self.loan_info:
            if isinstance(self.loan_info, list):
                for i in range(0, len(self.loan_info)):
                    element = self.loan_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.loan_info[i] = element.to_alipay_dict()
            if hasattr(self.loan_info, 'to_alipay_dict'):
                params['loan_info'] = self.loan_info.to_alipay_dict()
            else:
                params['loan_info'] = self.loan_info
        if self.total_loan_count:
            if hasattr(self.total_loan_count, 'to_alipay_dict'):
                params['total_loan_count'] = self.total_loan_count.to_alipay_dict()
            else:
                params['total_loan_count'] = self.total_loan_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsumerLoanLoanInfo()
        if 'last_principal_amount' in d:
            o.last_principal_amount = d['last_principal_amount']
        if 'last_total_principal_amount' in d:
            o.last_total_principal_amount = d['last_total_principal_amount']
        if 'loan_info' in d:
            o.loan_info = d['loan_info']
        if 'total_loan_count' in d:
            o.total_loan_count = d['total_loan_count']
        return o


