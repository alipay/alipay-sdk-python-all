#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UseDuration import UseDuration


class MoneyCardInfo(object):

    def __init__(self):
        self._effective_duration = None
        self._hotline = None
        self._limit_num = None
        self._limit_type = None
        self._origin_price = None
        self._pids = None
        self._remain_stock = None
        self._sale_price = None
        self._stock_num = None
        self._support_withdraw = None
        self._use_duration = None
        self._use_type = None

    @property
    def effective_duration(self):
        return self._effective_duration

    @effective_duration.setter
    def effective_duration(self, value):
        self._effective_duration = value
    @property
    def hotline(self):
        return self._hotline

    @hotline.setter
    def hotline(self, value):
        self._hotline = value
    @property
    def limit_num(self):
        return self._limit_num

    @limit_num.setter
    def limit_num(self, value):
        self._limit_num = value
    @property
    def limit_type(self):
        return self._limit_type

    @limit_type.setter
    def limit_type(self, value):
        self._limit_type = value
    @property
    def origin_price(self):
        return self._origin_price

    @origin_price.setter
    def origin_price(self, value):
        self._origin_price = value
    @property
    def pids(self):
        return self._pids

    @pids.setter
    def pids(self, value):
        if isinstance(value, list):
            self._pids = list()
            for i in value:
                self._pids.append(i)
    @property
    def remain_stock(self):
        return self._remain_stock

    @remain_stock.setter
    def remain_stock(self, value):
        self._remain_stock = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def stock_num(self):
        return self._stock_num

    @stock_num.setter
    def stock_num(self, value):
        self._stock_num = value
    @property
    def support_withdraw(self):
        return self._support_withdraw

    @support_withdraw.setter
    def support_withdraw(self, value):
        self._support_withdraw = value
    @property
    def use_duration(self):
        return self._use_duration

    @use_duration.setter
    def use_duration(self, value):
        if isinstance(value, UseDuration):
            self._use_duration = value
        else:
            self._use_duration = UseDuration.from_alipay_dict(value)
    @property
    def use_type(self):
        return self._use_type

    @use_type.setter
    def use_type(self, value):
        self._use_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.effective_duration:
            if hasattr(self.effective_duration, 'to_alipay_dict'):
                params['effective_duration'] = self.effective_duration.to_alipay_dict()
            else:
                params['effective_duration'] = self.effective_duration
        if self.hotline:
            if hasattr(self.hotline, 'to_alipay_dict'):
                params['hotline'] = self.hotline.to_alipay_dict()
            else:
                params['hotline'] = self.hotline
        if self.limit_num:
            if hasattr(self.limit_num, 'to_alipay_dict'):
                params['limit_num'] = self.limit_num.to_alipay_dict()
            else:
                params['limit_num'] = self.limit_num
        if self.limit_type:
            if hasattr(self.limit_type, 'to_alipay_dict'):
                params['limit_type'] = self.limit_type.to_alipay_dict()
            else:
                params['limit_type'] = self.limit_type
        if self.origin_price:
            if hasattr(self.origin_price, 'to_alipay_dict'):
                params['origin_price'] = self.origin_price.to_alipay_dict()
            else:
                params['origin_price'] = self.origin_price
        if self.pids:
            if isinstance(self.pids, list):
                for i in range(0, len(self.pids)):
                    element = self.pids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pids[i] = element.to_alipay_dict()
            if hasattr(self.pids, 'to_alipay_dict'):
                params['pids'] = self.pids.to_alipay_dict()
            else:
                params['pids'] = self.pids
        if self.remain_stock:
            if hasattr(self.remain_stock, 'to_alipay_dict'):
                params['remain_stock'] = self.remain_stock.to_alipay_dict()
            else:
                params['remain_stock'] = self.remain_stock
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.stock_num:
            if hasattr(self.stock_num, 'to_alipay_dict'):
                params['stock_num'] = self.stock_num.to_alipay_dict()
            else:
                params['stock_num'] = self.stock_num
        if self.support_withdraw:
            if hasattr(self.support_withdraw, 'to_alipay_dict'):
                params['support_withdraw'] = self.support_withdraw.to_alipay_dict()
            else:
                params['support_withdraw'] = self.support_withdraw
        if self.use_duration:
            if hasattr(self.use_duration, 'to_alipay_dict'):
                params['use_duration'] = self.use_duration.to_alipay_dict()
            else:
                params['use_duration'] = self.use_duration
        if self.use_type:
            if hasattr(self.use_type, 'to_alipay_dict'):
                params['use_type'] = self.use_type.to_alipay_dict()
            else:
                params['use_type'] = self.use_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MoneyCardInfo()
        if 'effective_duration' in d:
            o.effective_duration = d['effective_duration']
        if 'hotline' in d:
            o.hotline = d['hotline']
        if 'limit_num' in d:
            o.limit_num = d['limit_num']
        if 'limit_type' in d:
            o.limit_type = d['limit_type']
        if 'origin_price' in d:
            o.origin_price = d['origin_price']
        if 'pids' in d:
            o.pids = d['pids']
        if 'remain_stock' in d:
            o.remain_stock = d['remain_stock']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'stock_num' in d:
            o.stock_num = d['stock_num']
        if 'support_withdraw' in d:
            o.support_withdraw = d['support_withdraw']
        if 'use_duration' in d:
            o.use_duration = d['use_duration']
        if 'use_type' in d:
            o.use_type = d['use_type']
        return o


