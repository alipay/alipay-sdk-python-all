#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantIndirectFiletaskSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantIndirectFiletaskSubmitResponse, self).__init__()
        self._task_file_no = None
        self._task_state = None
        self._task_state_desc = None

    @property
    def task_file_no(self):
        return self._task_file_no

    @task_file_no.setter
    def task_file_no(self, value):
        self._task_file_no = value
    @property
    def task_state(self):
        return self._task_state

    @task_state.setter
    def task_state(self, value):
        self._task_state = value
    @property
    def task_state_desc(self):
        return self._task_state_desc

    @task_state_desc.setter
    def task_state_desc(self, value):
        self._task_state_desc = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantIndirectFiletaskSubmitResponse, self).parse_response_content(response_content)
        if 'task_file_no' in response:
            self.task_file_no = response['task_file_no']
        if 'task_state' in response:
            self.task_state = response['task_state']
        if 'task_state_desc' in response:
            self.task_state_desc = response['task_state_desc']
