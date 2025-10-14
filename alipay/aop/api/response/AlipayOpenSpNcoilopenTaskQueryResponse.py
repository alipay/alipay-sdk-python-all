#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpNcoilopenTaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNcoilopenTaskQueryResponse, self).__init__()
        self._fail_file_url = None
        self._fail_number = None
        self._task_progress = None

    @property
    def fail_file_url(self):
        return self._fail_file_url

    @fail_file_url.setter
    def fail_file_url(self, value):
        self._fail_file_url = value
    @property
    def fail_number(self):
        return self._fail_number

    @fail_number.setter
    def fail_number(self, value):
        self._fail_number = value
    @property
    def task_progress(self):
        return self._task_progress

    @task_progress.setter
    def task_progress(self, value):
        self._task_progress = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNcoilopenTaskQueryResponse, self).parse_response_content(response_content)
        if 'fail_file_url' in response:
            self.fail_file_url = response['fail_file_url']
        if 'fail_number' in response:
            self.fail_number = response['fail_number']
        if 'task_progress' in response:
            self.task_progress = response['task_progress']
