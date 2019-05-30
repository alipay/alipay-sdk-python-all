#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BillAmtVo import BillAmtVo
from alipay.aop.api.domain.BillAmtVo import BillAmtVo
from alipay.aop.api.domain.MultiCurrencyMoneyVO import MultiCurrencyMoneyVO


class BillDetailVo(object):

    def __init__(self):
        self._bill_account_date = None
        self._bill_balance_detail = None
        self._bill_create_date = None
        self._bill_no = None
        self._bill_repay_detail = None
        self._bill_status = None
        self._clear_date = None
        self._repay_date = None
        self._total_prin_amt = None

    @property
    def bill_account_date(self):
        return self._bill_account_date

    @bill_account_date.setter
    def bill_account_date(self, value):
        self._bill_account_date = value
    @property
    def bill_balance_detail(self):
        return self._bill_balance_detail

    @bill_balance_detail.setter
    def bill_balance_detail(self, value):
        if isinstance(value, BillAmtVo):
            self._bill_balance_detail = value
        else:
            self._bill_balance_detail = BillAmtVo.from_alipay_dict(value)
    @property
    def bill_create_date(self):
        return self._bill_create_date

    @bill_create_date.setter
    def bill_create_date(self, value):
        self._bill_create_date = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def bill_repay_detail(self):
        return self._bill_repay_detail

    @bill_repay_detail.setter
    def bill_repay_detail(self, value):
        if isinstance(value, BillAmtVo):
            self._bill_repay_detail = value
        else:
            self._bill_repay_detail = BillAmtVo.from_alipay_dict(value)
    @property
    def bill_status(self):
        return self._bill_status

    @bill_status.setter
    def bill_status(self, value):
        self._bill_status = value
    @property
    def clear_date(self):
        return self._clear_date

    @clear_date.setter
    def clear_date(self, value):
        self._clear_date = value
    @property
    def repay_date(self):
        return self._repay_date

    @repay_date.setter
    def repay_date(self, value):
        self._repay_date = value
    @property
    def total_prin_amt(self):
        return self._total_prin_amt

    @total_prin_amt.setter
    def total_prin_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyVO):
            self._total_prin_amt = value
        else:
            self._total_prin_amt = MultiCurrencyMoneyVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.bill_account_date:
            if hasattr(self.bill_account_date, 'to_alipay_dict'):
                params['bill_account_date'] = self.bill_account_date.to_alipay_dict()
            else:
                params['bill_account_date'] = self.bill_account_date
        if self.bill_balance_detail:
            if hasattr(self.bill_balance_detail, 'to_alipay_dict'):
                params['bill_balance_detail'] = self.bill_balance_detail.to_alipay_dict()
            else:
                params['bill_balance_detail'] = self.bill_balance_detail
        if self.bill_create_date:
            if hasattr(self.bill_create_date, 'to_alipay_dict'):
                params['bill_create_date'] = self.bill_create_date.to_alipay_dict()
            else:
                params['bill_create_date'] = self.bill_create_date
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.bill_repay_detail:
            if hasattr(self.bill_repay_detail, 'to_alipay_dict'):
                params['bill_repay_detail'] = self.bill_repay_detail.to_alipay_dict()
            else:
                params['bill_repay_detail'] = self.bill_repay_detail
        if self.bill_status:
            if hasattr(self.bill_status, 'to_alipay_dict'):
                params['bill_status'] = self.bill_status.to_alipay_dict()
            else:
                params['bill_status'] = self.bill_status
        if self.clear_date:
            if hasattr(self.clear_date, 'to_alipay_dict'):
                params['clear_date'] = self.clear_date.to_alipay_dict()
            else:
                params['clear_date'] = self.clear_date
        if self.repay_date:
            if hasattr(self.repay_date, 'to_alipay_dict'):
                params['repay_date'] = self.repay_date.to_alipay_dict()
            else:
                params['repay_date'] = self.repay_date
        if self.total_prin_amt:
            if hasattr(self.total_prin_amt, 'to_alipay_dict'):
                params['total_prin_amt'] = self.total_prin_amt.to_alipay_dict()
            else:
                params['total_prin_amt'] = self.total_prin_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BillDetailVo()
        if 'bill_account_date' in d:
            o.bill_account_date = d['bill_account_date']
        if 'bill_balance_detail' in d:
            o.bill_balance_detail = d['bill_balance_detail']
        if 'bill_create_date' in d:
            o.bill_create_date = d['bill_create_date']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'bill_repay_detail' in d:
            o.bill_repay_detail = d['bill_repay_detail']
        if 'bill_status' in d:
            o.bill_status = d['bill_status']
        if 'clear_date' in d:
            o.clear_date = d['clear_date']
        if 'repay_date' in d:
            o.repay_date = d['repay_date']
        if 'total_prin_amt' in d:
            o.total_prin_amt = d['total_prin_amt']
        return o


