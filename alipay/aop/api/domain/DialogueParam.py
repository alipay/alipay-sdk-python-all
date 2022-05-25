#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DialogueParam(object):

    def __init__(self):
        self._file_id = None
        self._task_id = None

    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
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
        o = DialogueParam()
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


