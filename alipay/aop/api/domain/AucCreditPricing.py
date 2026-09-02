#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AucCreditPricing(object):

    def __init__(self):
        self._funding_rate = None
        self._int_rate = None
        self._loan_term = None
        self._loan_term_unit = None
        self._repay_type = None
        self._serv_rate = None

    @property
    def funding_rate(self):
        return self._funding_rate

    @funding_rate.setter
    def funding_rate(self, value):
        self._funding_rate = value
    @property
    def int_rate(self):
        return self._int_rate

    @int_rate.setter
    def int_rate(self, value):
        self._int_rate = value
    @property
    def loan_term(self):
        return self._loan_term

    @loan_term.setter
    def loan_term(self, value):
        self._loan_term = value
    @property
    def loan_term_unit(self):
        return self._loan_term_unit

    @loan_term_unit.setter
    def loan_term_unit(self, value):
        self._loan_term_unit = value
    @property
    def repay_type(self):
        return self._repay_type

    @repay_type.setter
    def repay_type(self, value):
        self._repay_type = value
    @property
    def serv_rate(self):
        return self._serv_rate

    @serv_rate.setter
    def serv_rate(self, value):
        self._serv_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.funding_rate:
            if hasattr(self.funding_rate, 'to_alipay_dict'):
                params['funding_rate'] = self.funding_rate.to_alipay_dict()
            else:
                params['funding_rate'] = self.funding_rate
        if self.int_rate:
            if hasattr(self.int_rate, 'to_alipay_dict'):
                params['int_rate'] = self.int_rate.to_alipay_dict()
            else:
                params['int_rate'] = self.int_rate
        if self.loan_term:
            if hasattr(self.loan_term, 'to_alipay_dict'):
                params['loan_term'] = self.loan_term.to_alipay_dict()
            else:
                params['loan_term'] = self.loan_term
        if self.loan_term_unit:
            if hasattr(self.loan_term_unit, 'to_alipay_dict'):
                params['loan_term_unit'] = self.loan_term_unit.to_alipay_dict()
            else:
                params['loan_term_unit'] = self.loan_term_unit
        if self.repay_type:
            if hasattr(self.repay_type, 'to_alipay_dict'):
                params['repay_type'] = self.repay_type.to_alipay_dict()
            else:
                params['repay_type'] = self.repay_type
        if self.serv_rate:
            if hasattr(self.serv_rate, 'to_alipay_dict'):
                params['serv_rate'] = self.serv_rate.to_alipay_dict()
            else:
                params['serv_rate'] = self.serv_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AucCreditPricing()
        if 'funding_rate' in d:
            o.funding_rate = d['funding_rate']
        if 'int_rate' in d:
            o.int_rate = d['int_rate']
        if 'loan_term' in d:
            o.loan_term = d['loan_term']
        if 'loan_term_unit' in d:
            o.loan_term_unit = d['loan_term_unit']
        if 'repay_type' in d:
            o.repay_type = d['repay_type']
        if 'serv_rate' in d:
            o.serv_rate = d['serv_rate']
        return o


