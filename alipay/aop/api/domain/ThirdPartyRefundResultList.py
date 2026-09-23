#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ThirdPartyRefundResultList(object):

    def __init__(self):
        self._failure_reason = None
        self._platform_order_no = None
        self._status = None
        self._task_id = None

    @property
    def failure_reason(self):
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, value):
        self._failure_reason = value
    @property
    def platform_order_no(self):
        return self._platform_order_no

    @platform_order_no.setter
    def platform_order_no(self, value):
        self._platform_order_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.failure_reason:
            if hasattr(self.failure_reason, 'to_alipay_dict'):
                params['failure_reason'] = self.failure_reason.to_alipay_dict()
            else:
                params['failure_reason'] = self.failure_reason
        if self.platform_order_no:
            if hasattr(self.platform_order_no, 'to_alipay_dict'):
                params['platform_order_no'] = self.platform_order_no.to_alipay_dict()
            else:
                params['platform_order_no'] = self.platform_order_no
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ThirdPartyRefundResultList()
        if 'failure_reason' in d:
            o.failure_reason = d['failure_reason']
        if 'platform_order_no' in d:
            o.platform_order_no = d['platform_order_no']
        if 'status' in d:
            o.status = d['status']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


