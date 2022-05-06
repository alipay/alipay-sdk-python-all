#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarParkingRefundorderSyncModel(object):

    def __init__(self):
        self._car_number = None
        self._order_no = None
        self._out_refund_no = None
        self._refund_money = None
        self._refund_time = None
        self._user_id = None

    @property
    def car_number(self):
        return self._car_number

    @car_number.setter
    def car_number(self, value):
        self._car_number = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_refund_no(self):
        return self._out_refund_no

    @out_refund_no.setter
    def out_refund_no(self, value):
        self._out_refund_no = value
    @property
    def refund_money(self):
        return self._refund_money

    @refund_money.setter
    def refund_money(self, value):
        self._refund_money = value
    @property
    def refund_time(self):
        return self._refund_time

    @refund_time.setter
    def refund_time(self, value):
        self._refund_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_number:
            if hasattr(self.car_number, 'to_alipay_dict'):
                params['car_number'] = self.car_number.to_alipay_dict()
            else:
                params['car_number'] = self.car_number
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.out_refund_no:
            if hasattr(self.out_refund_no, 'to_alipay_dict'):
                params['out_refund_no'] = self.out_refund_no.to_alipay_dict()
            else:
                params['out_refund_no'] = self.out_refund_no
        if self.refund_money:
            if hasattr(self.refund_money, 'to_alipay_dict'):
                params['refund_money'] = self.refund_money.to_alipay_dict()
            else:
                params['refund_money'] = self.refund_money
        if self.refund_time:
            if hasattr(self.refund_time, 'to_alipay_dict'):
                params['refund_time'] = self.refund_time.to_alipay_dict()
            else:
                params['refund_time'] = self.refund_time
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
        o = AlipayEcoMycarParkingRefundorderSyncModel()
        if 'car_number' in d:
            o.car_number = d['car_number']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_refund_no' in d:
            o.out_refund_no = d['out_refund_no']
        if 'refund_money' in d:
            o.refund_money = d['refund_money']
        if 'refund_time' in d:
            o.refund_time = d['refund_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


