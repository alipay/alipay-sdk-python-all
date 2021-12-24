#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationPromoterExchangeSubmitModel(object):

    def __init__(self):
        self._exchange_token = None
        self._item_code = None
        self._pid = None
        self._point_amount = None
        self._task_code = None
        self._user_id = None

    @property
    def exchange_token(self):
        return self._exchange_token

    @exchange_token.setter
    def exchange_token(self, value):
        self._exchange_token = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def point_amount(self):
        return self._point_amount

    @point_amount.setter
    def point_amount(self, value):
        self._point_amount = value
    @property
    def task_code(self):
        return self._task_code

    @task_code.setter
    def task_code(self, value):
        self._task_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.exchange_token:
            if hasattr(self.exchange_token, 'to_alipay_dict'):
                params['exchange_token'] = self.exchange_token.to_alipay_dict()
            else:
                params['exchange_token'] = self.exchange_token
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.point_amount:
            if hasattr(self.point_amount, 'to_alipay_dict'):
                params['point_amount'] = self.point_amount.to_alipay_dict()
            else:
                params['point_amount'] = self.point_amount
        if self.task_code:
            if hasattr(self.task_code, 'to_alipay_dict'):
                params['task_code'] = self.task_code.to_alipay_dict()
            else:
                params['task_code'] = self.task_code
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
        o = AlipayCommerceOperationPromoterExchangeSubmitModel()
        if 'exchange_token' in d:
            o.exchange_token = d['exchange_token']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'pid' in d:
            o.pid = d['pid']
        if 'point_amount' in d:
            o.point_amount = d['point_amount']
        if 'task_code' in d:
            o.task_code = d['task_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


