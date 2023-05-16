#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BillResult(object):

    def __init__(self):
        self._activity_batch_no = None
        self._activity_type = None
        self._bank_bill_no = None
        self._bank_discount_amount = None
        self._card_type = None
        self._discount_name = None
        self._order_amount = None
        self._pay_date = None
        self._pay_time = None
        self._real_pay_amount = None
        self._scene = None
        self._sub_scene = None
        self._trade_channel = None

    @property
    def activity_batch_no(self):
        return self._activity_batch_no

    @activity_batch_no.setter
    def activity_batch_no(self, value):
        self._activity_batch_no = value
    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def bank_bill_no(self):
        return self._bank_bill_no

    @bank_bill_no.setter
    def bank_bill_no(self, value):
        self._bank_bill_no = value
    @property
    def bank_discount_amount(self):
        return self._bank_discount_amount

    @bank_discount_amount.setter
    def bank_discount_amount(self, value):
        self._bank_discount_amount = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def discount_name(self):
        return self._discount_name

    @discount_name.setter
    def discount_name(self, value):
        self._discount_name = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def pay_date(self):
        return self._pay_date

    @pay_date.setter
    def pay_date(self, value):
        self._pay_date = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def real_pay_amount(self):
        return self._real_pay_amount

    @real_pay_amount.setter
    def real_pay_amount(self, value):
        self._real_pay_amount = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def sub_scene(self):
        return self._sub_scene

    @sub_scene.setter
    def sub_scene(self, value):
        self._sub_scene = value
    @property
    def trade_channel(self):
        return self._trade_channel

    @trade_channel.setter
    def trade_channel(self, value):
        self._trade_channel = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_batch_no:
            if hasattr(self.activity_batch_no, 'to_alipay_dict'):
                params['activity_batch_no'] = self.activity_batch_no.to_alipay_dict()
            else:
                params['activity_batch_no'] = self.activity_batch_no
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
        if self.bank_bill_no:
            if hasattr(self.bank_bill_no, 'to_alipay_dict'):
                params['bank_bill_no'] = self.bank_bill_no.to_alipay_dict()
            else:
                params['bank_bill_no'] = self.bank_bill_no
        if self.bank_discount_amount:
            if hasattr(self.bank_discount_amount, 'to_alipay_dict'):
                params['bank_discount_amount'] = self.bank_discount_amount.to_alipay_dict()
            else:
                params['bank_discount_amount'] = self.bank_discount_amount
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.discount_name:
            if hasattr(self.discount_name, 'to_alipay_dict'):
                params['discount_name'] = self.discount_name.to_alipay_dict()
            else:
                params['discount_name'] = self.discount_name
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.pay_date:
            if hasattr(self.pay_date, 'to_alipay_dict'):
                params['pay_date'] = self.pay_date.to_alipay_dict()
            else:
                params['pay_date'] = self.pay_date
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.real_pay_amount:
            if hasattr(self.real_pay_amount, 'to_alipay_dict'):
                params['real_pay_amount'] = self.real_pay_amount.to_alipay_dict()
            else:
                params['real_pay_amount'] = self.real_pay_amount
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.sub_scene:
            if hasattr(self.sub_scene, 'to_alipay_dict'):
                params['sub_scene'] = self.sub_scene.to_alipay_dict()
            else:
                params['sub_scene'] = self.sub_scene
        if self.trade_channel:
            if hasattr(self.trade_channel, 'to_alipay_dict'):
                params['trade_channel'] = self.trade_channel.to_alipay_dict()
            else:
                params['trade_channel'] = self.trade_channel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BillResult()
        if 'activity_batch_no' in d:
            o.activity_batch_no = d['activity_batch_no']
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'bank_bill_no' in d:
            o.bank_bill_no = d['bank_bill_no']
        if 'bank_discount_amount' in d:
            o.bank_discount_amount = d['bank_discount_amount']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'discount_name' in d:
            o.discount_name = d['discount_name']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'pay_date' in d:
            o.pay_date = d['pay_date']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'real_pay_amount' in d:
            o.real_pay_amount = d['real_pay_amount']
        if 'scene' in d:
            o.scene = d['scene']
        if 'sub_scene' in d:
            o.sub_scene = d['sub_scene']
        if 'trade_channel' in d:
            o.trade_channel = d['trade_channel']
        return o


