#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TrustBillOrder(object):

    def __init__(self):
        self._actual_total_amount = None
        self._adjusted_amount = None
        self._bill_name = None
        self._bill_no = None
        self._desc = None
        self._original_total_amount = None
        self._out_bill_no = None
        self._remark = None
        self._status = None

    @property
    def actual_total_amount(self):
        return self._actual_total_amount

    @actual_total_amount.setter
    def actual_total_amount(self, value):
        self._actual_total_amount = value
    @property
    def adjusted_amount(self):
        return self._adjusted_amount

    @adjusted_amount.setter
    def adjusted_amount(self, value):
        self._adjusted_amount = value
    @property
    def bill_name(self):
        return self._bill_name

    @bill_name.setter
    def bill_name(self, value):
        self._bill_name = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def original_total_amount(self):
        return self._original_total_amount

    @original_total_amount.setter
    def original_total_amount(self, value):
        self._original_total_amount = value
    @property
    def out_bill_no(self):
        return self._out_bill_no

    @out_bill_no.setter
    def out_bill_no(self, value):
        self._out_bill_no = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_total_amount:
            if hasattr(self.actual_total_amount, 'to_alipay_dict'):
                params['actual_total_amount'] = self.actual_total_amount.to_alipay_dict()
            else:
                params['actual_total_amount'] = self.actual_total_amount
        if self.adjusted_amount:
            if hasattr(self.adjusted_amount, 'to_alipay_dict'):
                params['adjusted_amount'] = self.adjusted_amount.to_alipay_dict()
            else:
                params['adjusted_amount'] = self.adjusted_amount
        if self.bill_name:
            if hasattr(self.bill_name, 'to_alipay_dict'):
                params['bill_name'] = self.bill_name.to_alipay_dict()
            else:
                params['bill_name'] = self.bill_name
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.original_total_amount:
            if hasattr(self.original_total_amount, 'to_alipay_dict'):
                params['original_total_amount'] = self.original_total_amount.to_alipay_dict()
            else:
                params['original_total_amount'] = self.original_total_amount
        if self.out_bill_no:
            if hasattr(self.out_bill_no, 'to_alipay_dict'):
                params['out_bill_no'] = self.out_bill_no.to_alipay_dict()
            else:
                params['out_bill_no'] = self.out_bill_no
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
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
        o = TrustBillOrder()
        if 'actual_total_amount' in d:
            o.actual_total_amount = d['actual_total_amount']
        if 'adjusted_amount' in d:
            o.adjusted_amount = d['adjusted_amount']
        if 'bill_name' in d:
            o.bill_name = d['bill_name']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'desc' in d:
            o.desc = d['desc']
        if 'original_total_amount' in d:
            o.original_total_amount = d['original_total_amount']
        if 'out_bill_no' in d:
            o.out_bill_no = d['out_bill_no']
        if 'remark' in d:
            o.remark = d['remark']
        if 'status' in d:
            o.status = d['status']
        return o


