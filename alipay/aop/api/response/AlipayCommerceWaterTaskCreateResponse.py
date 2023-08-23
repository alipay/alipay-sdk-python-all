#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceWaterTaskCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceWaterTaskCreateResponse, self).__init__()
        self._task_result = None

    @property
    def task_result(self):
        return self._task_result

    @task_result.setter
    def task_result(self, value):
        self._task_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceWaterTaskCreateResponse, self).parse_response_content(response_content)
        if 'task_result' in response:
            self.task_result = response['task_result']
