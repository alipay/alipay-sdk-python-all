#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentPayQueryBillListResponse(object):

    def __init__(self):
        self._account_no = None
        self._bank_name = None
        self._bank_no = None
        self._batch_no = None
        self._batch_total_amount = None
        self._description = None
        self._payment_date = None
        self._settle_serial_no = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def bank_no(self):
        return self._bank_no

    @bank_no.setter
    def bank_no(self, value):
        self._bank_no = value
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def batch_total_amount(self):
        return self._batch_total_amount

    @batch_total_amount.setter
    def batch_total_amount(self, value):
        self._batch_total_amount = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def payment_date(self):
        return self._payment_date

    @payment_date.setter
    def payment_date(self, value):
        self._payment_date = value
    @property
    def settle_serial_no(self):
        return self._settle_serial_no

    @settle_serial_no.setter
    def settle_serial_no(self, value):
        self._settle_serial_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.bank_no:
            if hasattr(self.bank_no, 'to_alipay_dict'):
                params['bank_no'] = self.bank_no.to_alipay_dict()
            else:
                params['bank_no'] = self.bank_no
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.batch_total_amount:
            if hasattr(self.batch_total_amount, 'to_alipay_dict'):
                params['batch_total_amount'] = self.batch_total_amount.to_alipay_dict()
            else:
                params['batch_total_amount'] = self.batch_total_amount
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.payment_date:
            if hasattr(self.payment_date, 'to_alipay_dict'):
                params['payment_date'] = self.payment_date.to_alipay_dict()
            else:
                params['payment_date'] = self.payment_date
        if self.settle_serial_no:
            if hasattr(self.settle_serial_no, 'to_alipay_dict'):
                params['settle_serial_no'] = self.settle_serial_no.to_alipay_dict()
            else:
                params['settle_serial_no'] = self.settle_serial_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentPayQueryBillListResponse()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'bank_no' in d:
            o.bank_no = d['bank_no']
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'batch_total_amount' in d:
            o.batch_total_amount = d['batch_total_amount']
        if 'description' in d:
            o.description = d['description']
        if 'payment_date' in d:
            o.payment_date = d['payment_date']
        if 'settle_serial_no' in d:
            o.settle_serial_no = d['settle_serial_no']
        return o


