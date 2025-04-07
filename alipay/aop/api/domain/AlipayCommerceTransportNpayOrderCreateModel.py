#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportNpayOrderCreateModel(object):

    def __init__(self):
        self._amount = None
        self._channel = None
        self._out_order_no = None
        self._sn = None
        self._trip_info = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def trip_info(self):
        return self._trip_info

    @trip_info.setter
    def trip_info(self, value):
        self._trip_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.trip_info:
            if hasattr(self.trip_info, 'to_alipay_dict'):
                params['trip_info'] = self.trip_info.to_alipay_dict()
            else:
                params['trip_info'] = self.trip_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportNpayOrderCreateModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'channel' in d:
            o.channel = d['channel']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'sn' in d:
            o.sn = d['sn']
        if 'trip_info' in d:
            o.trip_info = d['trip_info']
        return o


