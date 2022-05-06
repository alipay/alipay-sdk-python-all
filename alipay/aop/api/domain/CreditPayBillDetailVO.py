#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO


class CreditPayBillDetailVO(object):

    def __init__(self):
        self._bill_date = None
        self._bill_no = None
        self._bill_term_desc = None
        self._repay_date = None
        self._repay_fee_amt = None
        self._repay_int_amt = None
        self._repay_prin_amt = None
        self._total_repay_amt = None

    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def bill_term_desc(self):
        return self._bill_term_desc

    @bill_term_desc.setter
    def bill_term_desc(self, value):
        self._bill_term_desc = value
    @property
    def repay_date(self):
        return self._repay_date

    @repay_date.setter
    def repay_date(self, value):
        self._repay_date = value
    @property
    def repay_fee_amt(self):
        return self._repay_fee_amt

    @repay_fee_amt.setter
    def repay_fee_amt(self, value):
        if isinstance(value, CreditPayMoneyVO):
            self._repay_fee_amt = value
        else:
            self._repay_fee_amt = CreditPayMoneyVO.from_alipay_dict(value)
    @property
    def repay_int_amt(self):
        return self._repay_int_amt

    @repay_int_amt.setter
    def repay_int_amt(self, value):
        if isinstance(value, CreditPayMoneyVO):
            self._repay_int_amt = value
        else:
            self._repay_int_amt = CreditPayMoneyVO.from_alipay_dict(value)
    @property
    def repay_prin_amt(self):
        return self._repay_prin_amt

    @repay_prin_amt.setter
    def repay_prin_amt(self, value):
        if isinstance(value, CreditPayMoneyVO):
            self._repay_prin_amt = value
        else:
            self._repay_prin_amt = CreditPayMoneyVO.from_alipay_dict(value)
    @property
    def total_repay_amt(self):
        return self._total_repay_amt

    @total_repay_amt.setter
    def total_repay_amt(self, value):
        if isinstance(value, CreditPayMoneyVO):
            self._total_repay_amt = value
        else:
            self._total_repay_amt = CreditPayMoneyVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.bill_date:
            if hasattr(self.bill_date, 'to_alipay_dict'):
                params['bill_date'] = self.bill_date.to_alipay_dict()
            else:
                params['bill_date'] = self.bill_date
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.bill_term_desc:
            if hasattr(self.bill_term_desc, 'to_alipay_dict'):
                params['bill_term_desc'] = self.bill_term_desc.to_alipay_dict()
            else:
                params['bill_term_desc'] = self.bill_term_desc
        if self.repay_date:
            if hasattr(self.repay_date, 'to_alipay_dict'):
                params['repay_date'] = self.repay_date.to_alipay_dict()
            else:
                params['repay_date'] = self.repay_date
        if self.repay_fee_amt:
            if hasattr(self.repay_fee_amt, 'to_alipay_dict'):
                params['repay_fee_amt'] = self.repay_fee_amt.to_alipay_dict()
            else:
                params['repay_fee_amt'] = self.repay_fee_amt
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
        if self.total_repay_amt:
            if hasattr(self.total_repay_amt, 'to_alipay_dict'):
                params['total_repay_amt'] = self.total_repay_amt.to_alipay_dict()
            else:
                params['total_repay_amt'] = self.total_repay_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditPayBillDetailVO()
        if 'bill_date' in d:
            o.bill_date = d['bill_date']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'bill_term_desc' in d:
            o.bill_term_desc = d['bill_term_desc']
        if 'repay_date' in d:
            o.repay_date = d['repay_date']
        if 'repay_fee_amt' in d:
            o.repay_fee_amt = d['repay_fee_amt']
        if 'repay_int_amt' in d:
            o.repay_int_amt = d['repay_int_amt']
        if 'repay_prin_amt' in d:
            o.repay_prin_amt = d['repay_prin_amt']
        if 'total_repay_amt' in d:
            o.total_repay_amt = d['total_repay_amt']
        return o


