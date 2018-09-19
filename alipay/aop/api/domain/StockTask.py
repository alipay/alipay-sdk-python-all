#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StockTask(object):

    def __init__(self):
        self._ad_user_id = None
        self._query_time = None
        self._status = None
        self._task_id = None

    @property
    def ad_user_id(self):
        return self._ad_user_id

    @ad_user_id.setter
    def ad_user_id(self, value):
        self._ad_user_id = value
    @property
    def query_time(self):
        return self._query_time

    @query_time.setter
    def query_time(self, value):
        self._query_time = value
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
        if self.ad_user_id:
            if hasattr(self.ad_user_id, 'to_alipay_dict'):
                params['ad_user_id'] = self.ad_user_id.to_alipay_dict()
            else:
                params['ad_user_id'] = self.ad_user_id
        if self.query_time:
            if hasattr(self.query_time, 'to_alipay_dict'):
                params['query_time'] = self.query_time.to_alipay_dict()
            else:
                params['query_time'] = self.query_time
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
        o = StockTask()
        if 'ad_user_id' in d:
            o.ad_user_id = d['ad_user_id']
        if 'query_time' in d:
            o.query_time = d['query_time']
        if 'status' in d:
            o.status = d['status']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


