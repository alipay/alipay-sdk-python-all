#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAccountExrateConfigQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAccountExrateConfigQueryResponse, self).__init__()
        self._task_context = None
        self._task_status = None
        self._task_type = None

    @property
    def task_context(self):
        return self._task_context

    @task_context.setter
    def task_context(self, value):
        self._task_context = value
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayAccountExrateConfigQueryResponse, self).parse_response_content(response_content)
        if 'task_context' in response:
            self.task_context = response['task_context']
        if 'task_status' in response:
            self.task_status = response['task_status']
        if 'task_type' in response:
            self.task_type = response['task_type']
