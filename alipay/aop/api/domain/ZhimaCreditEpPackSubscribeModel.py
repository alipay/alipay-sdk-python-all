#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpPackSubscribeModel(object):

    def __init__(self):
        self._customer_id = None
        self._end_date = None
        self._pack_type = None
        self._quota = None
        self._report_amount = None
        self._start_date = None

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def pack_type(self):
        return self._pack_type

    @pack_type.setter
    def pack_type(self, value):
        self._pack_type = value
    @property
    def quota(self):
        return self._quota

    @quota.setter
    def quota(self, value):
        self._quota = value
    @property
    def report_amount(self):
        return self._report_amount

    @report_amount.setter
    def report_amount(self, value):
        self._report_amount = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.pack_type:
            if hasattr(self.pack_type, 'to_alipay_dict'):
                params['pack_type'] = self.pack_type.to_alipay_dict()
            else:
                params['pack_type'] = self.pack_type
        if self.quota:
            if hasattr(self.quota, 'to_alipay_dict'):
                params['quota'] = self.quota.to_alipay_dict()
            else:
                params['quota'] = self.quota
        if self.report_amount:
            if hasattr(self.report_amount, 'to_alipay_dict'):
                params['report_amount'] = self.report_amount.to_alipay_dict()
            else:
                params['report_amount'] = self.report_amount
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpPackSubscribeModel()
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'pack_type' in d:
            o.pack_type = d['pack_type']
        if 'quota' in d:
            o.quota = d['quota']
        if 'report_amount' in d:
            o.report_amount = d['report_amount']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


