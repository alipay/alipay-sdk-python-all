#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecyclinginvoiceOrderAuditItem(object):

    def __init__(self):
        self._item_num = None
        self._item_total_amount = None
        self._item_unit_amount = None
        self._order_item_id = None

    @property
    def item_num(self):
        return self._item_num

    @item_num.setter
    def item_num(self, value):
        self._item_num = value
    @property
    def item_total_amount(self):
        return self._item_total_amount

    @item_total_amount.setter
    def item_total_amount(self, value):
        self._item_total_amount = value
    @property
    def item_unit_amount(self):
        return self._item_unit_amount

    @item_unit_amount.setter
    def item_unit_amount(self, value):
        self._item_unit_amount = value
    @property
    def order_item_id(self):
        return self._order_item_id

    @order_item_id.setter
    def order_item_id(self, value):
        self._order_item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_num:
            if hasattr(self.item_num, 'to_alipay_dict'):
                params['item_num'] = self.item_num.to_alipay_dict()
            else:
                params['item_num'] = self.item_num
        if self.item_total_amount:
            if hasattr(self.item_total_amount, 'to_alipay_dict'):
                params['item_total_amount'] = self.item_total_amount.to_alipay_dict()
            else:
                params['item_total_amount'] = self.item_total_amount
        if self.item_unit_amount:
            if hasattr(self.item_unit_amount, 'to_alipay_dict'):
                params['item_unit_amount'] = self.item_unit_amount.to_alipay_dict()
            else:
                params['item_unit_amount'] = self.item_unit_amount
        if self.order_item_id:
            if hasattr(self.order_item_id, 'to_alipay_dict'):
                params['order_item_id'] = self.order_item_id.to_alipay_dict()
            else:
                params['order_item_id'] = self.order_item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecyclinginvoiceOrderAuditItem()
        if 'item_num' in d:
            o.item_num = d['item_num']
        if 'item_total_amount' in d:
            o.item_total_amount = d['item_total_amount']
        if 'item_unit_amount' in d:
            o.item_unit_amount = d['item_unit_amount']
        if 'order_item_id' in d:
            o.order_item_id = d['order_item_id']
        return o


