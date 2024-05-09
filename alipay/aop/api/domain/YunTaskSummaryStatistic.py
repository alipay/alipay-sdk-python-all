#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class YunTaskSummaryStatistic(object):

    def __init__(self):
        self._active_shop_cnt = None
        self._bind_hunter_cnt = None
        self._task_incentive_amount = None
        self._task_incentive_cnt = None
        self._task_receive_cnt = None
        self._task_total_cnt = None

    @property
    def active_shop_cnt(self):
        return self._active_shop_cnt

    @active_shop_cnt.setter
    def active_shop_cnt(self, value):
        self._active_shop_cnt = value
    @property
    def bind_hunter_cnt(self):
        return self._bind_hunter_cnt

    @bind_hunter_cnt.setter
    def bind_hunter_cnt(self, value):
        self._bind_hunter_cnt = value
    @property
    def task_incentive_amount(self):
        return self._task_incentive_amount

    @task_incentive_amount.setter
    def task_incentive_amount(self, value):
        self._task_incentive_amount = value
    @property
    def task_incentive_cnt(self):
        return self._task_incentive_cnt

    @task_incentive_cnt.setter
    def task_incentive_cnt(self, value):
        self._task_incentive_cnt = value
    @property
    def task_receive_cnt(self):
        return self._task_receive_cnt

    @task_receive_cnt.setter
    def task_receive_cnt(self, value):
        self._task_receive_cnt = value
    @property
    def task_total_cnt(self):
        return self._task_total_cnt

    @task_total_cnt.setter
    def task_total_cnt(self, value):
        self._task_total_cnt = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_shop_cnt:
            if hasattr(self.active_shop_cnt, 'to_alipay_dict'):
                params['active_shop_cnt'] = self.active_shop_cnt.to_alipay_dict()
            else:
                params['active_shop_cnt'] = self.active_shop_cnt
        if self.bind_hunter_cnt:
            if hasattr(self.bind_hunter_cnt, 'to_alipay_dict'):
                params['bind_hunter_cnt'] = self.bind_hunter_cnt.to_alipay_dict()
            else:
                params['bind_hunter_cnt'] = self.bind_hunter_cnt
        if self.task_incentive_amount:
            if hasattr(self.task_incentive_amount, 'to_alipay_dict'):
                params['task_incentive_amount'] = self.task_incentive_amount.to_alipay_dict()
            else:
                params['task_incentive_amount'] = self.task_incentive_amount
        if self.task_incentive_cnt:
            if hasattr(self.task_incentive_cnt, 'to_alipay_dict'):
                params['task_incentive_cnt'] = self.task_incentive_cnt.to_alipay_dict()
            else:
                params['task_incentive_cnt'] = self.task_incentive_cnt
        if self.task_receive_cnt:
            if hasattr(self.task_receive_cnt, 'to_alipay_dict'):
                params['task_receive_cnt'] = self.task_receive_cnt.to_alipay_dict()
            else:
                params['task_receive_cnt'] = self.task_receive_cnt
        if self.task_total_cnt:
            if hasattr(self.task_total_cnt, 'to_alipay_dict'):
                params['task_total_cnt'] = self.task_total_cnt.to_alipay_dict()
            else:
                params['task_total_cnt'] = self.task_total_cnt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = YunTaskSummaryStatistic()
        if 'active_shop_cnt' in d:
            o.active_shop_cnt = d['active_shop_cnt']
        if 'bind_hunter_cnt' in d:
            o.bind_hunter_cnt = d['bind_hunter_cnt']
        if 'task_incentive_amount' in d:
            o.task_incentive_amount = d['task_incentive_amount']
        if 'task_incentive_cnt' in d:
            o.task_incentive_cnt = d['task_incentive_cnt']
        if 'task_receive_cnt' in d:
            o.task_receive_cnt = d['task_receive_cnt']
        if 'task_total_cnt' in d:
            o.task_total_cnt = d['task_total_cnt']
        return o


