#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TaskDetailResponse import TaskDetailResponse


class TaskDetailListResponse(object):

    def __init__(self):
        self._task_detail_list_response = None

    @property
    def task_detail_list_response(self):
        return self._task_detail_list_response

    @task_detail_list_response.setter
    def task_detail_list_response(self, value):
        if isinstance(value, list):
            self._task_detail_list_response = list()
            for i in value:
                if isinstance(i, TaskDetailResponse):
                    self._task_detail_list_response.append(i)
                else:
                    self._task_detail_list_response.append(TaskDetailResponse.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.task_detail_list_response:
            if isinstance(self.task_detail_list_response, list):
                for i in range(0, len(self.task_detail_list_response)):
                    element = self.task_detail_list_response[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.task_detail_list_response[i] = element.to_alipay_dict()
            if hasattr(self.task_detail_list_response, 'to_alipay_dict'):
                params['task_detail_list_response'] = self.task_detail_list_response.to_alipay_dict()
            else:
                params['task_detail_list_response'] = self.task_detail_list_response
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskDetailListResponse()
        if 'task_detail_list_response' in d:
            o.task_detail_list_response = d['task_detail_list_response']
        return o


