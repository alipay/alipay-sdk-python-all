#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FreightFlowWaybillInfo(object):

    def __init__(self):
        self._amount = None
        self._delivery_address = None
        self._order_accept_time = None
        self._order_finish_time = None
        self._order_time = None
        self._shipping_address = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def delivery_address(self):
        return self._delivery_address

    @delivery_address.setter
    def delivery_address(self, value):
        self._delivery_address = value
    @property
    def order_accept_time(self):
        return self._order_accept_time

    @order_accept_time.setter
    def order_accept_time(self, value):
        self._order_accept_time = value
    @property
    def order_finish_time(self):
        return self._order_finish_time

    @order_finish_time.setter
    def order_finish_time(self, value):
        self._order_finish_time = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def shipping_address(self):
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, value):
        self._shipping_address = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.delivery_address:
            if hasattr(self.delivery_address, 'to_alipay_dict'):
                params['delivery_address'] = self.delivery_address.to_alipay_dict()
            else:
                params['delivery_address'] = self.delivery_address
        if self.order_accept_time:
            if hasattr(self.order_accept_time, 'to_alipay_dict'):
                params['order_accept_time'] = self.order_accept_time.to_alipay_dict()
            else:
                params['order_accept_time'] = self.order_accept_time
        if self.order_finish_time:
            if hasattr(self.order_finish_time, 'to_alipay_dict'):
                params['order_finish_time'] = self.order_finish_time.to_alipay_dict()
            else:
                params['order_finish_time'] = self.order_finish_time
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        if self.shipping_address:
            if hasattr(self.shipping_address, 'to_alipay_dict'):
                params['shipping_address'] = self.shipping_address.to_alipay_dict()
            else:
                params['shipping_address'] = self.shipping_address
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FreightFlowWaybillInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'delivery_address' in d:
            o.delivery_address = d['delivery_address']
        if 'order_accept_time' in d:
            o.order_accept_time = d['order_accept_time']
        if 'order_finish_time' in d:
            o.order_finish_time = d['order_finish_time']
        if 'order_time' in d:
            o.order_time = d['order_time']
        if 'shipping_address' in d:
            o.shipping_address = d['shipping_address']
        return o


