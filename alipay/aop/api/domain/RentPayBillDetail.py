#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentPayBillDetail(object):

    def __init__(self):
        self._bill_time = None
        self._deposit_fee = None
        self._other_fee = None
        self._rent_fee = None
        self._subject = None
        self._total_amount = None

    @property
    def bill_time(self):
        return self._bill_time

    @bill_time.setter
    def bill_time(self, value):
        self._bill_time = value
    @property
    def deposit_fee(self):
        return self._deposit_fee

    @deposit_fee.setter
    def deposit_fee(self, value):
        self._deposit_fee = value
    @property
    def other_fee(self):
        return self._other_fee

    @other_fee.setter
    def other_fee(self, value):
        self._other_fee = value
    @property
    def rent_fee(self):
        return self._rent_fee

    @rent_fee.setter
    def rent_fee(self, value):
        self._rent_fee = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_time:
            if hasattr(self.bill_time, 'to_alipay_dict'):
                params['bill_time'] = self.bill_time.to_alipay_dict()
            else:
                params['bill_time'] = self.bill_time
        if self.deposit_fee:
            if hasattr(self.deposit_fee, 'to_alipay_dict'):
                params['deposit_fee'] = self.deposit_fee.to_alipay_dict()
            else:
                params['deposit_fee'] = self.deposit_fee
        if self.other_fee:
            if hasattr(self.other_fee, 'to_alipay_dict'):
                params['other_fee'] = self.other_fee.to_alipay_dict()
            else:
                params['other_fee'] = self.other_fee
        if self.rent_fee:
            if hasattr(self.rent_fee, 'to_alipay_dict'):
                params['rent_fee'] = self.rent_fee.to_alipay_dict()
            else:
                params['rent_fee'] = self.rent_fee
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentPayBillDetail()
        if 'bill_time' in d:
            o.bill_time = d['bill_time']
        if 'deposit_fee' in d:
            o.deposit_fee = d['deposit_fee']
        if 'other_fee' in d:
            o.other_fee = d['other_fee']
        if 'rent_fee' in d:
            o.rent_fee = d['rent_fee']
        if 'subject' in d:
            o.subject = d['subject']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


