#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LendInstallment(object):

    def __init__(self):
        self._installment_end_date = None
        self._installment_no = None
        self._settle_time = None
        self._status = None
        self._unpaid_interest = None
        self._unpaid_penalty = None
        self._unpaid_principal = None

    @property
    def installment_end_date(self):
        return self._installment_end_date

    @installment_end_date.setter
    def installment_end_date(self, value):
        self._installment_end_date = value
    @property
    def installment_no(self):
        return self._installment_no

    @installment_no.setter
    def installment_no(self, value):
        self._installment_no = value
    @property
    def settle_time(self):
        return self._settle_time

    @settle_time.setter
    def settle_time(self, value):
        self._settle_time = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.installment_end_date:
            if hasattr(self.installment_end_date, 'to_alipay_dict'):
                params['installment_end_date'] = self.installment_end_date.to_alipay_dict()
            else:
                params['installment_end_date'] = self.installment_end_date
        if self.installment_no:
            if hasattr(self.installment_no, 'to_alipay_dict'):
                params['installment_no'] = self.installment_no.to_alipay_dict()
            else:
                params['installment_no'] = self.installment_no
        if self.settle_time:
            if hasattr(self.settle_time, 'to_alipay_dict'):
                params['settle_time'] = self.settle_time.to_alipay_dict()
            else:
                params['settle_time'] = self.settle_time
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LendInstallment()
        if 'installment_end_date' in d:
            o.installment_end_date = d['installment_end_date']
        if 'installment_no' in d:
            o.installment_no = d['installment_no']
        if 'settle_time' in d:
            o.settle_time = d['settle_time']
        if 'status' in d:
            o.status = d['status']
        if 'unpaid_interest' in d:
            o.unpaid_interest = d['unpaid_interest']
        if 'unpaid_penalty' in d:
            o.unpaid_penalty = d['unpaid_penalty']
        if 'unpaid_principal' in d:
            o.unpaid_principal = d['unpaid_principal']
        return o


