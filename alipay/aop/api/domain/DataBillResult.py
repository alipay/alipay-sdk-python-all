#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DataBillResult(object):

    def __init__(self):
        self._activity_name = None
        self._activity_type = None
        self._bank_bill_no = None
        self._bank_code = None
        self._bank_name = None
        self._branch_name = None
        self._pay_date = None
        self._pay_time = None
        self._real_pay_amt = None
        self._trade_total_amt = None
        self._user_trd_cnt_rank = None

    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def bank_bill_no(self):
        return self._bank_bill_no

    @bank_bill_no.setter
    def bank_bill_no(self, value):
        self._bank_bill_no = value
    @property
    def bank_code(self):
        return self._bank_code

    @bank_code.setter
    def bank_code(self, value):
        self._bank_code = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def branch_name(self):
        return self._branch_name

    @branch_name.setter
    def branch_name(self, value):
        self._branch_name = value
    @property
    def pay_date(self):
        return self._pay_date

    @pay_date.setter
    def pay_date(self, value):
        self._pay_date = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def real_pay_amt(self):
        return self._real_pay_amt

    @real_pay_amt.setter
    def real_pay_amt(self, value):
        self._real_pay_amt = value
    @property
    def trade_total_amt(self):
        return self._trade_total_amt

    @trade_total_amt.setter
    def trade_total_amt(self, value):
        self._trade_total_amt = value
    @property
    def user_trd_cnt_rank(self):
        return self._user_trd_cnt_rank

    @user_trd_cnt_rank.setter
    def user_trd_cnt_rank(self, value):
        self._user_trd_cnt_rank = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
        if self.bank_bill_no:
            if hasattr(self.bank_bill_no, 'to_alipay_dict'):
                params['bank_bill_no'] = self.bank_bill_no.to_alipay_dict()
            else:
                params['bank_bill_no'] = self.bank_bill_no
        if self.bank_code:
            if hasattr(self.bank_code, 'to_alipay_dict'):
                params['bank_code'] = self.bank_code.to_alipay_dict()
            else:
                params['bank_code'] = self.bank_code
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.branch_name:
            if hasattr(self.branch_name, 'to_alipay_dict'):
                params['branch_name'] = self.branch_name.to_alipay_dict()
            else:
                params['branch_name'] = self.branch_name
        if self.pay_date:
            if hasattr(self.pay_date, 'to_alipay_dict'):
                params['pay_date'] = self.pay_date.to_alipay_dict()
            else:
                params['pay_date'] = self.pay_date
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.real_pay_amt:
            if hasattr(self.real_pay_amt, 'to_alipay_dict'):
                params['real_pay_amt'] = self.real_pay_amt.to_alipay_dict()
            else:
                params['real_pay_amt'] = self.real_pay_amt
        if self.trade_total_amt:
            if hasattr(self.trade_total_amt, 'to_alipay_dict'):
                params['trade_total_amt'] = self.trade_total_amt.to_alipay_dict()
            else:
                params['trade_total_amt'] = self.trade_total_amt
        if self.user_trd_cnt_rank:
            if hasattr(self.user_trd_cnt_rank, 'to_alipay_dict'):
                params['user_trd_cnt_rank'] = self.user_trd_cnt_rank.to_alipay_dict()
            else:
                params['user_trd_cnt_rank'] = self.user_trd_cnt_rank
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DataBillResult()
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'bank_bill_no' in d:
            o.bank_bill_no = d['bank_bill_no']
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'branch_name' in d:
            o.branch_name = d['branch_name']
        if 'pay_date' in d:
            o.pay_date = d['pay_date']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'real_pay_amt' in d:
            o.real_pay_amt = d['real_pay_amt']
        if 'trade_total_amt' in d:
            o.trade_total_amt = d['trade_total_amt']
        if 'user_trd_cnt_rank' in d:
            o.user_trd_cnt_rank = d['user_trd_cnt_rank']
        return o


