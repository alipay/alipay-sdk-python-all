#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HardeningTaskResponse(object):

    def __init__(self):
        self._after_md_five = None
        self._after_size = None
        self._status = None
        self._task_id = None

    @property
    def after_md_five(self):
        return self._after_md_five

    @after_md_five.setter
    def after_md_five(self, value):
        self._after_md_five = value
    @property
    def after_size(self):
        return self._after_size

    @after_size.setter
    def after_size(self, value):
        self._after_size = value
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
        if self.after_md_five:
            if hasattr(self.after_md_five, 'to_alipay_dict'):
                params['after_md_five'] = self.after_md_five.to_alipay_dict()
            else:
                params['after_md_five'] = self.after_md_five
        if self.after_size:
            if hasattr(self.after_size, 'to_alipay_dict'):
                params['after_size'] = self.after_size.to_alipay_dict()
            else:
                params['after_size'] = self.after_size
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
        o = HardeningTaskResponse()
        if 'after_md_five' in d:
            o.after_md_five = d['after_md_five']
        if 'after_size' in d:
            o.after_size = d['after_size']
        if 'status' in d:
            o.status = d['status']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


