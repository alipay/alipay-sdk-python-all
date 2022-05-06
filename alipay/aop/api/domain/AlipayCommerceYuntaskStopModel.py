#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceYuntaskStopModel(object):

    def __init__(self):
        self._merchant_pid = None
        self._operate_user_id = None
        self._task_template_id = None

    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def operate_user_id(self):
        return self._operate_user_id

    @operate_user_id.setter
    def operate_user_id(self, value):
        self._operate_user_id = value
    @property
    def task_template_id(self):
        return self._task_template_id

    @task_template_id.setter
    def task_template_id(self, value):
        self._task_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.operate_user_id:
            if hasattr(self.operate_user_id, 'to_alipay_dict'):
                params['operate_user_id'] = self.operate_user_id.to_alipay_dict()
            else:
                params['operate_user_id'] = self.operate_user_id
        if self.task_template_id:
            if hasattr(self.task_template_id, 'to_alipay_dict'):
                params['task_template_id'] = self.task_template_id.to_alipay_dict()
            else:
                params['task_template_id'] = self.task_template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceYuntaskStopModel()
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'operate_user_id' in d:
            o.operate_user_id = d['operate_user_id']
        if 'task_template_id' in d:
            o.task_template_id = d['task_template_id']
        return o


