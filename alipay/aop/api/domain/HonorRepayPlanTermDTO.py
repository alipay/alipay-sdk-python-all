#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HonorRepayPlanTermDTO(object):

    def __init__(self):
        self._amount = None
        self._overdue = None
        self._overdue_amount = None
        self._overdue_days = None
        self._payable_term_amount = None
        self._payable_term_inter_penalty = None
        self._payable_term_interest = None
        self._payable_term_penalty = None
        self._payable_term_prin_penalty = None
        self._payable_term_principal = None
        self._should_repay_date = None
        self._term_amount = None
        self._term_inter_penalty = None
        self._term_interest = None
        self._term_no = None
        self._term_penalty = None
        self._term_prin_penalty = None
        self._term_principal = None
        self._term_status = None
        self._term_total_discount = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def overdue(self):
        return self._overdue

    @overdue.setter
    def overdue(self, value):
        self._overdue = value
    @property
    def overdue_amount(self):
        return self._overdue_amount

    @overdue_amount.setter
    def overdue_amount(self, value):
        self._overdue_amount = value
    @property
    def overdue_days(self):
        return self._overdue_days

    @overdue_days.setter
    def overdue_days(self, value):
        self._overdue_days = value
    @property
    def payable_term_amount(self):
        return self._payable_term_amount

    @payable_term_amount.setter
    def payable_term_amount(self, value):
        self._payable_term_amount = value
    @property
    def payable_term_inter_penalty(self):
        return self._payable_term_inter_penalty

    @payable_term_inter_penalty.setter
    def payable_term_inter_penalty(self, value):
        self._payable_term_inter_penalty = value
    @property
    def payable_term_interest(self):
        return self._payable_term_interest

    @payable_term_interest.setter
    def payable_term_interest(self, value):
        self._payable_term_interest = value
    @property
    def payable_term_penalty(self):
        return self._payable_term_penalty

    @payable_term_penalty.setter
    def payable_term_penalty(self, value):
        self._payable_term_penalty = value
    @property
    def payable_term_prin_penalty(self):
        return self._payable_term_prin_penalty

    @payable_term_prin_penalty.setter
    def payable_term_prin_penalty(self, value):
        self._payable_term_prin_penalty = value
    @property
    def payable_term_principal(self):
        return self._payable_term_principal

    @payable_term_principal.setter
    def payable_term_principal(self, value):
        self._payable_term_principal = value
    @property
    def should_repay_date(self):
        return self._should_repay_date

    @should_repay_date.setter
    def should_repay_date(self, value):
        self._should_repay_date = value
    @property
    def term_amount(self):
        return self._term_amount

    @term_amount.setter
    def term_amount(self, value):
        self._term_amount = value
    @property
    def term_inter_penalty(self):
        return self._term_inter_penalty

    @term_inter_penalty.setter
    def term_inter_penalty(self, value):
        self._term_inter_penalty = value
    @property
    def term_interest(self):
        return self._term_interest

    @term_interest.setter
    def term_interest(self, value):
        self._term_interest = value
    @property
    def term_no(self):
        return self._term_no

    @term_no.setter
    def term_no(self, value):
        self._term_no = value
    @property
    def term_penalty(self):
        return self._term_penalty

    @term_penalty.setter
    def term_penalty(self, value):
        self._term_penalty = value
    @property
    def term_prin_penalty(self):
        return self._term_prin_penalty

    @term_prin_penalty.setter
    def term_prin_penalty(self, value):
        self._term_prin_penalty = value
    @property
    def term_principal(self):
        return self._term_principal

    @term_principal.setter
    def term_principal(self, value):
        self._term_principal = value
    @property
    def term_status(self):
        return self._term_status

    @term_status.setter
    def term_status(self, value):
        self._term_status = value
    @property
    def term_total_discount(self):
        return self._term_total_discount

    @term_total_discount.setter
    def term_total_discount(self, value):
        self._term_total_discount = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.overdue:
            if hasattr(self.overdue, 'to_alipay_dict'):
                params['overdue'] = self.overdue.to_alipay_dict()
            else:
                params['overdue'] = self.overdue
        if self.overdue_amount:
            if hasattr(self.overdue_amount, 'to_alipay_dict'):
                params['overdue_amount'] = self.overdue_amount.to_alipay_dict()
            else:
                params['overdue_amount'] = self.overdue_amount
        if self.overdue_days:
            if hasattr(self.overdue_days, 'to_alipay_dict'):
                params['overdue_days'] = self.overdue_days.to_alipay_dict()
            else:
                params['overdue_days'] = self.overdue_days
        if self.payable_term_amount:
            if hasattr(self.payable_term_amount, 'to_alipay_dict'):
                params['payable_term_amount'] = self.payable_term_amount.to_alipay_dict()
            else:
                params['payable_term_amount'] = self.payable_term_amount
        if self.payable_term_inter_penalty:
            if hasattr(self.payable_term_inter_penalty, 'to_alipay_dict'):
                params['payable_term_inter_penalty'] = self.payable_term_inter_penalty.to_alipay_dict()
            else:
                params['payable_term_inter_penalty'] = self.payable_term_inter_penalty
        if self.payable_term_interest:
            if hasattr(self.payable_term_interest, 'to_alipay_dict'):
                params['payable_term_interest'] = self.payable_term_interest.to_alipay_dict()
            else:
                params['payable_term_interest'] = self.payable_term_interest
        if self.payable_term_penalty:
            if hasattr(self.payable_term_penalty, 'to_alipay_dict'):
                params['payable_term_penalty'] = self.payable_term_penalty.to_alipay_dict()
            else:
                params['payable_term_penalty'] = self.payable_term_penalty
        if self.payable_term_prin_penalty:
            if hasattr(self.payable_term_prin_penalty, 'to_alipay_dict'):
                params['payable_term_prin_penalty'] = self.payable_term_prin_penalty.to_alipay_dict()
            else:
                params['payable_term_prin_penalty'] = self.payable_term_prin_penalty
        if self.payable_term_principal:
            if hasattr(self.payable_term_principal, 'to_alipay_dict'):
                params['payable_term_principal'] = self.payable_term_principal.to_alipay_dict()
            else:
                params['payable_term_principal'] = self.payable_term_principal
        if self.should_repay_date:
            if hasattr(self.should_repay_date, 'to_alipay_dict'):
                params['should_repay_date'] = self.should_repay_date.to_alipay_dict()
            else:
                params['should_repay_date'] = self.should_repay_date
        if self.term_amount:
            if hasattr(self.term_amount, 'to_alipay_dict'):
                params['term_amount'] = self.term_amount.to_alipay_dict()
            else:
                params['term_amount'] = self.term_amount
        if self.term_inter_penalty:
            if hasattr(self.term_inter_penalty, 'to_alipay_dict'):
                params['term_inter_penalty'] = self.term_inter_penalty.to_alipay_dict()
            else:
                params['term_inter_penalty'] = self.term_inter_penalty
        if self.term_interest:
            if hasattr(self.term_interest, 'to_alipay_dict'):
                params['term_interest'] = self.term_interest.to_alipay_dict()
            else:
                params['term_interest'] = self.term_interest
        if self.term_no:
            if hasattr(self.term_no, 'to_alipay_dict'):
                params['term_no'] = self.term_no.to_alipay_dict()
            else:
                params['term_no'] = self.term_no
        if self.term_penalty:
            if hasattr(self.term_penalty, 'to_alipay_dict'):
                params['term_penalty'] = self.term_penalty.to_alipay_dict()
            else:
                params['term_penalty'] = self.term_penalty
        if self.term_prin_penalty:
            if hasattr(self.term_prin_penalty, 'to_alipay_dict'):
                params['term_prin_penalty'] = self.term_prin_penalty.to_alipay_dict()
            else:
                params['term_prin_penalty'] = self.term_prin_penalty
        if self.term_principal:
            if hasattr(self.term_principal, 'to_alipay_dict'):
                params['term_principal'] = self.term_principal.to_alipay_dict()
            else:
                params['term_principal'] = self.term_principal
        if self.term_status:
            if hasattr(self.term_status, 'to_alipay_dict'):
                params['term_status'] = self.term_status.to_alipay_dict()
            else:
                params['term_status'] = self.term_status
        if self.term_total_discount:
            if hasattr(self.term_total_discount, 'to_alipay_dict'):
                params['term_total_discount'] = self.term_total_discount.to_alipay_dict()
            else:
                params['term_total_discount'] = self.term_total_discount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HonorRepayPlanTermDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'overdue' in d:
            o.overdue = d['overdue']
        if 'overdue_amount' in d:
            o.overdue_amount = d['overdue_amount']
        if 'overdue_days' in d:
            o.overdue_days = d['overdue_days']
        if 'payable_term_amount' in d:
            o.payable_term_amount = d['payable_term_amount']
        if 'payable_term_inter_penalty' in d:
            o.payable_term_inter_penalty = d['payable_term_inter_penalty']
        if 'payable_term_interest' in d:
            o.payable_term_interest = d['payable_term_interest']
        if 'payable_term_penalty' in d:
            o.payable_term_penalty = d['payable_term_penalty']
        if 'payable_term_prin_penalty' in d:
            o.payable_term_prin_penalty = d['payable_term_prin_penalty']
        if 'payable_term_principal' in d:
            o.payable_term_principal = d['payable_term_principal']
        if 'should_repay_date' in d:
            o.should_repay_date = d['should_repay_date']
        if 'term_amount' in d:
            o.term_amount = d['term_amount']
        if 'term_inter_penalty' in d:
            o.term_inter_penalty = d['term_inter_penalty']
        if 'term_interest' in d:
            o.term_interest = d['term_interest']
        if 'term_no' in d:
            o.term_no = d['term_no']
        if 'term_penalty' in d:
            o.term_penalty = d['term_penalty']
        if 'term_prin_penalty' in d:
            o.term_prin_penalty = d['term_prin_penalty']
        if 'term_principal' in d:
            o.term_principal = d['term_principal']
        if 'term_status' in d:
            o.term_status = d['term_status']
        if 'term_total_discount' in d:
            o.term_total_discount = d['term_total_discount']
        return o


