#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TimeCardSimpleItemInfo import TimeCardSimpleItemInfo


class TimeCardOrderInfo(object):

    def __init__(self):
        self._item_id = None
        self._order_amount = None
        self._order_date = None
        self._order_id = None
        self._time_card_info = None
        self._user_id = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_date(self):
        return self._order_date

    @order_date.setter
    def order_date(self, value):
        self._order_date = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def time_card_info(self):
        return self._time_card_info

    @time_card_info.setter
    def time_card_info(self, value):
        if isinstance(value, TimeCardSimpleItemInfo):
            self._time_card_info = value
        else:
            self._time_card_info = TimeCardSimpleItemInfo.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_date:
            if hasattr(self.order_date, 'to_alipay_dict'):
                params['order_date'] = self.order_date.to_alipay_dict()
            else:
                params['order_date'] = self.order_date
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.time_card_info:
            if hasattr(self.time_card_info, 'to_alipay_dict'):
                params['time_card_info'] = self.time_card_info.to_alipay_dict()
            else:
                params['time_card_info'] = self.time_card_info
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
        o = TimeCardOrderInfo()
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_date' in d:
            o.order_date = d['order_date']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'time_card_info' in d:
            o.time_card_info = d['time_card_info']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


