#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HelloHq import HelloHq


class AlipayDataDataserviceDataQueryModel(object):

    def __init__(self):
        self._amount = None
        self._balance = None
        self._car_keys = None
        self._ext_info = None
        self._hello_hq = None
        self._order_no = None
        self._seats = None
        self._test_g_one = None
        self._total = None
        self._weight = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def car_keys(self):
        return self._car_keys

    @car_keys.setter
    def car_keys(self, value):
        self._car_keys = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def hello_hq(self):
        return self._hello_hq

    @hello_hq.setter
    def hello_hq(self, value):
        if isinstance(value, HelloHq):
            self._hello_hq = value
        else:
            self._hello_hq = HelloHq.from_alipay_dict(value)
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def seats(self):
        return self._seats

    @seats.setter
    def seats(self, value):
        self._seats = value
    @property
    def test_g_one(self):
        return self._test_g_one

    @test_g_one.setter
    def test_g_one(self, value):
        if isinstance(value, list):
            self._test_g_one = list()
            for i in value:
                self._test_g_one.append(i)
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.car_keys:
            if hasattr(self.car_keys, 'to_alipay_dict'):
                params['car_keys'] = self.car_keys.to_alipay_dict()
            else:
                params['car_keys'] = self.car_keys
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.hello_hq:
            if hasattr(self.hello_hq, 'to_alipay_dict'):
                params['hello_hq'] = self.hello_hq.to_alipay_dict()
            else:
                params['hello_hq'] = self.hello_hq
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.seats:
            if hasattr(self.seats, 'to_alipay_dict'):
                params['seats'] = self.seats.to_alipay_dict()
            else:
                params['seats'] = self.seats
        if self.test_g_one:
            if isinstance(self.test_g_one, list):
                for i in range(0, len(self.test_g_one)):
                    element = self.test_g_one[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.test_g_one[i] = element.to_alipay_dict()
            if hasattr(self.test_g_one, 'to_alipay_dict'):
                params['test_g_one'] = self.test_g_one.to_alipay_dict()
            else:
                params['test_g_one'] = self.test_g_one
        if self.total:
            if hasattr(self.total, 'to_alipay_dict'):
                params['total'] = self.total.to_alipay_dict()
            else:
                params['total'] = self.total
        if self.weight:
            if hasattr(self.weight, 'to_alipay_dict'):
                params['weight'] = self.weight.to_alipay_dict()
            else:
                params['weight'] = self.weight
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceDataQueryModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'balance' in d:
            o.balance = d['balance']
        if 'car_keys' in d:
            o.car_keys = d['car_keys']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'hello_hq' in d:
            o.hello_hq = d['hello_hq']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'seats' in d:
            o.seats = d['seats']
        if 'test_g_one' in d:
            o.test_g_one = d['test_g_one']
        if 'total' in d:
            o.total = d['total']
        if 'weight' in d:
            o.weight = d['weight']
        return o


