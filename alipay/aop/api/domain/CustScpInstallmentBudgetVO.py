#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CustScpBillAmtVO import CustScpBillAmtVO


class CustScpInstallmentBudgetVO(object):

    def __init__(self):
        self._can_repay = None
        self._due_date = None
        self._install_num = None
        self._start_date = None
        self._status = None
        self._term_amt_detail = None
        self._term_total_amt = None

    @property
    def can_repay(self):
        return self._can_repay

    @can_repay.setter
    def can_repay(self, value):
        self._can_repay = value
    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        self._due_date = value
    @property
    def install_num(self):
        return self._install_num

    @install_num.setter
    def install_num(self, value):
        self._install_num = value
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
    def term_amt_detail(self):
        return self._term_amt_detail

    @term_amt_detail.setter
    def term_amt_detail(self, value):
        if isinstance(value, CustScpBillAmtVO):
            self._term_amt_detail = value
        else:
            self._term_amt_detail = CustScpBillAmtVO.from_alipay_dict(value)
    @property
    def term_total_amt(self):
        return self._term_total_amt

    @term_total_amt.setter
    def term_total_amt(self, value):
        self._term_total_amt = value


    def to_alipay_dict(self):
        params = dict()
        if self.can_repay:
            if hasattr(self.can_repay, 'to_alipay_dict'):
                params['can_repay'] = self.can_repay.to_alipay_dict()
            else:
                params['can_repay'] = self.can_repay
        if self.due_date:
            if hasattr(self.due_date, 'to_alipay_dict'):
                params['due_date'] = self.due_date.to_alipay_dict()
            else:
                params['due_date'] = self.due_date
        if self.install_num:
            if hasattr(self.install_num, 'to_alipay_dict'):
                params['install_num'] = self.install_num.to_alipay_dict()
            else:
                params['install_num'] = self.install_num
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
        if self.term_amt_detail:
            if hasattr(self.term_amt_detail, 'to_alipay_dict'):
                params['term_amt_detail'] = self.term_amt_detail.to_alipay_dict()
            else:
                params['term_amt_detail'] = self.term_amt_detail
        if self.term_total_amt:
            if hasattr(self.term_total_amt, 'to_alipay_dict'):
                params['term_total_amt'] = self.term_total_amt.to_alipay_dict()
            else:
                params['term_total_amt'] = self.term_total_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustScpInstallmentBudgetVO()
        if 'can_repay' in d:
            o.can_repay = d['can_repay']
        if 'due_date' in d:
            o.due_date = d['due_date']
        if 'install_num' in d:
            o.install_num = d['install_num']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'status' in d:
            o.status = d['status']
        if 'term_amt_detail' in d:
            o.term_amt_detail = d['term_amt_detail']
        if 'term_total_amt' in d:
            o.term_total_amt = d['term_total_amt']
        return o


