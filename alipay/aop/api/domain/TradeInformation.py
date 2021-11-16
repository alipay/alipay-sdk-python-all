#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TradeInformation(object):

    def __init__(self):
        self._commodity_name = None
        self._currency = None
        self._is_l_c_order = None
        self._is_l_c_received_by_one_touch = None
        self._order_amount = None
        self._order_id = None

    @property
    def commodity_name(self):
        return self._commodity_name

    @commodity_name.setter
    def commodity_name(self, value):
        self._commodity_name = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def is_l_c_order(self):
        return self._is_l_c_order

    @is_l_c_order.setter
    def is_l_c_order(self, value):
        self._is_l_c_order = value
    @property
    def is_l_c_received_by_one_touch(self):
        return self._is_l_c_received_by_one_touch

    @is_l_c_received_by_one_touch.setter
    def is_l_c_received_by_one_touch(self, value):
        self._is_l_c_received_by_one_touch = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.commodity_name:
            if hasattr(self.commodity_name, 'to_alipay_dict'):
                params['commodity_name'] = self.commodity_name.to_alipay_dict()
            else:
                params['commodity_name'] = self.commodity_name
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.is_l_c_order:
            if hasattr(self.is_l_c_order, 'to_alipay_dict'):
                params['is_l_c_order'] = self.is_l_c_order.to_alipay_dict()
            else:
                params['is_l_c_order'] = self.is_l_c_order
        if self.is_l_c_received_by_one_touch:
            if hasattr(self.is_l_c_received_by_one_touch, 'to_alipay_dict'):
                params['is_l_c_received_by_one_touch'] = self.is_l_c_received_by_one_touch.to_alipay_dict()
            else:
                params['is_l_c_received_by_one_touch'] = self.is_l_c_received_by_one_touch
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TradeInformation()
        if 'commodity_name' in d:
            o.commodity_name = d['commodity_name']
        if 'currency' in d:
            o.currency = d['currency']
        if 'is_l_c_order' in d:
            o.is_l_c_order = d['is_l_c_order']
        if 'is_l_c_received_by_one_touch' in d:
            o.is_l_c_received_by_one_touch = d['is_l_c_received_by_one_touch']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_id' in d:
            o.order_id = d['order_id']
        return o


