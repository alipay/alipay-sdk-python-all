#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoantradeLoanarRepayModel(object):

    def __init__(self):
        self._cust_iprole_id = None
        self._date = None
        self._loan_ar_no = None
        self._prin_amt = None
        self._request_id = None

    @property
    def cust_iprole_id(self):
        return self._cust_iprole_id

    @cust_iprole_id.setter
    def cust_iprole_id(self, value):
        self._cust_iprole_id = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def loan_ar_no(self):
        return self._loan_ar_no

    @loan_ar_no.setter
    def loan_ar_no(self, value):
        self._loan_ar_no = value
    @property
    def prin_amt(self):
        return self._prin_amt

    @prin_amt.setter
    def prin_amt(self, value):
        self._prin_amt = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cust_iprole_id:
            if hasattr(self.cust_iprole_id, 'to_alipay_dict'):
                params['cust_iprole_id'] = self.cust_iprole_id.to_alipay_dict()
            else:
                params['cust_iprole_id'] = self.cust_iprole_id
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.loan_ar_no:
            if hasattr(self.loan_ar_no, 'to_alipay_dict'):
                params['loan_ar_no'] = self.loan_ar_no.to_alipay_dict()
            else:
                params['loan_ar_no'] = self.loan_ar_no
        if self.prin_amt:
            if hasattr(self.prin_amt, 'to_alipay_dict'):
                params['prin_amt'] = self.prin_amt.to_alipay_dict()
            else:
                params['prin_amt'] = self.prin_amt
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradeLoanarRepayModel()
        if 'cust_iprole_id' in d:
            o.cust_iprole_id = d['cust_iprole_id']
        if 'date' in d:
            o.date = d['date']
        if 'loan_ar_no' in d:
            o.loan_ar_no = d['loan_ar_no']
        if 'prin_amt' in d:
            o.prin_amt = d['prin_amt']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


