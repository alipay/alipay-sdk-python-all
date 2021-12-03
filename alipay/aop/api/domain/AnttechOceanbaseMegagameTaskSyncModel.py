#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseMegagameTaskSyncModel(object):

    def __init__(self):
        self._fail_msg = None
        self._id = None
        self._machine_score = None
        self._task_status = None

    @property
    def fail_msg(self):
        return self._fail_msg

    @fail_msg.setter
    def fail_msg(self, value):
        self._fail_msg = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def machine_score(self):
        return self._machine_score

    @machine_score.setter
    def machine_score(self, value):
        self._machine_score = value
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.fail_msg:
            if hasattr(self.fail_msg, 'to_alipay_dict'):
                params['fail_msg'] = self.fail_msg.to_alipay_dict()
            else:
                params['fail_msg'] = self.fail_msg
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.machine_score:
            if hasattr(self.machine_score, 'to_alipay_dict'):
                params['machine_score'] = self.machine_score.to_alipay_dict()
            else:
                params['machine_score'] = self.machine_score
        if self.task_status:
            if hasattr(self.task_status, 'to_alipay_dict'):
                params['task_status'] = self.task_status.to_alipay_dict()
            else:
                params['task_status'] = self.task_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseMegagameTaskSyncModel()
        if 'fail_msg' in d:
            o.fail_msg = d['fail_msg']
        if 'id' in d:
            o.id = d['id']
        if 'machine_score' in d:
            o.machine_score = d['machine_score']
        if 'task_status' in d:
            o.task_status = d['task_status']
        return o


