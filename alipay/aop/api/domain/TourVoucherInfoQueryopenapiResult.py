#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TourVoucherInfoQueryopenapiResult(object):

    def __init__(self):
        self._effective_time_end = None
        self._effective_time_start = None
        self._exp_date = None
        self._item_id = None
        self._refund_amount = None
        self._refund_order_id = None
        self._refund_reason = None
        self._status = None
        self._voucher_id = None

    @property
    def effective_time_end(self):
        return self._effective_time_end

    @effective_time_end.setter
    def effective_time_end(self, value):
        self._effective_time_end = value
    @property
    def effective_time_start(self):
        return self._effective_time_start

    @effective_time_start.setter
    def effective_time_start(self, value):
        self._effective_time_start = value
    @property
    def exp_date(self):
        return self._exp_date

    @exp_date.setter
    def exp_date(self, value):
        self._exp_date = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_order_id(self):
        return self._refund_order_id

    @refund_order_id.setter
    def refund_order_id(self, value):
        self._refund_order_id = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.effective_time_end:
            if hasattr(self.effective_time_end, 'to_alipay_dict'):
                params['effective_time_end'] = self.effective_time_end.to_alipay_dict()
            else:
                params['effective_time_end'] = self.effective_time_end
        if self.effective_time_start:
            if hasattr(self.effective_time_start, 'to_alipay_dict'):
                params['effective_time_start'] = self.effective_time_start.to_alipay_dict()
            else:
                params['effective_time_start'] = self.effective_time_start
        if self.exp_date:
            if hasattr(self.exp_date, 'to_alipay_dict'):
                params['exp_date'] = self.exp_date.to_alipay_dict()
            else:
                params['exp_date'] = self.exp_date
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_order_id:
            if hasattr(self.refund_order_id, 'to_alipay_dict'):
                params['refund_order_id'] = self.refund_order_id.to_alipay_dict()
            else:
                params['refund_order_id'] = self.refund_order_id
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TourVoucherInfoQueryopenapiResult()
        if 'effective_time_end' in d:
            o.effective_time_end = d['effective_time_end']
        if 'effective_time_start' in d:
            o.effective_time_start = d['effective_time_start']
        if 'exp_date' in d:
            o.exp_date = d['exp_date']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_order_id' in d:
            o.refund_order_id = d['refund_order_id']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'status' in d:
            o.status = d['status']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


