#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoantradeNewloanarRepayApplyModel(object):

    def __init__(self):
        self._apply_repay_fee = None
        self._apply_repay_int = None
        self._apply_repay_penalty = None
        self._apply_repay_prin = None
        self._cust_iprole_id = None
        self._loan_ar_no = None
        self._repay_amt = None
        self._repay_card_no = None
        self._repay_type = None
        self._request_id = None

    @property
    def apply_repay_fee(self):
        return self._apply_repay_fee

    @apply_repay_fee.setter
    def apply_repay_fee(self, value):
        self._apply_repay_fee = value
    @property
    def apply_repay_int(self):
        return self._apply_repay_int

    @apply_repay_int.setter
    def apply_repay_int(self, value):
        self._apply_repay_int = value
    @property
    def apply_repay_penalty(self):
        return self._apply_repay_penalty

    @apply_repay_penalty.setter
    def apply_repay_penalty(self, value):
        self._apply_repay_penalty = value
    @property
    def apply_repay_prin(self):
        return self._apply_repay_prin

    @apply_repay_prin.setter
    def apply_repay_prin(self, value):
        self._apply_repay_prin = value
    @property
    def cust_iprole_id(self):
        return self._cust_iprole_id

    @cust_iprole_id.setter
    def cust_iprole_id(self, value):
        self._cust_iprole_id = value
    @property
    def loan_ar_no(self):
        return self._loan_ar_no

    @loan_ar_no.setter
    def loan_ar_no(self, value):
        self._loan_ar_no = value
    @property
    def repay_amt(self):
        return self._repay_amt

    @repay_amt.setter
    def repay_amt(self, value):
        self._repay_amt = value
    @property
    def repay_card_no(self):
        return self._repay_card_no

    @repay_card_no.setter
    def repay_card_no(self, value):
        self._repay_card_no = value
    @property
    def repay_type(self):
        return self._repay_type

    @repay_type.setter
    def repay_type(self, value):
        self._repay_type = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_repay_fee:
            if hasattr(self.apply_repay_fee, 'to_alipay_dict'):
                params['apply_repay_fee'] = self.apply_repay_fee.to_alipay_dict()
            else:
                params['apply_repay_fee'] = self.apply_repay_fee
        if self.apply_repay_int:
            if hasattr(self.apply_repay_int, 'to_alipay_dict'):
                params['apply_repay_int'] = self.apply_repay_int.to_alipay_dict()
            else:
                params['apply_repay_int'] = self.apply_repay_int
        if self.apply_repay_penalty:
            if hasattr(self.apply_repay_penalty, 'to_alipay_dict'):
                params['apply_repay_penalty'] = self.apply_repay_penalty.to_alipay_dict()
            else:
                params['apply_repay_penalty'] = self.apply_repay_penalty
        if self.apply_repay_prin:
            if hasattr(self.apply_repay_prin, 'to_alipay_dict'):
                params['apply_repay_prin'] = self.apply_repay_prin.to_alipay_dict()
            else:
                params['apply_repay_prin'] = self.apply_repay_prin
        if self.cust_iprole_id:
            if hasattr(self.cust_iprole_id, 'to_alipay_dict'):
                params['cust_iprole_id'] = self.cust_iprole_id.to_alipay_dict()
            else:
                params['cust_iprole_id'] = self.cust_iprole_id
        if self.loan_ar_no:
            if hasattr(self.loan_ar_no, 'to_alipay_dict'):
                params['loan_ar_no'] = self.loan_ar_no.to_alipay_dict()
            else:
                params['loan_ar_no'] = self.loan_ar_no
        if self.repay_amt:
            if hasattr(self.repay_amt, 'to_alipay_dict'):
                params['repay_amt'] = self.repay_amt.to_alipay_dict()
            else:
                params['repay_amt'] = self.repay_amt
        if self.repay_card_no:
            if hasattr(self.repay_card_no, 'to_alipay_dict'):
                params['repay_card_no'] = self.repay_card_no.to_alipay_dict()
            else:
                params['repay_card_no'] = self.repay_card_no
        if self.repay_type:
            if hasattr(self.repay_type, 'to_alipay_dict'):
                params['repay_type'] = self.repay_type.to_alipay_dict()
            else:
                params['repay_type'] = self.repay_type
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
        o = MybankCreditLoantradeNewloanarRepayApplyModel()
        if 'apply_repay_fee' in d:
            o.apply_repay_fee = d['apply_repay_fee']
        if 'apply_repay_int' in d:
            o.apply_repay_int = d['apply_repay_int']
        if 'apply_repay_penalty' in d:
            o.apply_repay_penalty = d['apply_repay_penalty']
        if 'apply_repay_prin' in d:
            o.apply_repay_prin = d['apply_repay_prin']
        if 'cust_iprole_id' in d:
            o.cust_iprole_id = d['cust_iprole_id']
        if 'loan_ar_no' in d:
            o.loan_ar_no = d['loan_ar_no']
        if 'repay_amt' in d:
            o.repay_amt = d['repay_amt']
        if 'repay_card_no' in d:
            o.repay_card_no = d['repay_card_no']
        if 'repay_type' in d:
            o.repay_type = d['repay_type']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


