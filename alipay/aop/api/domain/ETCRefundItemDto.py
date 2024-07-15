#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ETCRefundItemDto(object):

    def __init__(self):
        self._item_category = None
        self._item_refund_amount = None
        self._out_trip_id = None

    @property
    def item_category(self):
        return self._item_category

    @item_category.setter
    def item_category(self, value):
        self._item_category = value
    @property
    def item_refund_amount(self):
        return self._item_refund_amount

    @item_refund_amount.setter
    def item_refund_amount(self, value):
        self._item_refund_amount = value
    @property
    def out_trip_id(self):
        return self._out_trip_id

    @out_trip_id.setter
    def out_trip_id(self, value):
        self._out_trip_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_category:
            if hasattr(self.item_category, 'to_alipay_dict'):
                params['item_category'] = self.item_category.to_alipay_dict()
            else:
                params['item_category'] = self.item_category
        if self.item_refund_amount:
            if hasattr(self.item_refund_amount, 'to_alipay_dict'):
                params['item_refund_amount'] = self.item_refund_amount.to_alipay_dict()
            else:
                params['item_refund_amount'] = self.item_refund_amount
        if self.out_trip_id:
            if hasattr(self.out_trip_id, 'to_alipay_dict'):
                params['out_trip_id'] = self.out_trip_id.to_alipay_dict()
            else:
                params['out_trip_id'] = self.out_trip_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ETCRefundItemDto()
        if 'item_category' in d:
            o.item_category = d['item_category']
        if 'item_refund_amount' in d:
            o.item_refund_amount = d['item_refund_amount']
        if 'out_trip_id' in d:
            o.out_trip_id = d['out_trip_id']
        return o


