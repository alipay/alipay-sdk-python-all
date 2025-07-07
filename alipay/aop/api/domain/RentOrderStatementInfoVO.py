#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentOrderStatementInfoVO(object):

    def __init__(self):
        self._actual_promo_amount = None
        self._amount = None
        self._installment_no = None
        self._paid_amount = None
        self._plan_pay_time = None
        self._plan_promo_amount = None
        self._reduction = None
        self._statement_status = None
        self._statement_type = None

    @property
    def actual_promo_amount(self):
        return self._actual_promo_amount

    @actual_promo_amount.setter
    def actual_promo_amount(self, value):
        self._actual_promo_amount = value
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
    def paid_amount(self):
        return self._paid_amount

    @paid_amount.setter
    def paid_amount(self, value):
        self._paid_amount = value
    @property
    def plan_pay_time(self):
        return self._plan_pay_time

    @plan_pay_time.setter
    def plan_pay_time(self, value):
        self._plan_pay_time = value
    @property
    def plan_promo_amount(self):
        return self._plan_promo_amount

    @plan_promo_amount.setter
    def plan_promo_amount(self, value):
        self._plan_promo_amount = value
    @property
    def reduction(self):
        return self._reduction

    @reduction.setter
    def reduction(self, value):
        self._reduction = value
    @property
    def statement_status(self):
        return self._statement_status

    @statement_status.setter
    def statement_status(self, value):
        self._statement_status = value
    @property
    def statement_type(self):
        return self._statement_type

    @statement_type.setter
    def statement_type(self, value):
        self._statement_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_promo_amount:
            if hasattr(self.actual_promo_amount, 'to_alipay_dict'):
                params['actual_promo_amount'] = self.actual_promo_amount.to_alipay_dict()
            else:
                params['actual_promo_amount'] = self.actual_promo_amount
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
        if self.paid_amount:
            if hasattr(self.paid_amount, 'to_alipay_dict'):
                params['paid_amount'] = self.paid_amount.to_alipay_dict()
            else:
                params['paid_amount'] = self.paid_amount
        if self.plan_pay_time:
            if hasattr(self.plan_pay_time, 'to_alipay_dict'):
                params['plan_pay_time'] = self.plan_pay_time.to_alipay_dict()
            else:
                params['plan_pay_time'] = self.plan_pay_time
        if self.plan_promo_amount:
            if hasattr(self.plan_promo_amount, 'to_alipay_dict'):
                params['plan_promo_amount'] = self.plan_promo_amount.to_alipay_dict()
            else:
                params['plan_promo_amount'] = self.plan_promo_amount
        if self.reduction:
            if hasattr(self.reduction, 'to_alipay_dict'):
                params['reduction'] = self.reduction.to_alipay_dict()
            else:
                params['reduction'] = self.reduction
        if self.statement_status:
            if hasattr(self.statement_status, 'to_alipay_dict'):
                params['statement_status'] = self.statement_status.to_alipay_dict()
            else:
                params['statement_status'] = self.statement_status
        if self.statement_type:
            if hasattr(self.statement_type, 'to_alipay_dict'):
                params['statement_type'] = self.statement_type.to_alipay_dict()
            else:
                params['statement_type'] = self.statement_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentOrderStatementInfoVO()
        if 'actual_promo_amount' in d:
            o.actual_promo_amount = d['actual_promo_amount']
        if 'amount' in d:
            o.amount = d['amount']
        if 'installment_no' in d:
            o.installment_no = d['installment_no']
        if 'paid_amount' in d:
            o.paid_amount = d['paid_amount']
        if 'plan_pay_time' in d:
            o.plan_pay_time = d['plan_pay_time']
        if 'plan_promo_amount' in d:
            o.plan_promo_amount = d['plan_promo_amount']
        if 'reduction' in d:
            o.reduction = d['reduction']
        if 'statement_status' in d:
            o.statement_status = d['statement_status']
        if 'statement_type' in d:
            o.statement_type = d['statement_type']
        return o


