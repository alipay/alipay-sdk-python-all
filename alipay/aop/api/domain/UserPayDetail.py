#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserPayDetail(object):

    def __init__(self):
        self._pay_account = None
        self._pay_finish_time = None
        self._pay_fund_order_id = None
        self._salary_status = None
        self._user_bill_no = None

    @property
    def pay_account(self):
        return self._pay_account

    @pay_account.setter
    def pay_account(self, value):
        self._pay_account = value
    @property
    def pay_finish_time(self):
        return self._pay_finish_time

    @pay_finish_time.setter
    def pay_finish_time(self, value):
        self._pay_finish_time = value
    @property
    def pay_fund_order_id(self):
        return self._pay_fund_order_id

    @pay_fund_order_id.setter
    def pay_fund_order_id(self, value):
        self._pay_fund_order_id = value
    @property
    def salary_status(self):
        return self._salary_status

    @salary_status.setter
    def salary_status(self, value):
        self._salary_status = value
    @property
    def user_bill_no(self):
        return self._user_bill_no

    @user_bill_no.setter
    def user_bill_no(self, value):
        self._user_bill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.pay_account:
            if hasattr(self.pay_account, 'to_alipay_dict'):
                params['pay_account'] = self.pay_account.to_alipay_dict()
            else:
                params['pay_account'] = self.pay_account
        if self.pay_finish_time:
            if hasattr(self.pay_finish_time, 'to_alipay_dict'):
                params['pay_finish_time'] = self.pay_finish_time.to_alipay_dict()
            else:
                params['pay_finish_time'] = self.pay_finish_time
        if self.pay_fund_order_id:
            if hasattr(self.pay_fund_order_id, 'to_alipay_dict'):
                params['pay_fund_order_id'] = self.pay_fund_order_id.to_alipay_dict()
            else:
                params['pay_fund_order_id'] = self.pay_fund_order_id
        if self.salary_status:
            if hasattr(self.salary_status, 'to_alipay_dict'):
                params['salary_status'] = self.salary_status.to_alipay_dict()
            else:
                params['salary_status'] = self.salary_status
        if self.user_bill_no:
            if hasattr(self.user_bill_no, 'to_alipay_dict'):
                params['user_bill_no'] = self.user_bill_no.to_alipay_dict()
            else:
                params['user_bill_no'] = self.user_bill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserPayDetail()
        if 'pay_account' in d:
            o.pay_account = d['pay_account']
        if 'pay_finish_time' in d:
            o.pay_finish_time = d['pay_finish_time']
        if 'pay_fund_order_id' in d:
            o.pay_fund_order_id = d['pay_fund_order_id']
        if 'salary_status' in d:
            o.salary_status = d['salary_status']
        if 'user_bill_no' in d:
            o.user_bill_no = d['user_bill_no']
        return o


