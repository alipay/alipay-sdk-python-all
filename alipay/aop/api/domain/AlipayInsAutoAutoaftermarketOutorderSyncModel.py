#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsAutoAutoaftermarketOutorderSyncModel(object):

    def __init__(self):
        self._action = None
        self._actual_pay_amount = None
        self._alipay_id = None
        self._biz_time = None
        self._category = None
        self._out_order_no = None
        self._pay_trade_no = None
        self._prod_title = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def actual_pay_amount(self):
        return self._actual_pay_amount

    @actual_pay_amount.setter
    def actual_pay_amount(self, value):
        self._actual_pay_amount = value
    @property
    def alipay_id(self):
        return self._alipay_id

    @alipay_id.setter
    def alipay_id(self, value):
        self._alipay_id = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def pay_trade_no(self):
        return self._pay_trade_no

    @pay_trade_no.setter
    def pay_trade_no(self, value):
        self._pay_trade_no = value
    @property
    def prod_title(self):
        return self._prod_title

    @prod_title.setter
    def prod_title(self, value):
        self._prod_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.actual_pay_amount:
            if hasattr(self.actual_pay_amount, 'to_alipay_dict'):
                params['actual_pay_amount'] = self.actual_pay_amount.to_alipay_dict()
            else:
                params['actual_pay_amount'] = self.actual_pay_amount
        if self.alipay_id:
            if hasattr(self.alipay_id, 'to_alipay_dict'):
                params['alipay_id'] = self.alipay_id.to_alipay_dict()
            else:
                params['alipay_id'] = self.alipay_id
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.pay_trade_no:
            if hasattr(self.pay_trade_no, 'to_alipay_dict'):
                params['pay_trade_no'] = self.pay_trade_no.to_alipay_dict()
            else:
                params['pay_trade_no'] = self.pay_trade_no
        if self.prod_title:
            if hasattr(self.prod_title, 'to_alipay_dict'):
                params['prod_title'] = self.prod_title.to_alipay_dict()
            else:
                params['prod_title'] = self.prod_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsAutoAutoaftermarketOutorderSyncModel()
        if 'action' in d:
            o.action = d['action']
        if 'actual_pay_amount' in d:
            o.actual_pay_amount = d['actual_pay_amount']
        if 'alipay_id' in d:
            o.alipay_id = d['alipay_id']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'category' in d:
            o.category = d['category']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'pay_trade_no' in d:
            o.pay_trade_no = d['pay_trade_no']
        if 'prod_title' in d:
            o.prod_title = d['prod_title']
        return o


