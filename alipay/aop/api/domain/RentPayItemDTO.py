#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentPayItemDTO(object):

    def __init__(self):
        self._amount = None
        self._installment_no = None
        self._pay_amount = None
        self._reduction = None
        self._type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def installment_no(self):
        return self._installment_no

    @installment_no.setter
    def installment_no(self, value):
        self._installment_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def reduction(self):
        return self._reduction

    @reduction.setter
    def reduction(self, value):
        self._reduction = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.installment_no:
            if hasattr(self.installment_no, 'to_alipay_dict'):
                params['installment_no'] = self.installment_no.to_alipay_dict()
            else:
                params['installment_no'] = self.installment_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.reduction:
            if hasattr(self.reduction, 'to_alipay_dict'):
                params['reduction'] = self.reduction.to_alipay_dict()
            else:
                params['reduction'] = self.reduction
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentPayItemDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'installment_no' in d:
            o.installment_no = d['installment_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'reduction' in d:
            o.reduction = d['reduction']
        if 'type' in d:
            o.type = d['type']
        return o


