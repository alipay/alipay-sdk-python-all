#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RepayDetailVO(object):

    def __init__(self):
        self._paid_int_amt = None
        self._paid_ovd_int_amt = None
        self._paid_ovd_int_penalty_amt = None
        self._paid_ovd_prin_amt = None
        self._paid_ovd_prin_penalty_amt = None
        self._paid_prin_amt = None
        self._repay_amt_total = None
        self._repay_date = None

    @property
    def paid_int_amt(self):
        return self._paid_int_amt

    @paid_int_amt.setter
    def paid_int_amt(self, value):
        self._paid_int_amt = value
    @property
    def paid_ovd_int_amt(self):
        return self._paid_ovd_int_amt

    @paid_ovd_int_amt.setter
    def paid_ovd_int_amt(self, value):
        self._paid_ovd_int_amt = value
    @property
    def paid_ovd_int_penalty_amt(self):
        return self._paid_ovd_int_penalty_amt

    @paid_ovd_int_penalty_amt.setter
    def paid_ovd_int_penalty_amt(self, value):
        self._paid_ovd_int_penalty_amt = value
    @property
    def paid_ovd_prin_amt(self):
        return self._paid_ovd_prin_amt

    @paid_ovd_prin_amt.setter
    def paid_ovd_prin_amt(self, value):
        self._paid_ovd_prin_amt = value
    @property
    def paid_ovd_prin_penalty_amt(self):
        return self._paid_ovd_prin_penalty_amt

    @paid_ovd_prin_penalty_amt.setter
    def paid_ovd_prin_penalty_amt(self, value):
        self._paid_ovd_prin_penalty_amt = value
    @property
    def paid_prin_amt(self):
        return self._paid_prin_amt

    @paid_prin_amt.setter
    def paid_prin_amt(self, value):
        self._paid_prin_amt = value
    @property
    def repay_amt_total(self):
        return self._repay_amt_total

    @repay_amt_total.setter
    def repay_amt_total(self, value):
        self._repay_amt_total = value
    @property
    def repay_date(self):
        return self._repay_date

    @repay_date.setter
    def repay_date(self, value):
        self._repay_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.paid_int_amt:
            if hasattr(self.paid_int_amt, 'to_alipay_dict'):
                params['paid_int_amt'] = self.paid_int_amt.to_alipay_dict()
            else:
                params['paid_int_amt'] = self.paid_int_amt
        if self.paid_ovd_int_amt:
            if hasattr(self.paid_ovd_int_amt, 'to_alipay_dict'):
                params['paid_ovd_int_amt'] = self.paid_ovd_int_amt.to_alipay_dict()
            else:
                params['paid_ovd_int_amt'] = self.paid_ovd_int_amt
        if self.paid_ovd_int_penalty_amt:
            if hasattr(self.paid_ovd_int_penalty_amt, 'to_alipay_dict'):
                params['paid_ovd_int_penalty_amt'] = self.paid_ovd_int_penalty_amt.to_alipay_dict()
            else:
                params['paid_ovd_int_penalty_amt'] = self.paid_ovd_int_penalty_amt
        if self.paid_ovd_prin_amt:
            if hasattr(self.paid_ovd_prin_amt, 'to_alipay_dict'):
                params['paid_ovd_prin_amt'] = self.paid_ovd_prin_amt.to_alipay_dict()
            else:
                params['paid_ovd_prin_amt'] = self.paid_ovd_prin_amt
        if self.paid_ovd_prin_penalty_amt:
            if hasattr(self.paid_ovd_prin_penalty_amt, 'to_alipay_dict'):
                params['paid_ovd_prin_penalty_amt'] = self.paid_ovd_prin_penalty_amt.to_alipay_dict()
            else:
                params['paid_ovd_prin_penalty_amt'] = self.paid_ovd_prin_penalty_amt
        if self.paid_prin_amt:
            if hasattr(self.paid_prin_amt, 'to_alipay_dict'):
                params['paid_prin_amt'] = self.paid_prin_amt.to_alipay_dict()
            else:
                params['paid_prin_amt'] = self.paid_prin_amt
        if self.repay_amt_total:
            if hasattr(self.repay_amt_total, 'to_alipay_dict'):
                params['repay_amt_total'] = self.repay_amt_total.to_alipay_dict()
            else:
                params['repay_amt_total'] = self.repay_amt_total
        if self.repay_date:
            if hasattr(self.repay_date, 'to_alipay_dict'):
                params['repay_date'] = self.repay_date.to_alipay_dict()
            else:
                params['repay_date'] = self.repay_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RepayDetailVO()
        if 'paid_int_amt' in d:
            o.paid_int_amt = d['paid_int_amt']
        if 'paid_ovd_int_amt' in d:
            o.paid_ovd_int_amt = d['paid_ovd_int_amt']
        if 'paid_ovd_int_penalty_amt' in d:
            o.paid_ovd_int_penalty_amt = d['paid_ovd_int_penalty_amt']
        if 'paid_ovd_prin_amt' in d:
            o.paid_ovd_prin_amt = d['paid_ovd_prin_amt']
        if 'paid_ovd_prin_penalty_amt' in d:
            o.paid_ovd_prin_penalty_amt = d['paid_ovd_prin_penalty_amt']
        if 'paid_prin_amt' in d:
            o.paid_prin_amt = d['paid_prin_amt']
        if 'repay_amt_total' in d:
            o.repay_amt_total = d['repay_amt_total']
        if 'repay_date' in d:
            o.repay_date = d['repay_date']
        return o


