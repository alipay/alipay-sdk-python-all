#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceWaterUsertaskModifyModel(object):

    def __init__(self):
        self._change_type = None
        self._goods_exception_desc = None
        self._pay_amount = None
        self._task_id = None
        self._user_task_id = None

    @property
    def change_type(self):
        return self._change_type

    @change_type.setter
    def change_type(self, value):
        self._change_type = value
    @property
    def goods_exception_desc(self):
        return self._goods_exception_desc

    @goods_exception_desc.setter
    def goods_exception_desc(self, value):
        self._goods_exception_desc = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def user_task_id(self):
        return self._user_task_id

    @user_task_id.setter
    def user_task_id(self, value):
        self._user_task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.change_type:
            if hasattr(self.change_type, 'to_alipay_dict'):
                params['change_type'] = self.change_type.to_alipay_dict()
            else:
                params['change_type'] = self.change_type
        if self.goods_exception_desc:
            if hasattr(self.goods_exception_desc, 'to_alipay_dict'):
                params['goods_exception_desc'] = self.goods_exception_desc.to_alipay_dict()
            else:
                params['goods_exception_desc'] = self.goods_exception_desc
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.user_task_id:
            if hasattr(self.user_task_id, 'to_alipay_dict'):
                params['user_task_id'] = self.user_task_id.to_alipay_dict()
            else:
                params['user_task_id'] = self.user_task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceWaterUsertaskModifyModel()
        if 'change_type' in d:
            o.change_type = d['change_type']
        if 'goods_exception_desc' in d:
            o.goods_exception_desc = d['goods_exception_desc']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'user_task_id' in d:
            o.user_task_id = d['user_task_id']
        return o


