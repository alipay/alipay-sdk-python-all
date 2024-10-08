#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceYuntaskSupervisortaskQueryModel(object):

    def __init__(self):
        self._supervisor_id = None
        self._task_instance_id = None
        self._task_template_id = None

    @property
    def supervisor_id(self):
        return self._supervisor_id

    @supervisor_id.setter
    def supervisor_id(self, value):
        self._supervisor_id = value
    @property
    def task_instance_id(self):
        return self._task_instance_id

    @task_instance_id.setter
    def task_instance_id(self, value):
        self._task_instance_id = value
    @property
    def task_template_id(self):
        return self._task_template_id

    @task_template_id.setter
    def task_template_id(self, value):
        self._task_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.supervisor_id:
            if hasattr(self.supervisor_id, 'to_alipay_dict'):
                params['supervisor_id'] = self.supervisor_id.to_alipay_dict()
            else:
                params['supervisor_id'] = self.supervisor_id
        if self.task_instance_id:
            if hasattr(self.task_instance_id, 'to_alipay_dict'):
                params['task_instance_id'] = self.task_instance_id.to_alipay_dict()
            else:
                params['task_instance_id'] = self.task_instance_id
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
        o = AlipayCommerceYuntaskSupervisortaskQueryModel()
        if 'supervisor_id' in d:
            o.supervisor_id = d['supervisor_id']
        if 'task_instance_id' in d:
            o.task_instance_id = d['task_instance_id']
        if 'task_template_id' in d:
            o.task_template_id = d['task_template_id']
        return o


