#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderCollaborateTaskReceiveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderCollaborateTaskReceiveResponse, self).__init__()
        self._task_no = None

    @property
    def task_no(self):
        return self._task_no

    @task_no.setter
    def task_no(self, value):
        self._task_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderCollaborateTaskReceiveResponse, self).parse_response_content(response_content)
        if 'task_no' in response:
            self.task_no = response['task_no']
