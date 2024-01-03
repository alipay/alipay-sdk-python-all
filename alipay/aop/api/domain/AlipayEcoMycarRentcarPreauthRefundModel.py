#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarRentcarPreauthRefundModel(object):

    def __init__(self):
        self._deduct_out_trade_no = None
        self._open_id = None
        self._out_order_no = None
        self._refund_amount = None
        self._refund_out_request_no = None
        self._refund_reason = None
        self._user_id = None

    @property
    def deduct_out_trade_no(self):
        return self._deduct_out_trade_no

    @deduct_out_trade_no.setter
    def deduct_out_trade_no(self, value):
        self._deduct_out_trade_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_out_request_no(self):
        return self._refund_out_request_no

    @refund_out_request_no.setter
    def refund_out_request_no(self, value):
        self._refund_out_request_no = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.deduct_out_trade_no:
            if hasattr(self.deduct_out_trade_no, 'to_alipay_dict'):
                params['deduct_out_trade_no'] = self.deduct_out_trade_no.to_alipay_dict()
            else:
                params['deduct_out_trade_no'] = self.deduct_out_trade_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_out_request_no:
            if hasattr(self.refund_out_request_no, 'to_alipay_dict'):
                params['refund_out_request_no'] = self.refund_out_request_no.to_alipay_dict()
            else:
                params['refund_out_request_no'] = self.refund_out_request_no
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarRentcarPreauthRefundModel()
        if 'deduct_out_trade_no' in d:
            o.deduct_out_trade_no = d['deduct_out_trade_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_out_request_no' in d:
            o.refund_out_request_no = d['refund_out_request_no']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


