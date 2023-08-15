#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QueryUserTaskListResponse(object):

    def __init__(self):
        self._out_biz_no = None
        self._prize_name = None
        self._prize_price = None
        self._task_id = None
        self._task_name = None
        self._task_pay_status = None
        self._task_status = None
        self._user_task_id = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value
    @property
    def prize_price(self):
        return self._prize_price

    @prize_price.setter
    def prize_price(self, value):
        self._prize_price = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def task_pay_status(self):
        return self._task_pay_status

    @task_pay_status.setter
    def task_pay_status(self, value):
        self._task_pay_status = value
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value
    @property
    def user_task_id(self):
        return self._user_task_id

    @user_task_id.setter
    def user_task_id(self, value):
        self._user_task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        if self.prize_price:
            if hasattr(self.prize_price, 'to_alipay_dict'):
                params['prize_price'] = self.prize_price.to_alipay_dict()
            else:
                params['prize_price'] = self.prize_price
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        if self.task_pay_status:
            if hasattr(self.task_pay_status, 'to_alipay_dict'):
                params['task_pay_status'] = self.task_pay_status.to_alipay_dict()
            else:
                params['task_pay_status'] = self.task_pay_status
        if self.task_status:
            if hasattr(self.task_status, 'to_alipay_dict'):
                params['task_status'] = self.task_status.to_alipay_dict()
            else:
                params['task_status'] = self.task_status
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
        o = QueryUserTaskListResponse()
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'prize_price' in d:
            o.prize_price = d['prize_price']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'task_pay_status' in d:
            o.task_pay_status = d['task_pay_status']
        if 'task_status' in d:
            o.task_status = d['task_status']
        if 'user_task_id' in d:
            o.user_task_id = d['user_task_id']
        return o


