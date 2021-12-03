#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseMegagameTaskQueryModel(object):

    def __init__(self):
        self._run_task_time_out_minutes = None

    @property
    def run_task_time_out_minutes(self):
        return self._run_task_time_out_minutes

    @run_task_time_out_minutes.setter
    def run_task_time_out_minutes(self, value):
        self._run_task_time_out_minutes = value


    def to_alipay_dict(self):
        params = dict()
        if self.run_task_time_out_minutes:
            if hasattr(self.run_task_time_out_minutes, 'to_alipay_dict'):
                params['run_task_time_out_minutes'] = self.run_task_time_out_minutes.to_alipay_dict()
            else:
                params['run_task_time_out_minutes'] = self.run_task_time_out_minutes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseMegagameTaskQueryModel()
        if 'run_task_time_out_minutes' in d:
            o.run_task_time_out_minutes = d['run_task_time_out_minutes']
        return o


