#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RepaymentRecords(object):

    def __init__(self):
        self._date = None
        self._interest = None
        self._overdue_interest = None
        self._overdue_interest_penalty = None
        self._overdue_principal = None
        self._overdue_principal_penalty = None
        self._principal = None
        self._remarks = None
        self._total_amount = None

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def interest(self):
        return self._interest

    @interest.setter
    def interest(self, value):
        self._interest = value
    @property
    def overdue_interest(self):
        return self._overdue_interest

    @overdue_interest.setter
    def overdue_interest(self, value):
        self._overdue_interest = value
    @property
    def overdue_interest_penalty(self):
        return self._overdue_interest_penalty

    @overdue_interest_penalty.setter
    def overdue_interest_penalty(self, value):
        self._overdue_interest_penalty = value
    @property
    def overdue_principal(self):
        return self._overdue_principal

    @overdue_principal.setter
    def overdue_principal(self, value):
        self._overdue_principal = value
    @property
    def overdue_principal_penalty(self):
        return self._overdue_principal_penalty

    @overdue_principal_penalty.setter
    def overdue_principal_penalty(self, value):
        self._overdue_principal_penalty = value
    @property
    def principal(self):
        return self._principal

    @principal.setter
    def principal(self, value):
        self._principal = value
    @property
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, value):
        self._remarks = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.interest:
            if hasattr(self.interest, 'to_alipay_dict'):
                params['interest'] = self.interest.to_alipay_dict()
            else:
                params['interest'] = self.interest
        if self.overdue_interest:
            if hasattr(self.overdue_interest, 'to_alipay_dict'):
                params['overdue_interest'] = self.overdue_interest.to_alipay_dict()
            else:
                params['overdue_interest'] = self.overdue_interest
        if self.overdue_interest_penalty:
            if hasattr(self.overdue_interest_penalty, 'to_alipay_dict'):
                params['overdue_interest_penalty'] = self.overdue_interest_penalty.to_alipay_dict()
            else:
                params['overdue_interest_penalty'] = self.overdue_interest_penalty
        if self.overdue_principal:
            if hasattr(self.overdue_principal, 'to_alipay_dict'):
                params['overdue_principal'] = self.overdue_principal.to_alipay_dict()
            else:
                params['overdue_principal'] = self.overdue_principal
        if self.overdue_principal_penalty:
            if hasattr(self.overdue_principal_penalty, 'to_alipay_dict'):
                params['overdue_principal_penalty'] = self.overdue_principal_penalty.to_alipay_dict()
            else:
                params['overdue_principal_penalty'] = self.overdue_principal_penalty
        if self.principal:
            if hasattr(self.principal, 'to_alipay_dict'):
                params['principal'] = self.principal.to_alipay_dict()
            else:
                params['principal'] = self.principal
        if self.remarks:
            if hasattr(self.remarks, 'to_alipay_dict'):
                params['remarks'] = self.remarks.to_alipay_dict()
            else:
                params['remarks'] = self.remarks
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RepaymentRecords()
        if 'date' in d:
            o.date = d['date']
        if 'interest' in d:
            o.interest = d['interest']
        if 'overdue_interest' in d:
            o.overdue_interest = d['overdue_interest']
        if 'overdue_interest_penalty' in d:
            o.overdue_interest_penalty = d['overdue_interest_penalty']
        if 'overdue_principal' in d:
            o.overdue_principal = d['overdue_principal']
        if 'overdue_principal_penalty' in d:
            o.overdue_principal_penalty = d['overdue_principal_penalty']
        if 'principal' in d:
            o.principal = d['principal']
        if 'remarks' in d:
            o.remarks = d['remarks']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


