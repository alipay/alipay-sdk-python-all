#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditGoInfo(object):

    def __init__(self):
        self._benefit = None
        self._task = None
        self._template_id = None

    @property
    def benefit(self):
        return self._benefit

    @benefit.setter
    def benefit(self, value):
        self._benefit = value
    @property
    def task(self):
        return self._task

    @task.setter
    def task(self, value):
        self._task = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit:
            if hasattr(self.benefit, 'to_alipay_dict'):
                params['benefit'] = self.benefit.to_alipay_dict()
            else:
                params['benefit'] = self.benefit
        if self.task:
            if hasattr(self.task, 'to_alipay_dict'):
                params['task'] = self.task.to_alipay_dict()
            else:
                params['task'] = self.task
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditGoInfo()
        if 'benefit' in d:
            o.benefit = d['benefit']
        if 'task' in d:
            o.task = d['task']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


