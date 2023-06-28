#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCommonTaskdataQueryModel(object):

    def __init__(self):
        self._merchant_pid = None
        self._task_instance_id = None
        self._task_templete_id = None

    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def task_instance_id(self):
        return self._task_instance_id

    @task_instance_id.setter
    def task_instance_id(self, value):
        self._task_instance_id = value
    @property
    def task_templete_id(self):
        return self._task_templete_id

    @task_templete_id.setter
    def task_templete_id(self, value):
        self._task_templete_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.task_instance_id:
            if hasattr(self.task_instance_id, 'to_alipay_dict'):
                params['task_instance_id'] = self.task_instance_id.to_alipay_dict()
            else:
                params['task_instance_id'] = self.task_instance_id
        if self.task_templete_id:
            if hasattr(self.task_templete_id, 'to_alipay_dict'):
                params['task_templete_id'] = self.task_templete_id.to_alipay_dict()
            else:
                params['task_templete_id'] = self.task_templete_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCommonTaskdataQueryModel()
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'task_instance_id' in d:
            o.task_instance_id = d['task_instance_id']
        if 'task_templete_id' in d:
            o.task_templete_id = d['task_templete_id']
        return o


