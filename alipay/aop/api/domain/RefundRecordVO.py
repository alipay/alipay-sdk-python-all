#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RefundRecordVO(object):

    def __init__(self):
        self._amount = None
        self._out_refund_id = None
        self._refund_id = None
        self._status = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def out_refund_id(self):
        return self._out_refund_id

    @out_refund_id.setter
    def out_refund_id(self, value):
        self._out_refund_id = value
    @property
    def refund_id(self):
        return self._refund_id

    @refund_id.setter
    def refund_id(self, value):
        self._refund_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.out_refund_id:
            if hasattr(self.out_refund_id, 'to_alipay_dict'):
                params['out_refund_id'] = self.out_refund_id.to_alipay_dict()
            else:
                params['out_refund_id'] = self.out_refund_id
        if self.refund_id:
            if hasattr(self.refund_id, 'to_alipay_dict'):
                params['refund_id'] = self.refund_id.to_alipay_dict()
            else:
                params['refund_id'] = self.refund_id
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
        o = RefundRecordVO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'out_refund_id' in d:
            o.out_refund_id = d['out_refund_id']
        if 'refund_id' in d:
            o.refund_id = d['refund_id']
        if 'status' in d:
            o.status = d['status']
        return o


