#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SupvFundTransferDetail(object):

    def __init__(self):
        self._amount = None
        self._desc = None
        self._occurred_time = None
        self._settle_order_no = None
        self._status = None
        self._transfer_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def occurred_time(self):
        return self._occurred_time

    @occurred_time.setter
    def occurred_time(self, value):
        self._occurred_time = value
    @property
    def settle_order_no(self):
        return self._settle_order_no

    @settle_order_no.setter
    def settle_order_no(self, value):
        self._settle_order_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def transfer_type(self):
        return self._transfer_type

    @transfer_type.setter
    def transfer_type(self, value):
        self._transfer_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.occurred_time:
            if hasattr(self.occurred_time, 'to_alipay_dict'):
                params['occurred_time'] = self.occurred_time.to_alipay_dict()
            else:
                params['occurred_time'] = self.occurred_time
        if self.settle_order_no:
            if hasattr(self.settle_order_no, 'to_alipay_dict'):
                params['settle_order_no'] = self.settle_order_no.to_alipay_dict()
            else:
                params['settle_order_no'] = self.settle_order_no
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.transfer_type:
            if hasattr(self.transfer_type, 'to_alipay_dict'):
                params['transfer_type'] = self.transfer_type.to_alipay_dict()
            else:
                params['transfer_type'] = self.transfer_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SupvFundTransferDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'desc' in d:
            o.desc = d['desc']
        if 'occurred_time' in d:
            o.occurred_time = d['occurred_time']
        if 'settle_order_no' in d:
            o.settle_order_no = d['settle_order_no']
        if 'status' in d:
            o.status = d['status']
        if 'transfer_type' in d:
            o.transfer_type = d['transfer_type']
        return o


