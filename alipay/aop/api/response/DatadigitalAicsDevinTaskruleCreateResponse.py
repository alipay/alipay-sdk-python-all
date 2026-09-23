#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalAicsDevinTaskruleCreateResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalAicsDevinTaskruleCreateResponse, self).__init__()
        self._task_code = None
        self._task_name = None
        self._task_rules_code = None

    @property
    def task_code(self):
        return self._task_code

    @task_code.setter
    def task_code(self, value):
        self._task_code = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def task_rules_code(self):
        return self._task_rules_code

    @task_rules_code.setter
    def task_rules_code(self, value):
        self._task_rules_code = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalAicsDevinTaskruleCreateResponse, self).parse_response_content(response_content)
        if 'task_code' in response:
            self.task_code = response['task_code']
        if 'task_name' in response:
            self.task_name = response['task_name']
        if 'task_rules_code' in response:
            self.task_rules_code = response['task_rules_code']
