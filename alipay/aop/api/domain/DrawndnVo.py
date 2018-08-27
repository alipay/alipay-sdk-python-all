#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DrawndnVo(object):

    def __init__(self):
        self._actual_collected_interest = None
        self._balance = None
        self._collected_principal_and_interest = None
        self._credit_no = None
        self._drawndn_date = None
        self._drawndn_no = None
        self._due_date = None
        self._five_tier_classification = None
        self._interest = None
        self._interest_rate = None
        self._lending_amount = None
        self._overduce_terms = None
        self._overdue_days = None
        self._overdue_interest = None
        self._overdue_interest_penalty = None
        self._overdue_principal = None
        self._overdue_principal_penalty = None
        self._status = None

    @property
    def actual_collected_interest(self):
        return self._actual_collected_interest

    @actual_collected_interest.setter
    def actual_collected_interest(self, value):
        self._actual_collected_interest = value
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def collected_principal_and_interest(self):
        return self._collected_principal_and_interest

    @collected_principal_and_interest.setter
    def collected_principal_and_interest(self, value):
        self._collected_principal_and_interest = value
    @property
    def credit_no(self):
        return self._credit_no

    @credit_no.setter
    def credit_no(self, value):
        self._credit_no = value
    @property
    def drawndn_date(self):
        return self._drawndn_date

    @drawndn_date.setter
    def drawndn_date(self, value):
        self._drawndn_date = value
    @property
    def drawndn_no(self):
        return self._drawndn_no

    @drawndn_no.setter
    def drawndn_no(self, value):
        self._drawndn_no = value
    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        self._due_date = value
    @property
    def five_tier_classification(self):
        return self._five_tier_classification

    @five_tier_classification.setter
    def five_tier_classification(self, value):
        self._five_tier_classification = value
    @property
    def interest(self):
        return self._interest

    @interest.setter
    def interest(self, value):
        self._interest = value
    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        self._interest_rate = value
    @property
    def lending_amount(self):
        return self._lending_amount

    @lending_amount.setter
    def lending_amount(self, value):
        self._lending_amount = value
    @property
    def overduce_terms(self):
        return self._overduce_terms

    @overduce_terms.setter
    def overduce_terms(self, value):
        self._overduce_terms = value
    @property
    def overdue_days(self):
        return self._overdue_days

    @overdue_days.setter
    def overdue_days(self, value):
        self._overdue_days = value
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_collected_interest:
            if hasattr(self.actual_collected_interest, 'to_alipay_dict'):
                params['actual_collected_interest'] = self.actual_collected_interest.to_alipay_dict()
            else:
                params['actual_collected_interest'] = self.actual_collected_interest
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.collected_principal_and_interest:
            if hasattr(self.collected_principal_and_interest, 'to_alipay_dict'):
                params['collected_principal_and_interest'] = self.collected_principal_and_interest.to_alipay_dict()
            else:
                params['collected_principal_and_interest'] = self.collected_principal_and_interest
        if self.credit_no:
            if hasattr(self.credit_no, 'to_alipay_dict'):
                params['credit_no'] = self.credit_no.to_alipay_dict()
            else:
                params['credit_no'] = self.credit_no
        if self.drawndn_date:
            if hasattr(self.drawndn_date, 'to_alipay_dict'):
                params['drawndn_date'] = self.drawndn_date.to_alipay_dict()
            else:
                params['drawndn_date'] = self.drawndn_date
        if self.drawndn_no:
            if hasattr(self.drawndn_no, 'to_alipay_dict'):
                params['drawndn_no'] = self.drawndn_no.to_alipay_dict()
            else:
                params['drawndn_no'] = self.drawndn_no
        if self.due_date:
            if hasattr(self.due_date, 'to_alipay_dict'):
                params['due_date'] = self.due_date.to_alipay_dict()
            else:
                params['due_date'] = self.due_date
        if self.five_tier_classification:
            if hasattr(self.five_tier_classification, 'to_alipay_dict'):
                params['five_tier_classification'] = self.five_tier_classification.to_alipay_dict()
            else:
                params['five_tier_classification'] = self.five_tier_classification
        if self.interest:
            if hasattr(self.interest, 'to_alipay_dict'):
                params['interest'] = self.interest.to_alipay_dict()
            else:
                params['interest'] = self.interest
        if self.interest_rate:
            if hasattr(self.interest_rate, 'to_alipay_dict'):
                params['interest_rate'] = self.interest_rate.to_alipay_dict()
            else:
                params['interest_rate'] = self.interest_rate
        if self.lending_amount:
            if hasattr(self.lending_amount, 'to_alipay_dict'):
                params['lending_amount'] = self.lending_amount.to_alipay_dict()
            else:
                params['lending_amount'] = self.lending_amount
        if self.overduce_terms:
            if hasattr(self.overduce_terms, 'to_alipay_dict'):
                params['overduce_terms'] = self.overduce_terms.to_alipay_dict()
            else:
                params['overduce_terms'] = self.overduce_terms
        if self.overdue_days:
            if hasattr(self.overdue_days, 'to_alipay_dict'):
                params['overdue_days'] = self.overdue_days.to_alipay_dict()
            else:
                params['overdue_days'] = self.overdue_days
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
        o = DrawndnVo()
        if 'actual_collected_interest' in d:
            o.actual_collected_interest = d['actual_collected_interest']
        if 'balance' in d:
            o.balance = d['balance']
        if 'collected_principal_and_interest' in d:
            o.collected_principal_and_interest = d['collected_principal_and_interest']
        if 'credit_no' in d:
            o.credit_no = d['credit_no']
        if 'drawndn_date' in d:
            o.drawndn_date = d['drawndn_date']
        if 'drawndn_no' in d:
            o.drawndn_no = d['drawndn_no']
        if 'due_date' in d:
            o.due_date = d['due_date']
        if 'five_tier_classification' in d:
            o.five_tier_classification = d['five_tier_classification']
        if 'interest' in d:
            o.interest = d['interest']
        if 'interest_rate' in d:
            o.interest_rate = d['interest_rate']
        if 'lending_amount' in d:
            o.lending_amount = d['lending_amount']
        if 'overduce_terms' in d:
            o.overduce_terms = d['overduce_terms']
        if 'overdue_days' in d:
            o.overdue_days = d['overdue_days']
        if 'overdue_interest' in d:
            o.overdue_interest = d['overdue_interest']
        if 'overdue_interest_penalty' in d:
            o.overdue_interest_penalty = d['overdue_interest_penalty']
        if 'overdue_principal' in d:
            o.overdue_principal = d['overdue_principal']
        if 'overdue_principal_penalty' in d:
            o.overdue_principal_penalty = d['overdue_principal_penalty']
        if 'status' in d:
            o.status = d['status']
        return o


