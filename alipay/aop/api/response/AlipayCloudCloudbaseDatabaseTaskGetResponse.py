#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseDatabaseTaskGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseDatabaseTaskGetResponse, self).__init__()
        self._process = None
        self._start_time = None
        self._status = None
        self._task_type = None

    @property
    def process(self):
        return self._process

    @process.setter
    def process(self, value):
        self._process = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseDatabaseTaskGetResponse, self).parse_response_content(response_content)
        if 'process' in response:
            self.process = response['process']
        if 'start_time' in response:
            self.start_time = response['start_time']
        if 'status' in response:
            self.status = response['status']
        if 'task_type' in response:
            self.task_type = response['task_type']
