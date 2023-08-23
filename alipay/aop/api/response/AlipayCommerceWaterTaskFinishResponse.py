#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceWaterTaskFinishResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceWaterTaskFinishResponse, self).__init__()
        self._task_result = None

    @property
    def task_result(self):
        return self._task_result

    @task_result.setter
    def task_result(self, value):
        self._task_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceWaterTaskFinishResponse, self).parse_response_content(response_content)
        if 'task_result' in response:
            self.task_result = response['task_result']
