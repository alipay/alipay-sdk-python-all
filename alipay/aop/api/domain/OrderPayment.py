#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderPayment(object):

    def __init__(self):
        self._company_account_id = None
        self._pay_amount = None
        self._pay_no = None
        self._pay_status = None
        self._pay_status_message = None
        self._payee_open_id = None
        self._payee_user_id = None

    @property
    def company_account_id(self):
        return self._company_account_id

    @company_account_id.setter
    def company_account_id(self, value):
        self._company_account_id = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_no(self):
        return self._pay_no

    @pay_no.setter
    def pay_no(self, value):
        self._pay_no = value
    @property
    def pay_status(self):
        return self._pay_status

    @pay_status.setter
    def pay_status(self, value):
        self._pay_status = value
    @property
    def pay_status_message(self):
        return self._pay_status_message

    @pay_status_message.setter
    def pay_status_message(self, value):
        self._pay_status_message = value
    @property
    def payee_open_id(self):
        return self._payee_open_id

    @payee_open_id.setter
    def payee_open_id(self, value):
        self._payee_open_id = value
    @property
    def payee_user_id(self):
        return self._payee_user_id

    @payee_user_id.setter
    def payee_user_id(self, value):
        self._payee_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_account_id:
            if hasattr(self.company_account_id, 'to_alipay_dict'):
                params['company_account_id'] = self.company_account_id.to_alipay_dict()
            else:
                params['company_account_id'] = self.company_account_id
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_no:
            if hasattr(self.pay_no, 'to_alipay_dict'):
                params['pay_no'] = self.pay_no.to_alipay_dict()
            else:
                params['pay_no'] = self.pay_no
        if self.pay_status:
            if hasattr(self.pay_status, 'to_alipay_dict'):
                params['pay_status'] = self.pay_status.to_alipay_dict()
            else:
                params['pay_status'] = self.pay_status
        if self.pay_status_message:
            if hasattr(self.pay_status_message, 'to_alipay_dict'):
                params['pay_status_message'] = self.pay_status_message.to_alipay_dict()
            else:
                params['pay_status_message'] = self.pay_status_message
        if self.payee_open_id:
            if hasattr(self.payee_open_id, 'to_alipay_dict'):
                params['payee_open_id'] = self.payee_open_id.to_alipay_dict()
            else:
                params['payee_open_id'] = self.payee_open_id
        if self.payee_user_id:
            if hasattr(self.payee_user_id, 'to_alipay_dict'):
                params['payee_user_id'] = self.payee_user_id.to_alipay_dict()
            else:
                params['payee_user_id'] = self.payee_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderPayment()
        if 'company_account_id' in d:
            o.company_account_id = d['company_account_id']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_no' in d:
            o.pay_no = d['pay_no']
        if 'pay_status' in d:
            o.pay_status = d['pay_status']
        if 'pay_status_message' in d:
            o.pay_status_message = d['pay_status_message']
        if 'payee_open_id' in d:
            o.payee_open_id = d['payee_open_id']
        if 'payee_user_id' in d:
            o.payee_user_id = d['payee_user_id']
        return o


