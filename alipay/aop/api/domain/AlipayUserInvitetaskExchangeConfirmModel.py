#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserInvitetaskExchangeConfirmModel(object):

    def __init__(self):
        self._exchange_amount_money = None
        self._exchange_type = None
        self._order_id = None
        self._out_biz_no = None
        self._product_id = None
        self._task_process_id = None
        self._user_id = None

    @property
    def exchange_amount_money(self):
        return self._exchange_amount_money

    @exchange_amount_money.setter
    def exchange_amount_money(self, value):
        self._exchange_amount_money = value
    @property
    def exchange_type(self):
        return self._exchange_type

    @exchange_type.setter
    def exchange_type(self, value):
        self._exchange_type = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def task_process_id(self):
        return self._task_process_id

    @task_process_id.setter
    def task_process_id(self, value):
        self._task_process_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.exchange_amount_money:
            if hasattr(self.exchange_amount_money, 'to_alipay_dict'):
                params['exchange_amount_money'] = self.exchange_amount_money.to_alipay_dict()
            else:
                params['exchange_amount_money'] = self.exchange_amount_money
        if self.exchange_type:
            if hasattr(self.exchange_type, 'to_alipay_dict'):
                params['exchange_type'] = self.exchange_type.to_alipay_dict()
            else:
                params['exchange_type'] = self.exchange_type
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.task_process_id:
            if hasattr(self.task_process_id, 'to_alipay_dict'):
                params['task_process_id'] = self.task_process_id.to_alipay_dict()
            else:
                params['task_process_id'] = self.task_process_id
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
        o = AlipayUserInvitetaskExchangeConfirmModel()
        if 'exchange_amount_money' in d:
            o.exchange_amount_money = d['exchange_amount_money']
        if 'exchange_type' in d:
            o.exchange_type = d['exchange_type']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'task_process_id' in d:
            o.task_process_id = d['task_process_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


