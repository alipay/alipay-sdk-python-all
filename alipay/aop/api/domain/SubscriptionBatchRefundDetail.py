#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubscriptionBatchRefundDetail(object):

    def __init__(self):
        self._refund_amount = None
        self._refund_status = None
        self._refund_time = None
        self._trade_no = None
        self._trade_refund_id = None

    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def refund_time(self):
        return self._refund_time

    @refund_time.setter
    def refund_time(self, value):
        self._refund_time = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_refund_id(self):
        return self._trade_refund_id

    @trade_refund_id.setter
    def trade_refund_id(self, value):
        self._trade_refund_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_status:
            if hasattr(self.refund_status, 'to_alipay_dict'):
                params['refund_status'] = self.refund_status.to_alipay_dict()
            else:
                params['refund_status'] = self.refund_status
        if self.refund_time:
            if hasattr(self.refund_time, 'to_alipay_dict'):
                params['refund_time'] = self.refund_time.to_alipay_dict()
            else:
                params['refund_time'] = self.refund_time
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_refund_id:
            if hasattr(self.trade_refund_id, 'to_alipay_dict'):
                params['trade_refund_id'] = self.trade_refund_id.to_alipay_dict()
            else:
                params['trade_refund_id'] = self.trade_refund_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubscriptionBatchRefundDetail()
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_status' in d:
            o.refund_status = d['refund_status']
        if 'refund_time' in d:
            o.refund_time = d['refund_time']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_refund_id' in d:
            o.trade_refund_id = d['trade_refund_id']
        return o


