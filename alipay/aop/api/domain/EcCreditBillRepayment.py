#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcCreditBillRepayment(object):

    def __init__(self):
        self._bank_loan_no = None
        self._currency = None
        self._loan_balance = None
        self._loan_out_biz_no = None
        self._repay_capital = None
        self._repay_date = None
        self._repay_interest = None
        self._repay_status = None

    @property
    def bank_loan_no(self):
        return self._bank_loan_no

    @bank_loan_no.setter
    def bank_loan_no(self, value):
        self._bank_loan_no = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def loan_balance(self):
        return self._loan_balance

    @loan_balance.setter
    def loan_balance(self, value):
        self._loan_balance = value
    @property
    def loan_out_biz_no(self):
        return self._loan_out_biz_no

    @loan_out_biz_no.setter
    def loan_out_biz_no(self, value):
        self._loan_out_biz_no = value
    @property
    def repay_capital(self):
        return self._repay_capital

    @repay_capital.setter
    def repay_capital(self, value):
        self._repay_capital = value
    @property
    def repay_date(self):
        return self._repay_date

    @repay_date.setter
    def repay_date(self, value):
        self._repay_date = value
    @property
    def repay_interest(self):
        return self._repay_interest

    @repay_interest.setter
    def repay_interest(self, value):
        self._repay_interest = value
    @property
    def repay_status(self):
        return self._repay_status

    @repay_status.setter
    def repay_status(self, value):
        self._repay_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_loan_no:
            if hasattr(self.bank_loan_no, 'to_alipay_dict'):
                params['bank_loan_no'] = self.bank_loan_no.to_alipay_dict()
            else:
                params['bank_loan_no'] = self.bank_loan_no
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.loan_balance:
            if hasattr(self.loan_balance, 'to_alipay_dict'):
                params['loan_balance'] = self.loan_balance.to_alipay_dict()
            else:
                params['loan_balance'] = self.loan_balance
        if self.loan_out_biz_no:
            if hasattr(self.loan_out_biz_no, 'to_alipay_dict'):
                params['loan_out_biz_no'] = self.loan_out_biz_no.to_alipay_dict()
            else:
                params['loan_out_biz_no'] = self.loan_out_biz_no
        if self.repay_capital:
            if hasattr(self.repay_capital, 'to_alipay_dict'):
                params['repay_capital'] = self.repay_capital.to_alipay_dict()
            else:
                params['repay_capital'] = self.repay_capital
        if self.repay_date:
            if hasattr(self.repay_date, 'to_alipay_dict'):
                params['repay_date'] = self.repay_date.to_alipay_dict()
            else:
                params['repay_date'] = self.repay_date
        if self.repay_interest:
            if hasattr(self.repay_interest, 'to_alipay_dict'):
                params['repay_interest'] = self.repay_interest.to_alipay_dict()
            else:
                params['repay_interest'] = self.repay_interest
        if self.repay_status:
            if hasattr(self.repay_status, 'to_alipay_dict'):
                params['repay_status'] = self.repay_status.to_alipay_dict()
            else:
                params['repay_status'] = self.repay_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcCreditBillRepayment()
        if 'bank_loan_no' in d:
            o.bank_loan_no = d['bank_loan_no']
        if 'currency' in d:
            o.currency = d['currency']
        if 'loan_balance' in d:
            o.loan_balance = d['loan_balance']
        if 'loan_out_biz_no' in d:
            o.loan_out_biz_no = d['loan_out_biz_no']
        if 'repay_capital' in d:
            o.repay_capital = d['repay_capital']
        if 'repay_date' in d:
            o.repay_date = d['repay_date']
        if 'repay_interest' in d:
            o.repay_interest = d['repay_interest']
        if 'repay_status' in d:
            o.repay_status = d['repay_status']
        return o


