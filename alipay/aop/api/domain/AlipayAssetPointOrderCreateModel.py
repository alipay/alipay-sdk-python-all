#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAssetPointOrderCreateModel(object):

    def __init__(self):
        self._memo = None
        self._merchant_order_no = None
        self._order_time = None
        self._point_count = None
        self._user_symbol = None
        self._user_symbol_type = None

    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def point_count(self):
        return self._point_count

    @point_count.setter
    def point_count(self, value):
        self._point_count = value
    @property
    def user_symbol(self):
        return self._user_symbol

    @user_symbol.setter
    def user_symbol(self, value):
        self._user_symbol = value
    @property
    def user_symbol_type(self):
        return self._user_symbol_type

    @user_symbol_type.setter
    def user_symbol_type(self, value):
        self._user_symbol_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        if self.point_count:
            if hasattr(self.point_count, 'to_alipay_dict'):
                params['point_count'] = self.point_count.to_alipay_dict()
            else:
                params['point_count'] = self.point_count
        if self.user_symbol:
            if hasattr(self.user_symbol, 'to_alipay_dict'):
                params['user_symbol'] = self.user_symbol.to_alipay_dict()
            else:
                params['user_symbol'] = self.user_symbol
        if self.user_symbol_type:
            if hasattr(self.user_symbol_type, 'to_alipay_dict'):
                params['user_symbol_type'] = self.user_symbol_type.to_alipay_dict()
            else:
                params['user_symbol_type'] = self.user_symbol_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAssetPointOrderCreateModel()
        if 'memo' in d:
            o.memo = d['memo']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'order_time' in d:
            o.order_time = d['order_time']
        if 'point_count' in d:
            o.point_count = d['point_count']
        if 'user_symbol' in d:
            o.user_symbol = d['user_symbol']
        if 'user_symbol_type' in d:
            o.user_symbol_type = d['user_symbol_type']
        return o


