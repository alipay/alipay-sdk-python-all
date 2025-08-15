#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentPayItemVO import RentPayItemVO


class RentOrderPayInfoVO(object):

    def __init__(self):
        self._aftersale_id = None
        self._create_time = None
        self._order_id = None
        self._out_trade_no = None
        self._pay_amount = None
        self._pay_channel = None
        self._pay_items = None
        self._pay_method = None
        self._status = None
        self._trade_no = None

    @property
    def aftersale_id(self):
        return self._aftersale_id

    @aftersale_id.setter
    def aftersale_id(self, value):
        self._aftersale_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value
    @property
    def pay_items(self):
        return self._pay_items

    @pay_items.setter
    def pay_items(self, value):
        if isinstance(value, list):
            self._pay_items = list()
            for i in value:
                if isinstance(i, RentPayItemVO):
                    self._pay_items.append(i)
                else:
                    self._pay_items.append(RentPayItemVO.from_alipay_dict(i))
    @property
    def pay_method(self):
        return self._pay_method

    @pay_method.setter
    def pay_method(self, value):
        self._pay_method = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.aftersale_id:
            if hasattr(self.aftersale_id, 'to_alipay_dict'):
                params['aftersale_id'] = self.aftersale_id.to_alipay_dict()
            else:
                params['aftersale_id'] = self.aftersale_id
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_channel:
            if hasattr(self.pay_channel, 'to_alipay_dict'):
                params['pay_channel'] = self.pay_channel.to_alipay_dict()
            else:
                params['pay_channel'] = self.pay_channel
        if self.pay_items:
            if isinstance(self.pay_items, list):
                for i in range(0, len(self.pay_items)):
                    element = self.pay_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pay_items[i] = element.to_alipay_dict()
            if hasattr(self.pay_items, 'to_alipay_dict'):
                params['pay_items'] = self.pay_items.to_alipay_dict()
            else:
                params['pay_items'] = self.pay_items
        if self.pay_method:
            if hasattr(self.pay_method, 'to_alipay_dict'):
                params['pay_method'] = self.pay_method.to_alipay_dict()
            else:
                params['pay_method'] = self.pay_method
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentOrderPayInfoVO()
        if 'aftersale_id' in d:
            o.aftersale_id = d['aftersale_id']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_channel' in d:
            o.pay_channel = d['pay_channel']
        if 'pay_items' in d:
            o.pay_items = d['pay_items']
        if 'pay_method' in d:
            o.pay_method = d['pay_method']
        if 'status' in d:
            o.status = d['status']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


