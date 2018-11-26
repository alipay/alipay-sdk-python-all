#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PreRepayPlanTermVO(object):

    def __init__(self):
        self._int_bal = None
        self._prin_bal = None
        self._repay_amt_total = None
        self._term_end_date = None
        self._term_no = None

    @property
    def int_bal(self):
        return self._int_bal

    @int_bal.setter
    def int_bal(self, value):
        self._int_bal = value
    @property
    def prin_bal(self):
        return self._prin_bal

    @prin_bal.setter
    def prin_bal(self, value):
        self._prin_bal = value
    @property
    def repay_amt_total(self):
        return self._repay_amt_total

    @repay_amt_total.setter
    def repay_amt_total(self, value):
        self._repay_amt_total = value
    @property
    def term_end_date(self):
        return self._term_end_date

    @term_end_date.setter
    def term_end_date(self, value):
        self._term_end_date = value
    @property
    def term_no(self):
        return self._term_no

    @term_no.setter
    def term_no(self, value):
        self._term_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.int_bal:
            if hasattr(self.int_bal, 'to_alipay_dict'):
                params['int_bal'] = self.int_bal.to_alipay_dict()
            else:
                params['int_bal'] = self.int_bal
        if self.prin_bal:
            if hasattr(self.prin_bal, 'to_alipay_dict'):
                params['prin_bal'] = self.prin_bal.to_alipay_dict()
            else:
                params['prin_bal'] = self.prin_bal
        if self.repay_amt_total:
            if hasattr(self.repay_amt_total, 'to_alipay_dict'):
                params['repay_amt_total'] = self.repay_amt_total.to_alipay_dict()
            else:
                params['repay_amt_total'] = self.repay_amt_total
        if self.term_end_date:
            if hasattr(self.term_end_date, 'to_alipay_dict'):
                params['term_end_date'] = self.term_end_date.to_alipay_dict()
            else:
                params['term_end_date'] = self.term_end_date
        if self.term_no:
            if hasattr(self.term_no, 'to_alipay_dict'):
                params['term_no'] = self.term_no.to_alipay_dict()
            else:
                params['term_no'] = self.term_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PreRepayPlanTermVO()
        if 'int_bal' in d:
            o.int_bal = d['int_bal']
        if 'prin_bal' in d:
            o.prin_bal = d['prin_bal']
        if 'repay_amt_total' in d:
            o.repay_amt_total = d['repay_amt_total']
        if 'term_end_date' in d:
            o.term_end_date = d['term_end_date']
        if 'term_no' in d:
            o.term_no = d['term_no']
        return o


