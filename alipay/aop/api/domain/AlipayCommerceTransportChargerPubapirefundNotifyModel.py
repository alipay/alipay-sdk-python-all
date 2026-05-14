#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportChargerPubapirefundNotifyModel(object):

    def __init__(self):
        self._open_id = None
        self._refund_amount = None
        self._refund_order_id = None
        self._refund_reason = None
        self._refund_result = None
        self._refund_time = None
        self._start_charge_seq = None
        self._trade_no = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
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
    def refund_result(self):
        return self._refund_result

    @refund_result.setter
    def refund_result(self, value):
        self._refund_result = value
    @property
    def refund_time(self):
        return self._refund_time

    @refund_time.setter
    def refund_time(self, value):
        self._refund_time = value
    @property
    def start_charge_seq(self):
        return self._start_charge_seq

    @start_charge_seq.setter
    def start_charge_seq(self, value):
        self._start_charge_seq = value
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
        if self.refund_result:
            if hasattr(self.refund_result, 'to_alipay_dict'):
                params['refund_result'] = self.refund_result.to_alipay_dict()
            else:
                params['refund_result'] = self.refund_result
        if self.refund_time:
            if hasattr(self.refund_time, 'to_alipay_dict'):
                params['refund_time'] = self.refund_time.to_alipay_dict()
            else:
                params['refund_time'] = self.refund_time
        if self.start_charge_seq:
            if hasattr(self.start_charge_seq, 'to_alipay_dict'):
                params['start_charge_seq'] = self.start_charge_seq.to_alipay_dict()
            else:
                params['start_charge_seq'] = self.start_charge_seq
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
        o = AlipayCommerceTransportChargerPubapirefundNotifyModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_order_id' in d:
            o.refund_order_id = d['refund_order_id']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'refund_result' in d:
            o.refund_result = d['refund_result']
        if 'refund_time' in d:
            o.refund_time = d['refund_time']
        if 'start_charge_seq' in d:
            o.start_charge_seq = d['start_charge_seq']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


