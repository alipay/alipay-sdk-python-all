#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFincoreProgovQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreProgovQueryResponse, self).__init__()
        self._task_status = None

    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreProgovQueryResponse, self).parse_response_content(response_content)
        if 'task_status' in response:
            self.task_status = response['task_status']
