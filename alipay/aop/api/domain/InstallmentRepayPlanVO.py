#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BillTermAmountVO import BillTermAmountVO
from alipay.aop.api.domain.BillTermAmountVO import BillTermAmountVO


class InstallmentRepayPlanVO(object):

    def __init__(self):
        self._due_date = None
        self._payed_amount = None
        self._payed_date = None
        self._start_date = None
        self._status = None
        self._term_amount = None
        self._term_num = None
        self._total_amount = None

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        self._due_date = value
    @property
    def payed_amount(self):
        return self._payed_amount

    @payed_amount.setter
    def payed_amount(self, value):
        if isinstance(value, BillTermAmountVO):
            self._payed_amount = value
        else:
            self._payed_amount = BillTermAmountVO.from_alipay_dict(value)
    @property
    def payed_date(self):
        return self._payed_date

    @payed_date.setter
    def payed_date(self, value):
        self._payed_date = value
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
    @property
    def term_amount(self):
        return self._term_amount

    @term_amount.setter
    def term_amount(self, value):
        if isinstance(value, BillTermAmountVO):
            self._term_amount = value
        else:
            self._term_amount = BillTermAmountVO.from_alipay_dict(value)
    @property
    def term_num(self):
        return self._term_num

    @term_num.setter
    def term_num(self, value):
        self._term_num = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.due_date:
            if hasattr(self.due_date, 'to_alipay_dict'):
                params['due_date'] = self.due_date.to_alipay_dict()
            else:
                params['due_date'] = self.due_date
        if self.payed_amount:
            if hasattr(self.payed_amount, 'to_alipay_dict'):
                params['payed_amount'] = self.payed_amount.to_alipay_dict()
            else:
                params['payed_amount'] = self.payed_amount
        if self.payed_date:
            if hasattr(self.payed_date, 'to_alipay_dict'):
                params['payed_date'] = self.payed_date.to_alipay_dict()
            else:
                params['payed_date'] = self.payed_date
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
        if self.term_amount:
            if hasattr(self.term_amount, 'to_alipay_dict'):
                params['term_amount'] = self.term_amount.to_alipay_dict()
            else:
                params['term_amount'] = self.term_amount
        if self.term_num:
            if hasattr(self.term_num, 'to_alipay_dict'):
                params['term_num'] = self.term_num.to_alipay_dict()
            else:
                params['term_num'] = self.term_num
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
        o = InstallmentRepayPlanVO()
        if 'due_date' in d:
            o.due_date = d['due_date']
        if 'payed_amount' in d:
            o.payed_amount = d['payed_amount']
        if 'payed_date' in d:
            o.payed_date = d['payed_date']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'status' in d:
            o.status = d['status']
        if 'term_amount' in d:
            o.term_amount = d['term_amount']
        if 'term_num' in d:
            o.term_num = d['term_num']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


