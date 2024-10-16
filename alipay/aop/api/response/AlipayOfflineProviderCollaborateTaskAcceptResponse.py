#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CollaborateTask import CollaborateTask


class AlipayOfflineProviderCollaborateTaskAcceptResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderCollaborateTaskAcceptResponse, self).__init__()
        self._task = None
        self._task_no = None

    @property
    def task(self):
        return self._task

    @task.setter
    def task(self, value):
        if isinstance(value, CollaborateTask):
            self._task = value
        else:
            self._task = CollaborateTask.from_alipay_dict(value)
    @property
    def task_no(self):
        return self._task_no

    @task_no.setter
    def task_no(self, value):
        self._task_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderCollaborateTaskAcceptResponse, self).parse_response_content(response_content)
        if 'task' in response:
            self.task = response['task']
        if 'task_no' in response:
            self.task_no = response['task_no']
