#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsurancePersonInfo import InsurancePersonInfo
from alipay.aop.api.domain.InsurancePersonInfo import InsurancePersonInfo
from alipay.aop.api.domain.InsuranceClauseInfo import InsuranceClauseInfo
from alipay.aop.api.domain.InsurancePersonInfo import InsurancePersonInfo


class ApplyBasicInfo(object):

    def __init__(self):
        self._amount = None
        self._apply_info = None
        self._beneficiary_info = None
        self._insurance_clause = None
        self._insure_end_date = None
        self._insure_start_date = None
        self._insured_info = None
        self._premium = None
        self._rate = None
        self._related_order_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def apply_info(self):
        return self._apply_info

    @apply_info.setter
    def apply_info(self, value):
        if isinstance(value, InsurancePersonInfo):
            self._apply_info = value
        else:
            self._apply_info = InsurancePersonInfo.from_alipay_dict(value)
    @property
    def beneficiary_info(self):
        return self._beneficiary_info

    @beneficiary_info.setter
    def beneficiary_info(self, value):
        if isinstance(value, InsurancePersonInfo):
            self._beneficiary_info = value
        else:
            self._beneficiary_info = InsurancePersonInfo.from_alipay_dict(value)
    @property
    def insurance_clause(self):
        return self._insurance_clause

    @insurance_clause.setter
    def insurance_clause(self, value):
        if isinstance(value, InsuranceClauseInfo):
            self._insurance_clause = value
        else:
            self._insurance_clause = InsuranceClauseInfo.from_alipay_dict(value)
    @property
    def insure_end_date(self):
        return self._insure_end_date

    @insure_end_date.setter
    def insure_end_date(self, value):
        self._insure_end_date = value
    @property
    def insure_start_date(self):
        return self._insure_start_date

    @insure_start_date.setter
    def insure_start_date(self, value):
        self._insure_start_date = value
    @property
    def insured_info(self):
        return self._insured_info

    @insured_info.setter
    def insured_info(self, value):
        if isinstance(value, InsurancePersonInfo):
            self._insured_info = value
        else:
            self._insured_info = InsurancePersonInfo.from_alipay_dict(value)
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value
    @property
    def related_order_no(self):
        return self._related_order_no

    @related_order_no.setter
    def related_order_no(self, value):
        self._related_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.apply_info:
            if hasattr(self.apply_info, 'to_alipay_dict'):
                params['apply_info'] = self.apply_info.to_alipay_dict()
            else:
                params['apply_info'] = self.apply_info
        if self.beneficiary_info:
            if hasattr(self.beneficiary_info, 'to_alipay_dict'):
                params['beneficiary_info'] = self.beneficiary_info.to_alipay_dict()
            else:
                params['beneficiary_info'] = self.beneficiary_info
        if self.insurance_clause:
            if hasattr(self.insurance_clause, 'to_alipay_dict'):
                params['insurance_clause'] = self.insurance_clause.to_alipay_dict()
            else:
                params['insurance_clause'] = self.insurance_clause
        if self.insure_end_date:
            if hasattr(self.insure_end_date, 'to_alipay_dict'):
                params['insure_end_date'] = self.insure_end_date.to_alipay_dict()
            else:
                params['insure_end_date'] = self.insure_end_date
        if self.insure_start_date:
            if hasattr(self.insure_start_date, 'to_alipay_dict'):
                params['insure_start_date'] = self.insure_start_date.to_alipay_dict()
            else:
                params['insure_start_date'] = self.insure_start_date
        if self.insured_info:
            if hasattr(self.insured_info, 'to_alipay_dict'):
                params['insured_info'] = self.insured_info.to_alipay_dict()
            else:
                params['insured_info'] = self.insured_info
        if self.premium:
            if hasattr(self.premium, 'to_alipay_dict'):
                params['premium'] = self.premium.to_alipay_dict()
            else:
                params['premium'] = self.premium
        if self.rate:
            if hasattr(self.rate, 'to_alipay_dict'):
                params['rate'] = self.rate.to_alipay_dict()
            else:
                params['rate'] = self.rate
        if self.related_order_no:
            if hasattr(self.related_order_no, 'to_alipay_dict'):
                params['related_order_no'] = self.related_order_no.to_alipay_dict()
            else:
                params['related_order_no'] = self.related_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApplyBasicInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'apply_info' in d:
            o.apply_info = d['apply_info']
        if 'beneficiary_info' in d:
            o.beneficiary_info = d['beneficiary_info']
        if 'insurance_clause' in d:
            o.insurance_clause = d['insurance_clause']
        if 'insure_end_date' in d:
            o.insure_end_date = d['insure_end_date']
        if 'insure_start_date' in d:
            o.insure_start_date = d['insure_start_date']
        if 'insured_info' in d:
            o.insured_info = d['insured_info']
        if 'premium' in d:
            o.premium = d['premium']
        if 'rate' in d:
            o.rate = d['rate']
        if 'related_order_no' in d:
            o.related_order_no = d['related_order_no']
        return o


