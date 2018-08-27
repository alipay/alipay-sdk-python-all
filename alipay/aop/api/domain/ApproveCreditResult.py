#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LoanChargeInfo import LoanChargeInfo
from alipay.aop.api.domain.InstallmentMetaInfo import InstallmentMetaInfo
from alipay.aop.api.domain.InstallmentMetaInfo import InstallmentMetaInfo


class ApproveCreditResult(object):

    def __init__(self):
        self._charge_info_list = None
        self._credit_amt = None
        self._credit_no = None
        self._credit_term = None
        self._expire_date = None
        self._instal_int_rate = None
        self._loan_term = None
        self._repay_modes = None
        self._start_date = None
        self._status = None

    @property
    def charge_info_list(self):
        return self._charge_info_list

    @charge_info_list.setter
    def charge_info_list(self, value):
        if isinstance(value, list):
            self._charge_info_list = list()
            for i in value:
                if isinstance(i, LoanChargeInfo):
                    self._charge_info_list.append(i)
                else:
                    self._charge_info_list.append(LoanChargeInfo.from_alipay_dict(i))
    @property
    def credit_amt(self):
        return self._credit_amt

    @credit_amt.setter
    def credit_amt(self, value):
        self._credit_amt = value
    @property
    def credit_no(self):
        return self._credit_no

    @credit_no.setter
    def credit_no(self, value):
        self._credit_no = value
    @property
    def credit_term(self):
        return self._credit_term

    @credit_term.setter
    def credit_term(self, value):
        self._credit_term = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def instal_int_rate(self):
        return self._instal_int_rate

    @instal_int_rate.setter
    def instal_int_rate(self, value):
        if isinstance(value, list):
            self._instal_int_rate = list()
            for i in value:
                if isinstance(i, InstallmentMetaInfo):
                    self._instal_int_rate.append(i)
                else:
                    self._instal_int_rate.append(InstallmentMetaInfo.from_alipay_dict(i))
    @property
    def loan_term(self):
        return self._loan_term

    @loan_term.setter
    def loan_term(self, value):
        self._loan_term = value
    @property
    def repay_modes(self):
        return self._repay_modes

    @repay_modes.setter
    def repay_modes(self, value):
        if isinstance(value, list):
            self._repay_modes = list()
            for i in value:
                if isinstance(i, InstallmentMetaInfo):
                    self._repay_modes.append(i)
                else:
                    self._repay_modes.append(InstallmentMetaInfo.from_alipay_dict(i))
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.charge_info_list:
            if isinstance(self.charge_info_list, list):
                for i in range(0, len(self.charge_info_list)):
                    element = self.charge_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.charge_info_list[i] = element.to_alipay_dict()
            if hasattr(self.charge_info_list, 'to_alipay_dict'):
                params['charge_info_list'] = self.charge_info_list.to_alipay_dict()
            else:
                params['charge_info_list'] = self.charge_info_list
        if self.credit_amt:
            if hasattr(self.credit_amt, 'to_alipay_dict'):
                params['credit_amt'] = self.credit_amt.to_alipay_dict()
            else:
                params['credit_amt'] = self.credit_amt
        if self.credit_no:
            if hasattr(self.credit_no, 'to_alipay_dict'):
                params['credit_no'] = self.credit_no.to_alipay_dict()
            else:
                params['credit_no'] = self.credit_no
        if self.credit_term:
            if hasattr(self.credit_term, 'to_alipay_dict'):
                params['credit_term'] = self.credit_term.to_alipay_dict()
            else:
                params['credit_term'] = self.credit_term
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.instal_int_rate:
            if isinstance(self.instal_int_rate, list):
                for i in range(0, len(self.instal_int_rate)):
                    element = self.instal_int_rate[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.instal_int_rate[i] = element.to_alipay_dict()
            if hasattr(self.instal_int_rate, 'to_alipay_dict'):
                params['instal_int_rate'] = self.instal_int_rate.to_alipay_dict()
            else:
                params['instal_int_rate'] = self.instal_int_rate
        if self.loan_term:
            if hasattr(self.loan_term, 'to_alipay_dict'):
                params['loan_term'] = self.loan_term.to_alipay_dict()
            else:
                params['loan_term'] = self.loan_term
        if self.repay_modes:
            if isinstance(self.repay_modes, list):
                for i in range(0, len(self.repay_modes)):
                    element = self.repay_modes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.repay_modes[i] = element.to_alipay_dict()
            if hasattr(self.repay_modes, 'to_alipay_dict'):
                params['repay_modes'] = self.repay_modes.to_alipay_dict()
            else:
                params['repay_modes'] = self.repay_modes
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApproveCreditResult()
        if 'charge_info_list' in d:
            o.charge_info_list = d['charge_info_list']
        if 'credit_amt' in d:
            o.credit_amt = d['credit_amt']
        if 'credit_no' in d:
            o.credit_no = d['credit_no']
        if 'credit_term' in d:
            o.credit_term = d['credit_term']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'instal_int_rate' in d:
            o.instal_int_rate = d['instal_int_rate']
        if 'loan_term' in d:
            o.loan_term = d['loan_term']
        if 'repay_modes' in d:
            o.repay_modes = d['repay_modes']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'status' in d:
            o.status = d['status']
        return o


