#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SpiDetectionTask import SpiDetectionTask


class AlipayEcoTextDetectModel(object):

    def __init__(self):
        self._task = None

    @property
    def task(self):
        return self._task

    @task.setter
    def task(self, value):
        if isinstance(value, list):
            self._task = list()
            for i in value:
                if isinstance(i, SpiDetectionTask):
                    self._task.append(i)
                else:
                    self._task.append(SpiDetectionTask.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.task:
            if isinstance(self.task, list):
                for i in range(0, len(self.task)):
                    element = self.task[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.task[i] = element.to_alipay_dict()
            if hasattr(self.task, 'to_alipay_dict'):
                params['task'] = self.task.to_alipay_dict()
            else:
                params['task'] = self.task
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoTextDetectModel()
        if 'task' in d:
            o.task = d['task']
        return o


