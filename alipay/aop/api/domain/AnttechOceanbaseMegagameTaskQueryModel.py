#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseMegagameTaskQueryModel(object):

    def __init__(self):
        self._run_task_time_out_minutes = None
        self._team_id = None

    @property
    def run_task_time_out_minutes(self):
        return self._run_task_time_out_minutes

    @run_task_time_out_minutes.setter
    def run_task_time_out_minutes(self, value):
        self._run_task_time_out_minutes = value
    @property
    def team_id(self):
        return self._team_id

    @team_id.setter
    def team_id(self, value):
        self._team_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.run_task_time_out_minutes:
            if hasattr(self.run_task_time_out_minutes, 'to_alipay_dict'):
                params['run_task_time_out_minutes'] = self.run_task_time_out_minutes.to_alipay_dict()
            else:
                params['run_task_time_out_minutes'] = self.run_task_time_out_minutes
        if self.team_id:
            if hasattr(self.team_id, 'to_alipay_dict'):
                params['team_id'] = self.team_id.to_alipay_dict()
            else:
                params['team_id'] = self.team_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseMegagameTaskQueryModel()
        if 'run_task_time_out_minutes' in d:
            o.run_task_time_out_minutes = d['run_task_time_out_minutes']
        if 'team_id' in d:
            o.team_id = d['team_id']
        return o


