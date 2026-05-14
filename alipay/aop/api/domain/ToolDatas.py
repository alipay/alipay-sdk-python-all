#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ToolDatas(object):

    def __init__(self):
        self._keyword = None
        self._problem = None
        self._solution = None
        self._solution_type = None
        self._task_id = None

    @property
    def keyword(self):
        return self._keyword

    @keyword.setter
    def keyword(self, value):
        self._keyword = value
    @property
    def problem(self):
        return self._problem

    @problem.setter
    def problem(self, value):
        self._problem = value
    @property
    def solution(self):
        return self._solution

    @solution.setter
    def solution(self, value):
        self._solution = value
    @property
    def solution_type(self):
        return self._solution_type

    @solution_type.setter
    def solution_type(self, value):
        self._solution_type = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.keyword:
            if hasattr(self.keyword, 'to_alipay_dict'):
                params['keyword'] = self.keyword.to_alipay_dict()
            else:
                params['keyword'] = self.keyword
        if self.problem:
            if hasattr(self.problem, 'to_alipay_dict'):
                params['problem'] = self.problem.to_alipay_dict()
            else:
                params['problem'] = self.problem
        if self.solution:
            if hasattr(self.solution, 'to_alipay_dict'):
                params['solution'] = self.solution.to_alipay_dict()
            else:
                params['solution'] = self.solution
        if self.solution_type:
            if hasattr(self.solution_type, 'to_alipay_dict'):
                params['solution_type'] = self.solution_type.to_alipay_dict()
            else:
                params['solution_type'] = self.solution_type
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
        o = ToolDatas()
        if 'keyword' in d:
            o.keyword = d['keyword']
        if 'problem' in d:
            o.problem = d['problem']
        if 'solution' in d:
            o.solution = d['solution']
        if 'solution_type' in d:
            o.solution_type = d['solution_type']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


