#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoAcceptanceTaskCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoAcceptanceTaskCreateResponse, self).__init__()
        self._task_id = None
        self._total_results = None

    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def total_results(self):
        return self._total_results

    @total_results.setter
    def total_results(self, value):
        self._total_results = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoAcceptanceTaskCreateResponse, self).parse_response_content(response_content)
        if 'task_id' in response:
            self.task_id = response['task_id']
        if 'total_results' in response:
            self.total_results = response['total_results']
