#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeviceTradeDetail(object):

    def __init__(self):
        self._device_sn = None
        self._item_name = None
        self._max_dt = None
        self._pay_mode = None
        self._trade_amt = None
        self._trade_no = None
        self._trade_time = None

    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def max_dt(self):
        return self._max_dt

    @max_dt.setter
    def max_dt(self, value):
        self._max_dt = value
    @property
    def pay_mode(self):
        return self._pay_mode

    @pay_mode.setter
    def pay_mode(self, value):
        self._pay_mode = value
    @property
    def trade_amt(self):
        return self._trade_amt

    @trade_amt.setter
    def trade_amt(self, value):
        self._trade_amt = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_time(self):
        return self._trade_time

    @trade_time.setter
    def trade_time(self, value):
        self._trade_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.max_dt:
            if hasattr(self.max_dt, 'to_alipay_dict'):
                params['max_dt'] = self.max_dt.to_alipay_dict()
            else:
                params['max_dt'] = self.max_dt
        if self.pay_mode:
            if hasattr(self.pay_mode, 'to_alipay_dict'):
                params['pay_mode'] = self.pay_mode.to_alipay_dict()
            else:
                params['pay_mode'] = self.pay_mode
        if self.trade_amt:
            if hasattr(self.trade_amt, 'to_alipay_dict'):
                params['trade_amt'] = self.trade_amt.to_alipay_dict()
            else:
                params['trade_amt'] = self.trade_amt
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_time:
            if hasattr(self.trade_time, 'to_alipay_dict'):
                params['trade_time'] = self.trade_time.to_alipay_dict()
            else:
                params['trade_time'] = self.trade_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeviceTradeDetail()
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'max_dt' in d:
            o.max_dt = d['max_dt']
        if 'pay_mode' in d:
            o.pay_mode = d['pay_mode']
        if 'trade_amt' in d:
            o.trade_amt = d['trade_amt']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_time' in d:
            o.trade_time = d['trade_time']
        return o


