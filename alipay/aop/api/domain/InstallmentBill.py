#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InstallmentVO import InstallmentVO


class InstallmentBill(object):

    def __init__(self):
        self._installment_end_date = None
        self._installment_list = None
        self._status = None
        self._unpaid_interest = None
        self._unpaid_penalty = None
        self._unpaid_principal = None
        self._unpaid_total_amount = None

    @property
    def installment_end_date(self):
        return self._installment_end_date

    @installment_end_date.setter
    def installment_end_date(self, value):
        self._installment_end_date = value
    @property
    def installment_list(self):
        return self._installment_list

    @installment_list.setter
    def installment_list(self, value):
        if isinstance(value, list):
            self._installment_list = list()
            for i in value:
                if isinstance(i, InstallmentVO):
                    self._installment_list.append(i)
                else:
                    self._installment_list.append(InstallmentVO.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def unpaid_interest(self):
        return self._unpaid_interest

    @unpaid_interest.setter
    def unpaid_interest(self, value):
        self._unpaid_interest = value
    @property
    def unpaid_penalty(self):
        return self._unpaid_penalty

    @unpaid_penalty.setter
    def unpaid_penalty(self, value):
        self._unpaid_penalty = value
    @property
    def unpaid_principal(self):
        return self._unpaid_principal

    @unpaid_principal.setter
    def unpaid_principal(self, value):
        self._unpaid_principal = value
    @property
    def unpaid_total_amount(self):
        return self._unpaid_total_amount

    @unpaid_total_amount.setter
    def unpaid_total_amount(self, value):
        self._unpaid_total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.installment_end_date:
            if hasattr(self.installment_end_date, 'to_alipay_dict'):
                params['installment_end_date'] = self.installment_end_date.to_alipay_dict()
            else:
                params['installment_end_date'] = self.installment_end_date
        if self.installment_list:
            if isinstance(self.installment_list, list):
                for i in range(0, len(self.installment_list)):
                    element = self.installment_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.installment_list[i] = element.to_alipay_dict()
            if hasattr(self.installment_list, 'to_alipay_dict'):
                params['installment_list'] = self.installment_list.to_alipay_dict()
            else:
                params['installment_list'] = self.installment_list
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.unpaid_interest:
            if hasattr(self.unpaid_interest, 'to_alipay_dict'):
                params['unpaid_interest'] = self.unpaid_interest.to_alipay_dict()
            else:
                params['unpaid_interest'] = self.unpaid_interest
        if self.unpaid_penalty:
            if hasattr(self.unpaid_penalty, 'to_alipay_dict'):
                params['unpaid_penalty'] = self.unpaid_penalty.to_alipay_dict()
            else:
                params['unpaid_penalty'] = self.unpaid_penalty
        if self.unpaid_principal:
            if hasattr(self.unpaid_principal, 'to_alipay_dict'):
                params['unpaid_principal'] = self.unpaid_principal.to_alipay_dict()
            else:
                params['unpaid_principal'] = self.unpaid_principal
        if self.unpaid_total_amount:
            if hasattr(self.unpaid_total_amount, 'to_alipay_dict'):
                params['unpaid_total_amount'] = self.unpaid_total_amount.to_alipay_dict()
            else:
                params['unpaid_total_amount'] = self.unpaid_total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstallmentBill()
        if 'installment_end_date' in d:
            o.installment_end_date = d['installment_end_date']
        if 'installment_list' in d:
            o.installment_list = d['installment_list']
        if 'status' in d:
            o.status = d['status']
        if 'unpaid_interest' in d:
            o.unpaid_interest = d['unpaid_interest']
        if 'unpaid_penalty' in d:
            o.unpaid_penalty = d['unpaid_penalty']
        if 'unpaid_principal' in d:
            o.unpaid_principal = d['unpaid_principal']
        if 'unpaid_total_amount' in d:
            o.unpaid_total_amount = d['unpaid_total_amount']
        return o


