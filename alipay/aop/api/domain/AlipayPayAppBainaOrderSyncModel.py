#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderItemDetail import OrderItemDetail


class AlipayPayAppBainaOrderSyncModel(object):

    def __init__(self):
        self._amount = None
        self._detail = None
        self._detail_flag = None
        self._items = None
        self._lm_order_id = None
        self._main_flag = None
        self._main_lm_order_id = None
        self._modified_time = None
        self._open_id = None
        self._order_status = None
        self._out_request_no = None
        self._pre_order_status = None
        self._user_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, value):
        self._detail = value
    @property
    def detail_flag(self):
        return self._detail_flag

    @detail_flag.setter
    def detail_flag(self, value):
        self._detail_flag = value
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, OrderItemDetail):
                    self._items.append(i)
                else:
                    self._items.append(OrderItemDetail.from_alipay_dict(i))
    @property
    def lm_order_id(self):
        return self._lm_order_id

    @lm_order_id.setter
    def lm_order_id(self, value):
        self._lm_order_id = value
    @property
    def main_flag(self):
        return self._main_flag

    @main_flag.setter
    def main_flag(self, value):
        self._main_flag = value
    @property
    def main_lm_order_id(self):
        return self._main_lm_order_id

    @main_lm_order_id.setter
    def main_lm_order_id(self, value):
        self._main_lm_order_id = value
    @property
    def modified_time(self):
        return self._modified_time

    @modified_time.setter
    def modified_time(self, value):
        self._modified_time = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def pre_order_status(self):
        return self._pre_order_status

    @pre_order_status.setter
    def pre_order_status(self, value):
        self._pre_order_status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.detail:
            if hasattr(self.detail, 'to_alipay_dict'):
                params['detail'] = self.detail.to_alipay_dict()
            else:
                params['detail'] = self.detail
        if self.detail_flag:
            if hasattr(self.detail_flag, 'to_alipay_dict'):
                params['detail_flag'] = self.detail_flag.to_alipay_dict()
            else:
                params['detail_flag'] = self.detail_flag
        if self.items:
            if isinstance(self.items, list):
                for i in range(0, len(self.items)):
                    element = self.items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.items[i] = element.to_alipay_dict()
            if hasattr(self.items, 'to_alipay_dict'):
                params['items'] = self.items.to_alipay_dict()
            else:
                params['items'] = self.items
        if self.lm_order_id:
            if hasattr(self.lm_order_id, 'to_alipay_dict'):
                params['lm_order_id'] = self.lm_order_id.to_alipay_dict()
            else:
                params['lm_order_id'] = self.lm_order_id
        if self.main_flag:
            if hasattr(self.main_flag, 'to_alipay_dict'):
                params['main_flag'] = self.main_flag.to_alipay_dict()
            else:
                params['main_flag'] = self.main_flag
        if self.main_lm_order_id:
            if hasattr(self.main_lm_order_id, 'to_alipay_dict'):
                params['main_lm_order_id'] = self.main_lm_order_id.to_alipay_dict()
            else:
                params['main_lm_order_id'] = self.main_lm_order_id
        if self.modified_time:
            if hasattr(self.modified_time, 'to_alipay_dict'):
                params['modified_time'] = self.modified_time.to_alipay_dict()
            else:
                params['modified_time'] = self.modified_time
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.pre_order_status:
            if hasattr(self.pre_order_status, 'to_alipay_dict'):
                params['pre_order_status'] = self.pre_order_status.to_alipay_dict()
            else:
                params['pre_order_status'] = self.pre_order_status
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
        o = AlipayPayAppBainaOrderSyncModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'detail' in d:
            o.detail = d['detail']
        if 'detail_flag' in d:
            o.detail_flag = d['detail_flag']
        if 'items' in d:
            o.items = d['items']
        if 'lm_order_id' in d:
            o.lm_order_id = d['lm_order_id']
        if 'main_flag' in d:
            o.main_flag = d['main_flag']
        if 'main_lm_order_id' in d:
            o.main_lm_order_id = d['main_lm_order_id']
        if 'modified_time' in d:
            o.modified_time = d['modified_time']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'pre_order_status' in d:
            o.pre_order_status = d['pre_order_status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


