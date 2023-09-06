#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceWaterTaskCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceWaterTaskCreateResponse, self).__init__()
        self._task_id = None
        self._task_result = None

    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def task_result(self):
        return self._task_result

    @task_result.setter
    def task_result(self, value):
        self._task_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceWaterTaskCreateResponse, self).parse_response_content(response_content)
        if 'task_id' in response:
            self.task_id = response['task_id']
        if 'task_result' in response:
            self.task_result = response['task_result']
