#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RepaymemtPlanPreview(object):

    def __init__(self):
        self._deduct_int_amt = None
        self._end_date = None
        self._initial_int_amt = None
        self._repay_int_amt = None
        self._repay_prin_amt = None
        self._repay_total_amt = None
        self._serv_amt = None
        self._term_no = None

    @property
    def deduct_int_amt(self):
        return self._deduct_int_amt

    @deduct_int_amt.setter
    def deduct_int_amt(self, value):
        self._deduct_int_amt = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def initial_int_amt(self):
        return self._initial_int_amt

    @initial_int_amt.setter
    def initial_int_amt(self, value):
        self._initial_int_amt = value
    @property
    def repay_int_amt(self):
        return self._repay_int_amt

    @repay_int_amt.setter
    def repay_int_amt(self, value):
        self._repay_int_amt = value
    @property
    def repay_prin_amt(self):
        return self._repay_prin_amt

    @repay_prin_amt.setter
    def repay_prin_amt(self, value):
        self._repay_prin_amt = value
    @property
    def repay_total_amt(self):
        return self._repay_total_amt

    @repay_total_amt.setter
    def repay_total_amt(self, value):
        self._repay_total_amt = value
    @property
    def serv_amt(self):
        return self._serv_amt

    @serv_amt.setter
    def serv_amt(self, value):
        self._serv_amt = value
    @property
    def term_no(self):
        return self._term_no

    @term_no.setter
    def term_no(self, value):
        self._term_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.deduct_int_amt:
            if hasattr(self.deduct_int_amt, 'to_alipay_dict'):
                params['deduct_int_amt'] = self.deduct_int_amt.to_alipay_dict()
            else:
                params['deduct_int_amt'] = self.deduct_int_amt
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.initial_int_amt:
            if hasattr(self.initial_int_amt, 'to_alipay_dict'):
                params['initial_int_amt'] = self.initial_int_amt.to_alipay_dict()
            else:
                params['initial_int_amt'] = self.initial_int_amt
        if self.repay_int_amt:
            if hasattr(self.repay_int_amt, 'to_alipay_dict'):
                params['repay_int_amt'] = self.repay_int_amt.to_alipay_dict()
            else:
                params['repay_int_amt'] = self.repay_int_amt
        if self.repay_prin_amt:
            if hasattr(self.repay_prin_amt, 'to_alipay_dict'):
                params['repay_prin_amt'] = self.repay_prin_amt.to_alipay_dict()
            else:
                params['repay_prin_amt'] = self.repay_prin_amt
        if self.repay_total_amt:
            if hasattr(self.repay_total_amt, 'to_alipay_dict'):
                params['repay_total_amt'] = self.repay_total_amt.to_alipay_dict()
            else:
                params['repay_total_amt'] = self.repay_total_amt
        if self.serv_amt:
            if hasattr(self.serv_amt, 'to_alipay_dict'):
                params['serv_amt'] = self.serv_amt.to_alipay_dict()
            else:
                params['serv_amt'] = self.serv_amt
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
        o = RepaymemtPlanPreview()
        if 'deduct_int_amt' in d:
            o.deduct_int_amt = d['deduct_int_amt']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'initial_int_amt' in d:
            o.initial_int_amt = d['initial_int_amt']
        if 'repay_int_amt' in d:
            o.repay_int_amt = d['repay_int_amt']
        if 'repay_prin_amt' in d:
            o.repay_prin_amt = d['repay_prin_amt']
        if 'repay_total_amt' in d:
            o.repay_total_amt = d['repay_total_amt']
        if 'serv_amt' in d:
            o.serv_amt = d['serv_amt']
        if 'term_no' in d:
            o.term_no = d['term_no']
        return o


