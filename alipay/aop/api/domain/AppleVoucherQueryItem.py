#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AppleVoucherQueryItem(object):

    def __init__(self):
        self._credit_amount = None
        self._end_date = None
        self._instance_no = None
        self._start_date = None
        self._status = None

    @property
    def credit_amount(self):
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, value):
        self._credit_amount = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def instance_no(self):
        return self._instance_no

    @instance_no.setter
    def instance_no(self, value):
        self._instance_no = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_amount:
            if hasattr(self.credit_amount, 'to_alipay_dict'):
                params['credit_amount'] = self.credit_amount.to_alipay_dict()
            else:
                params['credit_amount'] = self.credit_amount
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.instance_no:
            if hasattr(self.instance_no, 'to_alipay_dict'):
                params['instance_no'] = self.instance_no.to_alipay_dict()
            else:
                params['instance_no'] = self.instance_no
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppleVoucherQueryItem()
        if 'credit_amount' in d:
            o.credit_amount = d['credit_amount']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'instance_no' in d:
            o.instance_no = d['instance_no']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'status' in d:
            o.status = d['status']
        return o


