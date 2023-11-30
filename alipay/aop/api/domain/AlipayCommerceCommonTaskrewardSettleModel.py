#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCommonTaskrewardSettleModel(object):

    def __init__(self):
        self._hunter_id = None
        self._hunter_open_id = None
        self._operator = None
        self._out_biz_no = None
        self._reward_way = None
        self._task_instance_id = None
        self._unfreeze_time = None
        self._valid_trade_amount = None

    @property
    def hunter_id(self):
        return self._hunter_id

    @hunter_id.setter
    def hunter_id(self, value):
        self._hunter_id = value
    @property
    def hunter_open_id(self):
        return self._hunter_open_id

    @hunter_open_id.setter
    def hunter_open_id(self, value):
        self._hunter_open_id = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def reward_way(self):
        return self._reward_way

    @reward_way.setter
    def reward_way(self, value):
        self._reward_way = value
    @property
    def task_instance_id(self):
        return self._task_instance_id

    @task_instance_id.setter
    def task_instance_id(self, value):
        self._task_instance_id = value
    @property
    def unfreeze_time(self):
        return self._unfreeze_time

    @unfreeze_time.setter
    def unfreeze_time(self, value):
        self._unfreeze_time = value
    @property
    def valid_trade_amount(self):
        return self._valid_trade_amount

    @valid_trade_amount.setter
    def valid_trade_amount(self, value):
        self._valid_trade_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.hunter_id:
            if hasattr(self.hunter_id, 'to_alipay_dict'):
                params['hunter_id'] = self.hunter_id.to_alipay_dict()
            else:
                params['hunter_id'] = self.hunter_id
        if self.hunter_open_id:
            if hasattr(self.hunter_open_id, 'to_alipay_dict'):
                params['hunter_open_id'] = self.hunter_open_id.to_alipay_dict()
            else:
                params['hunter_open_id'] = self.hunter_open_id
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.reward_way:
            if hasattr(self.reward_way, 'to_alipay_dict'):
                params['reward_way'] = self.reward_way.to_alipay_dict()
            else:
                params['reward_way'] = self.reward_way
        if self.task_instance_id:
            if hasattr(self.task_instance_id, 'to_alipay_dict'):
                params['task_instance_id'] = self.task_instance_id.to_alipay_dict()
            else:
                params['task_instance_id'] = self.task_instance_id
        if self.unfreeze_time:
            if hasattr(self.unfreeze_time, 'to_alipay_dict'):
                params['unfreeze_time'] = self.unfreeze_time.to_alipay_dict()
            else:
                params['unfreeze_time'] = self.unfreeze_time
        if self.valid_trade_amount:
            if hasattr(self.valid_trade_amount, 'to_alipay_dict'):
                params['valid_trade_amount'] = self.valid_trade_amount.to_alipay_dict()
            else:
                params['valid_trade_amount'] = self.valid_trade_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCommonTaskrewardSettleModel()
        if 'hunter_id' in d:
            o.hunter_id = d['hunter_id']
        if 'hunter_open_id' in d:
            o.hunter_open_id = d['hunter_open_id']
        if 'operator' in d:
            o.operator = d['operator']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'reward_way' in d:
            o.reward_way = d['reward_way']
        if 'task_instance_id' in d:
            o.task_instance_id = d['task_instance_id']
        if 'unfreeze_time' in d:
            o.unfreeze_time = d['unfreeze_time']
        if 'valid_trade_amount' in d:
            o.valid_trade_amount = d['valid_trade_amount']
        return o


