#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechAiCvDsbGetResponse(AlipayResponse):

    def __init__(self):
        super(AnttechAiCvDsbGetResponse, self).__init__()
        self._result_url = None
        self._status = None
        self._task_id = None

    @property
    def result_url(self):
        return self._result_url

    @result_url.setter
    def result_url(self, value):
        self._result_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechAiCvDsbGetResponse, self).parse_response_content(response_content)
        if 'result_url' in response:
            self.result_url = response['result_url']
        if 'status' in response:
            self.status = response['status']
        if 'task_id' in response:
            self.task_id = response['task_id']
