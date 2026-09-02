#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaskCreateResponse import TaskCreateResponse


class AlipayCommerceMedicalHomedoctorFollowuptaskCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHomedoctorFollowuptaskCreateResponse, self).__init__()
        self._task_list = None

    @property
    def task_list(self):
        return self._task_list

    @task_list.setter
    def task_list(self, value):
        if isinstance(value, list):
            self._task_list = list()
            for i in value:
                if isinstance(i, TaskCreateResponse):
                    self._task_list.append(i)
                else:
                    self._task_list.append(TaskCreateResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHomedoctorFollowuptaskCreateResponse, self).parse_response_content(response_content)
        if 'task_list' in response:
            self.task_list = response['task_list']
