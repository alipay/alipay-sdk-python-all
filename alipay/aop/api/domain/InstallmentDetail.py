#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InstallmentDetail(object):

    def __init__(self):
        self._currency = None
        self._is_settle = None
        self._period = None
        self._reduce_interest = None
        self._reduce_interest_penalty = None
        self._reduce_penalty = None
        self._repaid_interest_amount = None
        self._repaid_interest_penalty_amount = None
        self._repaid_penalty_amount = None
        self._repaid_principal_amount = None
        self._rest_interest = None
        self._rest_interest_penalty = None
        self._rest_penalty = None
        self._rest_principal = None

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def is_settle(self):
        return self._is_settle

    @is_settle.setter
    def is_settle(self, value):
        self._is_settle = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def reduce_interest(self):
        return self._reduce_interest

    @reduce_interest.setter
    def reduce_interest(self, value):
        self._reduce_interest = value
    @property
    def reduce_interest_penalty(self):
        return self._reduce_interest_penalty

    @reduce_interest_penalty.setter
    def reduce_interest_penalty(self, value):
        self._reduce_interest_penalty = value
    @property
    def reduce_penalty(self):
        return self._reduce_penalty

    @reduce_penalty.setter
    def reduce_penalty(self, value):
        self._reduce_penalty = value
    @property
    def repaid_interest_amount(self):
        return self._repaid_interest_amount

    @repaid_interest_amount.setter
    def repaid_interest_amount(self, value):
        self._repaid_interest_amount = value
    @property
    def repaid_interest_penalty_amount(self):
        return self._repaid_interest_penalty_amount

    @repaid_interest_penalty_amount.setter
    def repaid_interest_penalty_amount(self, value):
        self._repaid_interest_penalty_amount = value
    @property
    def repaid_penalty_amount(self):
        return self._repaid_penalty_amount

    @repaid_penalty_amount.setter
    def repaid_penalty_amount(self, value):
        self._repaid_penalty_amount = value
    @property
    def repaid_principal_amount(self):
        return self._repaid_principal_amount

    @repaid_principal_amount.setter
    def repaid_principal_amount(self, value):
        self._repaid_principal_amount = value
    @property
    def rest_interest(self):
        return self._rest_interest

    @rest_interest.setter
    def rest_interest(self, value):
        self._rest_interest = value
    @property
    def rest_interest_penalty(self):
        return self._rest_interest_penalty

    @rest_interest_penalty.setter
    def rest_interest_penalty(self, value):
        self._rest_interest_penalty = value
    @property
    def rest_penalty(self):
        return self._rest_penalty

    @rest_penalty.setter
    def rest_penalty(self, value):
        self._rest_penalty = value
    @property
    def rest_principal(self):
        return self._rest_principal

    @rest_principal.setter
    def rest_principal(self, value):
        self._rest_principal = value


    def to_alipay_dict(self):
        params = dict()
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.is_settle:
            if hasattr(self.is_settle, 'to_alipay_dict'):
                params['is_settle'] = self.is_settle.to_alipay_dict()
            else:
                params['is_settle'] = self.is_settle
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.reduce_interest:
            if hasattr(self.reduce_interest, 'to_alipay_dict'):
                params['reduce_interest'] = self.reduce_interest.to_alipay_dict()
            else:
                params['reduce_interest'] = self.reduce_interest
        if self.reduce_interest_penalty:
            if hasattr(self.reduce_interest_penalty, 'to_alipay_dict'):
                params['reduce_interest_penalty'] = self.reduce_interest_penalty.to_alipay_dict()
            else:
                params['reduce_interest_penalty'] = self.reduce_interest_penalty
        if self.reduce_penalty:
            if hasattr(self.reduce_penalty, 'to_alipay_dict'):
                params['reduce_penalty'] = self.reduce_penalty.to_alipay_dict()
            else:
                params['reduce_penalty'] = self.reduce_penalty
        if self.repaid_interest_amount:
            if hasattr(self.repaid_interest_amount, 'to_alipay_dict'):
                params['repaid_interest_amount'] = self.repaid_interest_amount.to_alipay_dict()
            else:
                params['repaid_interest_amount'] = self.repaid_interest_amount
        if self.repaid_interest_penalty_amount:
            if hasattr(self.repaid_interest_penalty_amount, 'to_alipay_dict'):
                params['repaid_interest_penalty_amount'] = self.repaid_interest_penalty_amount.to_alipay_dict()
            else:
                params['repaid_interest_penalty_amount'] = self.repaid_interest_penalty_amount
        if self.repaid_penalty_amount:
            if hasattr(self.repaid_penalty_amount, 'to_alipay_dict'):
                params['repaid_penalty_amount'] = self.repaid_penalty_amount.to_alipay_dict()
            else:
                params['repaid_penalty_amount'] = self.repaid_penalty_amount
        if self.repaid_principal_amount:
            if hasattr(self.repaid_principal_amount, 'to_alipay_dict'):
                params['repaid_principal_amount'] = self.repaid_principal_amount.to_alipay_dict()
            else:
                params['repaid_principal_amount'] = self.repaid_principal_amount
        if self.rest_interest:
            if hasattr(self.rest_interest, 'to_alipay_dict'):
                params['rest_interest'] = self.rest_interest.to_alipay_dict()
            else:
                params['rest_interest'] = self.rest_interest
        if self.rest_interest_penalty:
            if hasattr(self.rest_interest_penalty, 'to_alipay_dict'):
                params['rest_interest_penalty'] = self.rest_interest_penalty.to_alipay_dict()
            else:
                params['rest_interest_penalty'] = self.rest_interest_penalty
        if self.rest_penalty:
            if hasattr(self.rest_penalty, 'to_alipay_dict'):
                params['rest_penalty'] = self.rest_penalty.to_alipay_dict()
            else:
                params['rest_penalty'] = self.rest_penalty
        if self.rest_principal:
            if hasattr(self.rest_principal, 'to_alipay_dict'):
                params['rest_principal'] = self.rest_principal.to_alipay_dict()
            else:
                params['rest_principal'] = self.rest_principal
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstallmentDetail()
        if 'currency' in d:
            o.currency = d['currency']
        if 'is_settle' in d:
            o.is_settle = d['is_settle']
        if 'period' in d:
            o.period = d['period']
        if 'reduce_interest' in d:
            o.reduce_interest = d['reduce_interest']
        if 'reduce_interest_penalty' in d:
            o.reduce_interest_penalty = d['reduce_interest_penalty']
        if 'reduce_penalty' in d:
            o.reduce_penalty = d['reduce_penalty']
        if 'repaid_interest_amount' in d:
            o.repaid_interest_amount = d['repaid_interest_amount']
        if 'repaid_interest_penalty_amount' in d:
            o.repaid_interest_penalty_amount = d['repaid_interest_penalty_amount']
        if 'repaid_penalty_amount' in d:
            o.repaid_penalty_amount = d['repaid_penalty_amount']
        if 'repaid_principal_amount' in d:
            o.repaid_principal_amount = d['repaid_principal_amount']
        if 'rest_interest' in d:
            o.rest_interest = d['rest_interest']
        if 'rest_interest_penalty' in d:
            o.rest_interest_penalty = d['rest_interest_penalty']
        if 'rest_penalty' in d:
            o.rest_penalty = d['rest_penalty']
        if 'rest_principal' in d:
            o.rest_principal = d['rest_principal']
        return o


