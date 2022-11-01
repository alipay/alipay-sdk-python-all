#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcomItemDTO import EcomItemDTO


class EcomSubOrderDTO(object):

    def __init__(self):
        self._buy_amount = None
        self._gmt_create = None
        self._item = None
        self._order_fee = None
        self._order_id = None
        self._trade_end_time = None

    @property
    def buy_amount(self):
        return self._buy_amount

    @buy_amount.setter
    def buy_amount(self, value):
        self._buy_amount = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, value):
        if isinstance(value, EcomItemDTO):
            self._item = value
        else:
            self._item = EcomItemDTO.from_alipay_dict(value)
    @property
    def order_fee(self):
        return self._order_fee

    @order_fee.setter
    def order_fee(self, value):
        self._order_fee = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def trade_end_time(self):
        return self._trade_end_time

    @trade_end_time.setter
    def trade_end_time(self, value):
        self._trade_end_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.buy_amount:
            if hasattr(self.buy_amount, 'to_alipay_dict'):
                params['buy_amount'] = self.buy_amount.to_alipay_dict()
            else:
                params['buy_amount'] = self.buy_amount
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.item:
            if hasattr(self.item, 'to_alipay_dict'):
                params['item'] = self.item.to_alipay_dict()
            else:
                params['item'] = self.item
        if self.order_fee:
            if hasattr(self.order_fee, 'to_alipay_dict'):
                params['order_fee'] = self.order_fee.to_alipay_dict()
            else:
                params['order_fee'] = self.order_fee
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.trade_end_time:
            if hasattr(self.trade_end_time, 'to_alipay_dict'):
                params['trade_end_time'] = self.trade_end_time.to_alipay_dict()
            else:
                params['trade_end_time'] = self.trade_end_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcomSubOrderDTO()
        if 'buy_amount' in d:
            o.buy_amount = d['buy_amount']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'item' in d:
            o.item = d['item']
        if 'order_fee' in d:
            o.order_fee = d['order_fee']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'trade_end_time' in d:
            o.trade_end_time = d['trade_end_time']
        return o


