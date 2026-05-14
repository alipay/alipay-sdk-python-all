#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceResaleOrderRefundModel(object):

    def __init__(self):
        self._open_id = None
        self._out_order_id = None
        self._out_refund_id = None
        self._refund_amount = None
        self._refund_amount_type = None
        self._refund_memo = None
        self._trade_no = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def out_refund_id(self):
        return self._out_refund_id

    @out_refund_id.setter
    def out_refund_id(self, value):
        self._out_refund_id = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_amount_type(self):
        return self._refund_amount_type

    @refund_amount_type.setter
    def refund_amount_type(self, value):
        self._refund_amount_type = value
    @property
    def refund_memo(self):
        return self._refund_memo

    @refund_memo.setter
    def refund_memo(self, value):
        self._refund_memo = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.out_refund_id:
            if hasattr(self.out_refund_id, 'to_alipay_dict'):
                params['out_refund_id'] = self.out_refund_id.to_alipay_dict()
            else:
                params['out_refund_id'] = self.out_refund_id
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_amount_type:
            if hasattr(self.refund_amount_type, 'to_alipay_dict'):
                params['refund_amount_type'] = self.refund_amount_type.to_alipay_dict()
            else:
                params['refund_amount_type'] = self.refund_amount_type
        if self.refund_memo:
            if hasattr(self.refund_memo, 'to_alipay_dict'):
                params['refund_memo'] = self.refund_memo.to_alipay_dict()
            else:
                params['refund_memo'] = self.refund_memo
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
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
        o = AlipayCommerceResaleOrderRefundModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'out_refund_id' in d:
            o.out_refund_id = d['out_refund_id']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_amount_type' in d:
            o.refund_amount_type = d['refund_amount_type']
        if 'refund_memo' in d:
            o.refund_memo = d['refund_memo']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


