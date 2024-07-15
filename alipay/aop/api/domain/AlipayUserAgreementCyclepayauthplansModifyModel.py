#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAgreementCyclepayauthplansModifyModel(object):

    def __init__(self):
        self._agreement_no = None
        self._single_amount = None
        self._total_payments = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def single_amount(self):
        return self._single_amount

    @single_amount.setter
    def single_amount(self, value):
        self._single_amount = value
    @property
    def total_payments(self):
        return self._total_payments

    @total_payments.setter
    def total_payments(self, value):
        self._total_payments = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.single_amount:
            if hasattr(self.single_amount, 'to_alipay_dict'):
                params['single_amount'] = self.single_amount.to_alipay_dict()
            else:
                params['single_amount'] = self.single_amount
        if self.total_payments:
            if hasattr(self.total_payments, 'to_alipay_dict'):
                params['total_payments'] = self.total_payments.to_alipay_dict()
            else:
                params['total_payments'] = self.total_payments
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAgreementCyclepayauthplansModifyModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'single_amount' in d:
            o.single_amount = d['single_amount']
        if 'total_payments' in d:
            o.total_payments = d['total_payments']
        return o


