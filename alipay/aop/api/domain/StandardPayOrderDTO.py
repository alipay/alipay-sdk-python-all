#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyDTO import MultiCurrencyMoneyDTO


class StandardPayOrderDTO(object):

    def __init__(self):
        self._create_time = None
        self._finish_time = None
        self._open_id = None
        self._order_status = None
        self._pay_order_id = None
        self._payment_amount = None
        self._payment_request_id = None
        self._user_id = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def finish_time(self):
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value):
        self._finish_time = value
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
    def pay_order_id(self):
        return self._pay_order_id

    @pay_order_id.setter
    def pay_order_id(self, value):
        self._pay_order_id = value
    @property
    def payment_amount(self):
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyDTO):
            self._payment_amount = value
        else:
            self._payment_amount = MultiCurrencyMoneyDTO.from_alipay_dict(value)
    @property
    def payment_request_id(self):
        return self._payment_request_id

    @payment_request_id.setter
    def payment_request_id(self, value):
        self._payment_request_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.finish_time:
            if hasattr(self.finish_time, 'to_alipay_dict'):
                params['finish_time'] = self.finish_time.to_alipay_dict()
            else:
                params['finish_time'] = self.finish_time
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
        if self.pay_order_id:
            if hasattr(self.pay_order_id, 'to_alipay_dict'):
                params['pay_order_id'] = self.pay_order_id.to_alipay_dict()
            else:
                params['pay_order_id'] = self.pay_order_id
        if self.payment_amount:
            if hasattr(self.payment_amount, 'to_alipay_dict'):
                params['payment_amount'] = self.payment_amount.to_alipay_dict()
            else:
                params['payment_amount'] = self.payment_amount
        if self.payment_request_id:
            if hasattr(self.payment_request_id, 'to_alipay_dict'):
                params['payment_request_id'] = self.payment_request_id.to_alipay_dict()
            else:
                params['payment_request_id'] = self.payment_request_id
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
        o = StandardPayOrderDTO()
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'finish_time' in d:
            o.finish_time = d['finish_time']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'pay_order_id' in d:
            o.pay_order_id = d['pay_order_id']
        if 'payment_amount' in d:
            o.payment_amount = d['payment_amount']
        if 'payment_request_id' in d:
            o.payment_request_id = d['payment_request_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


