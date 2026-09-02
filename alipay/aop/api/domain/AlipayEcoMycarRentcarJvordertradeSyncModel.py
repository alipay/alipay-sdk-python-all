#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarRentcarJvordertradeSyncModel(object):

    def __init__(self):
        self._open_id = None
        self._order_type = None
        self._out_order_no = None
        self._out_trade_no = None
        self._out_trade_order_no = None
        self._pay_status = None
        self._refund_status = None
        self._total_amount = None
        self._trade_app_id = None
        self._trade_app_name = None
        self._trade_no = None
        self._trade_pid = None
        self._trade_time = None
        self._trade_type = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def out_trade_order_no(self):
        return self._out_trade_order_no

    @out_trade_order_no.setter
    def out_trade_order_no(self, value):
        self._out_trade_order_no = value
    @property
    def pay_status(self):
        return self._pay_status

    @pay_status.setter
    def pay_status(self, value):
        self._pay_status = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_app_id(self):
        return self._trade_app_id

    @trade_app_id.setter
    def trade_app_id(self, value):
        self._trade_app_id = value
    @property
    def trade_app_name(self):
        return self._trade_app_name

    @trade_app_name.setter
    def trade_app_name(self, value):
        self._trade_app_name = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_pid(self):
        return self._trade_pid

    @trade_pid.setter
    def trade_pid(self, value):
        self._trade_pid = value
    @property
    def trade_time(self):
        return self._trade_time

    @trade_time.setter
    def trade_time(self, value):
        self._trade_time = value
    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        self._trade_type = value
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
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.out_trade_order_no:
            if hasattr(self.out_trade_order_no, 'to_alipay_dict'):
                params['out_trade_order_no'] = self.out_trade_order_no.to_alipay_dict()
            else:
                params['out_trade_order_no'] = self.out_trade_order_no
        if self.pay_status:
            if hasattr(self.pay_status, 'to_alipay_dict'):
                params['pay_status'] = self.pay_status.to_alipay_dict()
            else:
                params['pay_status'] = self.pay_status
        if self.refund_status:
            if hasattr(self.refund_status, 'to_alipay_dict'):
                params['refund_status'] = self.refund_status.to_alipay_dict()
            else:
                params['refund_status'] = self.refund_status
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.trade_app_id:
            if hasattr(self.trade_app_id, 'to_alipay_dict'):
                params['trade_app_id'] = self.trade_app_id.to_alipay_dict()
            else:
                params['trade_app_id'] = self.trade_app_id
        if self.trade_app_name:
            if hasattr(self.trade_app_name, 'to_alipay_dict'):
                params['trade_app_name'] = self.trade_app_name.to_alipay_dict()
            else:
                params['trade_app_name'] = self.trade_app_name
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_pid:
            if hasattr(self.trade_pid, 'to_alipay_dict'):
                params['trade_pid'] = self.trade_pid.to_alipay_dict()
            else:
                params['trade_pid'] = self.trade_pid
        if self.trade_time:
            if hasattr(self.trade_time, 'to_alipay_dict'):
                params['trade_time'] = self.trade_time.to_alipay_dict()
            else:
                params['trade_time'] = self.trade_time
        if self.trade_type:
            if hasattr(self.trade_type, 'to_alipay_dict'):
                params['trade_type'] = self.trade_type.to_alipay_dict()
            else:
                params['trade_type'] = self.trade_type
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
        o = AlipayEcoMycarRentcarJvordertradeSyncModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'out_trade_order_no' in d:
            o.out_trade_order_no = d['out_trade_order_no']
        if 'pay_status' in d:
            o.pay_status = d['pay_status']
        if 'refund_status' in d:
            o.refund_status = d['refund_status']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_app_id' in d:
            o.trade_app_id = d['trade_app_id']
        if 'trade_app_name' in d:
            o.trade_app_name = d['trade_app_name']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_pid' in d:
            o.trade_pid = d['trade_pid']
        if 'trade_time' in d:
            o.trade_time = d['trade_time']
        if 'trade_type' in d:
            o.trade_type = d['trade_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


