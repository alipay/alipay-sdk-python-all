#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppProdmodeTasknodeQueryModel(object):

    def __init__(self):
        self._task_id = None

    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
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
        o = AlipayEbppProdmodeTasknodeQueryModel()
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


