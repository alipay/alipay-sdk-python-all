#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechMorseDataserviceInsightreportQueryModel(object):

    def __init__(self):
        self._consult_id = None
        self._task_id = None

    @property
    def consult_id(self):
        return self._consult_id

    @consult_id.setter
    def consult_id(self, value):
        self._consult_id = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.consult_id:
            if hasattr(self.consult_id, 'to_alipay_dict'):
                params['consult_id'] = self.consult_id.to_alipay_dict()
            else:
                params['consult_id'] = self.consult_id
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
        o = AnttechMorseDataserviceInsightreportQueryModel()
        if 'consult_id' in d:
            o.consult_id = d['consult_id']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


